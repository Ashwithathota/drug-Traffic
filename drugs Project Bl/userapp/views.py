from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
import urllib.request
import urllib.parse
from django.contrib.auth import logout
from django.core.mail import send_mail
import os
import random
from django.conf import settings
from userapp.models import *
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from PIL import Image
import pytesseract
import moviepy.editor as mp
import speech_recognition as sr

from mainapp.models import *



from django.http import JsonResponse
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable.
# Make sure Tesseract OCR is installed on your system.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def user_logout(request):
    logout(request)
    messages.info(request, "Logout Successfully ")
    return redirect("user_login")


# Create your views here.

def main_page(request):    
    return render(request,'user/main-page.html')


EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')




def contains_manual_violation(text):
    """Return True if any violation keyword is found in text."""
    if text:
        lower_text = text.lower()
        for keyword in VIOLATION_KEYWORDS:
            if keyword in lower_text:
                return True
    return False



def generate_otp(length=4):
    otp = "".join(random.choices("0123456789", k=length))
    return otp





import json
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from web3 import Web3

import re
from nltk.stem import WordNetLemmatizer
import pickle
# Load vectorizer and model
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
mnb = pickle.load(open('tweet.pkl', 'rb'))





def user_dashboard(request):
    user_id = request.session.get('user_id_after_login')
    user = get_object_or_404(User, id=user_id)
    friends = User.objects.filter(
        Q(sent_requests__to_user=user, sent_requests__is_accepted=True) |
        Q(received_requests__from_user=user, sent_requests__is_accepted=True)
    )
    posts = Post.objects.filter(
        Q(user__in=friends) | Q(user=user)
    ).order_by('-timestamp')

    # Helper function to perform blockchain mining for unposted content
    def mine_unposted_content_blockchain(user_obj, use_case='post'):
        try:
            w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
            if not w3.is_connected():
                messages.error(request, "Blockchain connection failed.")
                return
            with open("blockchain/build/contracts/Cannatch.json") as f:
                contract_json = json.load(f)
                contract_abi = contract_json["abi"]
            contract_address = "0x231cB0Ce79ff94818595e1cf9636eD96F2dD0343"
            contract = w3.eth.contract(address=contract_address, abi=contract_abi)
            account = w3.eth.accounts[0]
            w3.eth.default_account = account
            # Use a valid recipient address (using the default Ganache account in this example)
            recipient_address = account
            tx_hash = contract.functions.executeTransaction(recipient_address, 2000000).transact()
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            tx = w3.eth.get_transaction(tx_hash)
            block = w3.eth.get_block(tx_receipt['blockNumber'])
            mined_on = datetime.fromtimestamp(block['timestamp'])
            BlockchainTransaction.objects.create(
                user=user_obj,
                block_no=str(tx_receipt['blockNumber']),
                gas_used=str(tx_receipt['gasUsed']),
                gas_limit=str(tx['gas']),
                mined_on=mined_on,
                block_hash=tx_receipt['blockHash'].hex(),
                from_address=tx['from'],
                to_address=tx['to'],
                tx_hash=tx_receipt['transactionHash'].hex(),
                use_case=use_case  # Set the use case here
            )
        except Exception as e:
            messages.error(request, f"Blockchain transaction failed: {str(e)}")

    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        audio = request.FILES.get('audio')

        # Process inputs from various sources
        text_from_text = text.strip() if text else ""
        print(f"Text from text input:\n{text_from_text}")

        text_from_image = extract_text_from_image(image) if image else ""
        print(f"Text from image input:\n{text_from_image}")

        text_from_video = extract_text_from_video(video) if video else ""
        print(f"Text from video input:\n{text_from_video}")

        text_from_audio = extract_text_from_audio(audio) if audio else ""
        print(f"Text from audio input:\n{text_from_audio}")

        # Combine all extracted texts
        combined_text = "\n\n".join(filter(None, [text_from_text, text_from_image, text_from_video, text_from_audio]))
        print(f"Combined text:\n{combined_text}")

        # Check for manual violations first
        if contains_manual_violation(combined_text):
            messages.error(request, "Your post contains prohibited content and cannot be uploaded.")
            unposted_content = UnpostedContent(user_id=user_id, text=combined_text)
            if image:
                unposted_content.image = image
            if video:
                unposted_content.video = video
            if audio:
                unposted_content.audio = audio
            unposted_content.save()
            # Mine the unposted content on blockchain
            mine_unposted_content_blockchain(unposted_content.user)
            return JsonResponse({'status': 'success'})

        # Perform prediction using the classifier
        example_counts = vectorizer.transform([combined_text])
        prediction = mnb.predict(example_counts)[0]
        print(f"Prediction: {prediction}")

        if prediction == 0:
            new_post = Post(user_id=user_id, text=combined_text)
            if image:
                new_post.image = image
            if video:
                new_post.video = video
            if audio:
                new_post.audio = audio
            new_post.save()
            messages.success(request, "Your post has been successfully uploaded.")
        else:
            unposted_content = UnpostedContent(user_id=user_id, text=combined_text)
            if image:
                unposted_content.image = image
            if video:
                unposted_content.video = video
            if audio:
                unposted_content.audio = audio
            unposted_content.save()
            messages.error(request, "Your post contains prohibited content and cannot be uploaded.")
            # Mine the unposted content on blockchain
            mine_unposted_content_blockchain(unposted_content.user)
        return JsonResponse({'status': 'success'})

    context = {
        'posts': posts,
    }
    return render(request, "user/index.html", context)



def extract_text_from_image(image):
    print("Extracting text from image...")
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    return text.strip()

def extract_text_from_video(video):
    print("Extracting text from video...")
    video_clip = mp.VideoFileClip(video)
    audio_path = "temp_audio.wav"
    video_clip.audio.write_audiofile(audio_path)
    text = extract_text_from_audio(audio_path)
    os.remove(audio_path)  
    return text

def extract_text_from_audio(audio):
    print("Extracting text from audio...")
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text.strip()


def post_comment(request, post_id):
    text = request.POST.get('text')
    if not text:
        messages.error(request, "Please add some content to your comment.")
        return redirect('user_dashboard')
    user_id = request.session.get('user_id_after_login')
    post = get_object_or_404(Post, id=post_id)
    new_comment = Comment(post=post, user_id=user_id, text=text)
    new_comment.save()
    messages.success(request, "comment posted.")
    return redirect('user_dashboard')



def post_comment2(request, post_id):
    text = request.POST.get('text')
    if not text:
        messages.error(request, "Please add some content to your comment.")
        return redirect('user_dashboard')
    user_id = request.session.get('user_id_after_login')
    post = get_object_or_404(Post, id=post_id)
    new_comment = Comment(post=post, user_id=user_id, text=text)
    new_comment.save()
    messages.success(request, "comment posted.")
    return redirect('user_dashboard')



def like_post(request, post_id):
    user_id = request.session.get('user_id_after_login')
    post = get_object_or_404(Post, id=post_id)
    
    if user_id:
        user = get_object_or_404(User, id=user_id)
        post.likes.add(user)
        post.save()
    
    return redirect('user_dashboard')



def like_post2(request, post_id):
    user_id = request.session.get('user_id_after_login')
    post = get_object_or_404(Post, id=post_id)
    
    if user_id:
        user = get_object_or_404(User, id=user_id)
        post.likes.add(user)
        post.save()
    
    return redirect('visit_profile')


def user_profile(request):
    user_id = request.session['user_id_after_login']
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        try:
            profile = request.FILES['profile']
            user.photo = profile
        except MultiValueDictKeyError:
            profile = user.photo
        password = request.POST.get('password')
        location = request.POST.get('location')
        interests = request.POST.getlist('interests')

        user.full_name = name
        user.email = email
        user.phone_number = phone
        user.password = password
        user.address = location
        user.save()

        user.interests.clear()
        for interest_id in interests:
            interest = Interest.objects.get(id=interest_id)
            user.interests.add(interest)

        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')

    all_interests = Interest.objects.all()
    return render(request, "user/my-profile.html", {'user': user, 'all_interests': all_interests})



def res(request):
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        results = User.objects.filter(full_name__icontains=search_query)
    else:
        results = User.objects.none() 
    return render(request,"user/res.html",{'results': results})



from django.db.models import Q

def send_friend_request(request, recipient_id):
    if request.method == 'POST':
        user_id = request.session.get('user_id_after_login')
        if user_id:
            current_user = get_object_or_404(User, id=user_id)
            recipient_user = get_object_or_404(User, id=recipient_id)

            if FriendRequest.objects.filter(
                (Q(from_user=current_user, to_user=recipient_user) | Q(from_user=recipient_user, to_user=current_user)),
                is_accepted=True
            ).exists():
                messages.warning(request, 'You are already friends.')
            elif FriendRequest.objects.filter(from_user=current_user, to_user=recipient_user).exists():
                messages.warning(request, 'Friend request already sent.')
            else:
                friend_request = FriendRequest(from_user=current_user, to_user=recipient_user)
                friend_request.save()
                messages.success(request, 'Friend request sent successfully.')
            return redirect('res')
        else:
            messages.error(request, 'User ID not found in session.')
            return redirect('user_login')
    return redirect('res')



def fr_req(request):
    user_id = request.session.get('user_id_after_login')
    user = get_object_or_404(User, id=user_id)
    received_requests = FriendRequest.objects.filter(to_user=user, is_accepted=False)
    context = {
        'received_requests': received_requests,
    }
    return render(request, "user/friend-req.html", context)



def visit_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user).order_by('-timestamp')
    context = {
        'user_details': user,
        'posts': posts,
    }
    return render(request, "user/visit-profile.html", context)




def accept_friend_request(request, user_details_id):
    user_id = request.session.get('user_id_after_login')
    user = get_object_or_404(User, pk=user_id)
    friend_request = get_object_or_404(FriendRequest, from_user=user_details_id, to_user =user)
    friend_request.is_accepted = True
    friend_request.save()
    messages.success(request, f"Friend request from {friend_request.from_user.full_name} accepted.")
    return redirect('fr_req')


def reject_friend_request(request, user_details_id):
    user_id = request.session.get('user_id_after_login')
    user = get_object_or_404(User, pk=user_id)
    friend_request = get_object_or_404(FriendRequest, from_user=user_details_id,to_user =user)
    from_user_name = friend_request.from_user.full_name
    friend_request.delete()
    messages.info(request, f"Friend request from {from_user_name} rejected.")
    return redirect('fr_req')


from itertools import chain
from operator import attrgetter



def my_posts(request):
    user_id = request.session.get('user_id_after_login')
    user = get_object_or_404(User, pk=user_id)

    # Retrieve posts from both models, ordered by timestamp
    posted_content = Post.objects.filter(user=user).order_by('-timestamp')
    unposted_content = UnpostedContent.objects.filter(user=user).order_by('-timestamp')

    # Combine posts and sort by timestamp
    all_posts = sorted(
        chain(posted_content, unposted_content),
        key=attrgetter('timestamp'),
        reverse=True
    )

    # Create a list to store each post along with its type
    formatted_posts = []
    for post in all_posts:
        if isinstance(post, Post):
            formatted_posts.append((post, 'posted'))
        elif isinstance(post, UnpostedContent):
            formatted_posts.append((post, 'unposted'))

    return render(request, "user/myposts.html", {'formatted_posts': formatted_posts})



def user_messages(request):
    user_id = request.session.get('user_id_after_login')
    user = get_object_or_404(User, pk=user_id)
    my_messages = Message.objects.filter(to_user=user)
    
    if request.method == 'POST':
        print("POST request received.")
        user_id = request.session.get('user_id_after_login')
        print(f"user_id: {user_id}")
        from_user = get_object_or_404(User, pk=user_id)
        print(f"from_user: {from_user}")
        to_user_id = request.POST.get('to_user')
        print(f"to_user_id: {to_user_id}")
        to_user = get_object_or_404(User, pk=to_user_id)
        print(f"to_user: {to_user}")
        message_text = request.POST.get('message')
        print(f"message_text: {message_text}")

        # If message text exists, perform violation checks.
        if message_text:
            # Manual violation check
            if contains_manual_violation(message_text):
                messages.error(request, "Message cannot be sent due to violated content in the text")
                print("Manual violation detected in message text")
                return redirect('user_messages')
            # Classifier check using your vectorizer and mnb classifier
            example_counts = vectorizer.transform([message_text])
            prediction = mnb.predict(example_counts)[0]
            print(f"Prediction (text): {prediction}")
            if prediction == 1:
                messages.error(request, "Message cannot be sent due to violated content in the text")
                print("Classifier violation detected in message text")
                return redirect('user_messages')
            # If no violations, create the message
            message = Message.objects.create(
                from_user=from_user, 
                to_user=to_user, 
                message=message_text
            )
            messages.success(request, "Message sent successfully!")
            print("Message saved successfully.")
        else:
            messages.error(request, "Failed to send message. Message content is empty.") 
            print("Failed to save message.")
    return render(request, "user/messages.html", {'my_messages': my_messages}) 
VIOLATION_KEYWORDS = ['drugs', 'DRUGS', 'drug', 'DRUG', 'cocaine', 'COCAINE','heroin', 'HEROIN','meth', 'METH','methamphetamine', 'METHAMPHETAMINE','amphetamine', 'AMPHETAMINE',    'opioid', 'OPIOID','fentanyl', 'FENTANYL','ecstasy', 'ECSTASY','mdma', 'MDMA','weed', 'WEED','marijuana', 'MARIJUANA', 'crack', 'CRACK',    'opium', 'OPIUM','substance abuse', 'SUBSTANCE ABUSE','narcotics', 'NARCOTICS']
def mark_as_read(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.read = 'read'
    message.save()
    messages.success(request, 'Marked as read !')

    return redirect('user_messages')
def whatsapp(request):
    return render(request, "user/whatsapp.html")

def whatsapp_logout(request):
    messages.success(request, 'Logged out successfully.')
    return redirect('user_login')

def telegram(request):
    return render(request, "user/telegram.html")
def send_message(request):
    if request.method == 'POST':
        # Handle text message
        text_message = request.POST.get('message', '')
        if text_message:
            print(f"Text Message: {text_message}")
            # First, do a manual check for violation keywords
            if contains_manual_violation(text_message):
                print("Manual violation detected in text message")
                messages.error(request, "Message cannot be sent due to violated content in the text")   
                return JsonResponse({
                    'status': 'error',
                    'message': 'Message cannot be sent due to violated content in the text'
                }, status=400)
            # Process text message using your vectorizer and classifier
            example_counts = vectorizer.transform([text_message])
            prediction = mnb.predict(example_counts)[0]
            print(f"Prediction (text): {prediction}")
            if prediction == 1:
                messages.error(request, 'Message cannot be sent due to violated content in the text')
                return JsonResponse({
                    'status': 'error',
                    'message': 'Message cannot be sent due to violated content in the text'
                }, status=400)

        # Handle file attachments (assume these are images)
        files = request.FILES.getlist('attachments')
        for file in files:
            print(f"File received: {file.name} ({file.content_type}), Size: {file.size} bytes")
            
            # Extract text from the image
            text_from_image = extract_text_from_image(file) if file else ""
            print(f"Text from image input:\n{text_from_image}")
            
            # Check manually for violation keywords in the extracted text
            if contains_manual_violation(text_from_image):
                print("Manual violation detected in image text")
                messages.error(request, 'Image cannot be sent due to violated content in the text')
                return JsonResponse({
                    'status': 'error',
                    'message': 'Image cannot be sent due to violated content in the text'
                }, status=400)
            
            example_counts = vectorizer.transform([text_from_image])
            prediction = mnb.predict(example_counts)[0]
            print(f"Prediction (image): {prediction}")
            if prediction == 1:
                messages.error(request, 'Image cannot be sent due to violated content in the text')
                return JsonResponse({
                    'status': 'error',
                    'message': 'Image cannot be sent due to violated content in the text'
                }, status=400)

        # If everything is ok, return success.
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'invalid request'}, status=400)