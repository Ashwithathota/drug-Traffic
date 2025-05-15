from django.shortcuts import render,redirect
from django.contrib import messages
import urllib.request
import urllib.parse
from django.contrib.auth import logout
from django.core.mail import send_mail
import os
import random
from django.conf import settings
from userapp.models import *
from mainapp.models import *


def user_logout(request):
    logout(request)
    messages.info(request, "Logout Successfully ")
    return redirect("user_login")


# Create your views here.




EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')





def generate_otp(length=4):
    otp = "".join(random.choices("0123456789", k=length))
    return otp



def index(request):
    return render(request,"main/index.html")



def about(request):
    return render(request,"main/about.html")



def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            messages.success(request, 'Login Successful')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid details !')
            return redirect('admin_login')
    return render(request,"main/admin-login.html")





def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
            if user.password != password:
                messages.error(request, "Incorrect password.")
                return redirect("user_login")
            if user.status == "Accepted":
                if user.otp_status == "Verified":
                    request.session["user_id_after_login"] = user.pk
                    messages.success(request, "Login successful!")
                    return redirect("main_page")
                else:
                    new_otp = generate_otp()
                    user.otp = new_otp
                    user.otp_status = "Not Verified"
                    user.save()
                    subject = "New OTP for Verification"
                    message = f"Your new OTP for verification is: {new_otp}"
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [user.email]
                    send_mail(
                        subject, message, from_email, recipient_list, fail_silently=False
                    )
                    messages.warning(
                        request,
                        "OTP not verified. A new OTP has been sent to your email and phone.",
                    )
                    request.session["id_for_otp_verification_user"] = user.pk
                    return redirect("user_otp")
            else:
                if user.status == "Hold":
                    messages.error(request, "Your account is temporarily on hold for posting prohibited content. Please contact the admin for more details.")
                    return redirect("user_login")
                else:
                    messages.info(request, "Your Account is Not Accepted by Admin Yet")
                    return redirect("user_login")
        except User.DoesNotExist:
            messages.error(request, "Email not registered.")
            return redirect("user_login")
    return render(request,"main/user-login.html")




def user_otp(request):
    otp_user_id = request.session.get("id_for_otp_verification_user")
    if not otp_user_id:
        messages.error(request, "No OTP session found. Please try again.")
        return redirect("user_register")
    if request.method == "POST":
        entered_otp = "".join(
            [
                request.POST["first"],
                request.POST["second"],
                request.POST["third"],
                request.POST["fourth"],
            ]
        )
        try:
            user = User.objects.get(id=otp_user_id)
        except User.DoesNotExist:
            messages.error(request, "User not found. Please try again.")
            return redirect("user_register")
        if user.otp == entered_otp:
            user.otp_status = "Verified"
            user.save()
            messages.success(request, "OTP verification successful!")
            return redirect("user_login")
        else:
            messages.error(request, "Incorrect OTP. Please try again.")
            return redirect("user_otp")
    return render(request,"main/user-otp.html")

import json
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.timezone import now
from web3 import Web3
from django.core.mail import send_mail
from django.conf import settings
import json
from web3 import Web3
from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import User, Interest, BlockchainTransaction

def user_register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        interests = request.POST.getlist('interests')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('user_register')

        # Create and save the user
        user = User(
            full_name=full_name,
            email=email,
            password=password,
            phone_number=phone_number,
            age=age,
            address=address,
            photo=photo
        )
        user.save()

        # Add interests
        for interest_name in interests:
            interest, created = Interest.objects.get_or_create(name=interest_name)
            user.interests.add(interest)

        otp = generate_otp()
        user.otp = otp
        user.save()

        # Send Email with OTP
        mail_message = f"Dear {full_name},\n\nYour OTP for registration is: {otp}\n\nBest regards,\nYour Team"
        try:
            send_mail("User Registration OTP", mail_message, settings.EMAIL_HOST_USER, [email])
            messages.success(request, "OTP sent to your email.")
        except Exception as e:
            messages.error(request, f"Email sending failed: {str(e)}")
            return redirect("user_register")

        # --- Blockchain Integration Start ---
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        if not w3.is_connected():
            messages.error(request, "Blockchain connection failed.")
            return redirect("user_register")

        try:
            # Load the contract ABI from the build folder
            with open("blockchain/build/contracts/Cannatch.json") as f:
                contract_json = json.load(f)
                contract_abi = contract_json["abi"]
        except Exception as e:
            messages.error(request, f"Error loading contract ABI: {str(e)}")
            return redirect("user_register")

        # Use your deployed contract address here
        contract_address = "0x231cB0Ce79ff94818595e1cf9636eD96F2dD0343"
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)

        # Set default account (using first Ganache account)
        account = w3.eth.accounts[0]
        w3.eth.default_account = account

        try:
            recipient_address = account  # or specify another valid address from Ganache
            tx_hash = contract.functions.executeTransaction(recipient_address, 2000000).transact()
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            tx = w3.eth.get_transaction(tx_hash)
            block = w3.eth.get_block(tx_receipt['blockNumber'])
            mined_on = datetime.fromtimestamp(block['timestamp'])

            # Save blockchain transaction details in the model
            BlockchainTransaction.objects.create(
                user=user,
                block_no=tx_receipt['blockNumber'],
                gas_used=tx_receipt['gasUsed'],
                gas_limit=tx['gas'],
                mined_on=mined_on,
                block_hash=tx_receipt['blockHash'].hex(),
                from_address=tx['from'],
                to_address=tx['to'],
                tx_hash=tx_receipt['transactionHash'].hex(),
            )
            messages.success(request, "User registered and blockchain transaction recorded.")
        except Exception as e:
            messages.error(request, f"Blockchain transaction failed: {str(e)}")
            return redirect("user_register")
        # --- Blockchain Integration End ---

        request.session["id_for_otp_verification_user"] = user.pk
        return redirect("user_otp")

    return render(request, "main/user-register.html")


def contact(request):
    return render(request,"main/contact.html")