from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import *
from mainapp.models import *


def suggested_friends_context(request):
    try:
        user_id = request.session.get('user_id_after_login')
        # print(f"User ID from session: {user_id}")
        
        user = get_object_or_404(User, id=user_id)
        # print(f"Logged-in user: {user}")
        
        user_interests = user.interests.all()
        # print(f"User interests: {[interest.name for interest in user_interests]}")

        suggested_friends = User.objects.filter(
            interests__in=user_interests
        ).exclude(id=user.id).distinct()
        # print(f"Suggested friends after interest filter: {[friend.full_name for friend in suggested_friends]}")

        suggested_friends = suggested_friends.filter(address=user.address)
        # print(f"Suggested friends after address filter: {[friend.full_name for friend in suggested_friends]}")

        return {
            'suggested_friends': suggested_friends,
        }
    except User.DoesNotExist:
        # print("User does not exist.")
        return {
            'suggested_friends': None,
        }
    except Exception as e:
        # print(f"Error in suggested_friends_context: {e}")
        return {
            'suggested_friends': None,
        }