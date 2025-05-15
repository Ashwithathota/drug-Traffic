from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import *
from mainapp.models import *


def friends_context(request):
    try:
        user_id = request.session.get('user_id_after_login')
        user = get_object_or_404(User, id=user_id)
        
        print(f"Current user: {user}")

        # Get friend requests that are accepted
        friend_requests = FriendRequest.objects.filter(
            (Q(from_user=user) | Q(to_user=user)) & Q(is_accepted=True)
        )
        
        print(f"Friend requests found: {friend_requests.count()}")

        friends = []
        for request in friend_requests:
            if request.from_user == user:
                friends.append(request.to_user)
            else:
                friends.append(request.from_user)
        
        print(f"Friends list: {friends}")

        friends_count = len(friends)
        print(f"Number of friends: {friends_count}")

        # Count friend requests that are not accepted
        pending_requests_count = FriendRequest.objects.filter(
            to_user=user, is_accepted=False
        ).count()
        
        print(f"Pending friend requests: {pending_requests_count}")

        # Count unread messages for the current user
        unread_messages_count = Message.objects.filter(to_user=user, read='pending').count()
        print(f"Unread messages count: {unread_messages_count}")

        total_notification = pending_requests_count + unread_messages_count
 
        return {
            'friends': friends,
            'friends_count': friends_count,
            'pending_requests_count': pending_requests_count,
            'unread_messages_count': unread_messages_count,
            'total_notification':total_notification,
        }

    except Exception as e:
        print(f"Error in friends_context: {e}")
        return {
            'friends': None,
            'friends_count': None,
            'pending_requests_count': None,
            'unread_messages_count': None,
            'total_notification':None,

        }