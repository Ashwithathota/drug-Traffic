from django.shortcuts import get_object_or_404
from userapp.models import *
from mainapp.models import *

def latest_friend_request(request):
    try:
        user_id = request.session.get('user_id_after_login')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            latest_request = FriendRequest.objects.filter(to_user=user, is_accepted=True).order_by('-timestamp').first()
            if latest_request:
                from_user = latest_request.from_user
                return {'latest_friend_request_from_user': from_user}
        return {'latest_friend_request_from_user': None}
    except User.DoesNotExist:
        return {'latest_friend_request_from_user': None}
    except Exception as e:
        print(f"Error in latest_friend_request: {e}")
        return {'latest_friend_request_from_user': None}