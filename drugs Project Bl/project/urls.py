"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


from adminapp import views as admin_views
from userapp import views as user_views
from mainapp import views as main_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',main_views.index,name="index"),
    path('about/',main_views.about,name="about"),
    path('admin-login',main_views.admin_login,name="admin_login"),
    path('user/login/',main_views.user_login,name="user_login"),
    path('user/register/',main_views.user_register,name="user_register"),
    path("user/otp/",main_views.user_otp,name="user_otp"),
    path('contact',main_views.contact,name="contact"),



    path('user-dashboard',user_views.user_dashboard,name="user_dashboard"),
    path('user/logout/',user_views.user_logout,name="user_logout"),
    path('send-message/', user_views.send_message, name='send_message'),
    path('user/main-page/',user_views.main_page,name="main_page"),
    path('user/whatsapp/dashboard/',user_views.whatsapp,name="whatsapp"),
    path('whatsapp/logout/', user_views.whatsapp_logout, name='whatsapp_logout'),
    path('user/telegram/dashboard/',user_views.telegram,name="telegram"),
    path('user/myposts/',user_views.my_posts,name="my_posts"),
    path('user/profile/',user_views.user_profile,name="user_profile"),
    path('user/friend/request',user_views.fr_req,name="fr_req"),
    path('user/friend/responses',user_views.res,name="res"),
    path('user/messages/',user_views.user_messages,name="user_messages"),
    path('post-comment/<int:post_id>/', user_views.post_comment, name='post_comment'),
    path('viewing-profile/<int:post_id>/', user_views.post_comment2, name='post_comment2'),
    path('like-post/<int:post_id>/', user_views.like_post, name='like_post'),
    path('like-post-in-profile/<int:post_id>/', user_views.like_post2, name='like_post2'),
    path('send-friend-request/<int:recipient_id>/', user_views.send_friend_request, name='send_friend_request'),
    path('view/profile/<int:user_id>/', user_views.visit_profile, name='visit_profile'),
    path('accept-friend-request/<int:user_details_id>/', user_views.accept_friend_request, name='accept_friend_request'),
    path('reject-friend-request/<int:user_details_id>/', user_views.reject_friend_request, name='reject_friend_request'),
    path('mark-as-read/<int:message_id>/', user_views.mark_as_read, name='mark_as_read'),




    
    path('admin-dashboard/', admin_views.index, name='admin_dashboard'),
    path('post/remove/<int:post_id>/', admin_views.remove_post, name='remove_post'),
    path('hate/users/', admin_views.users_hate, name='users_hate'),
    path('user/change-status/<int:user_id>/', admin_views.change_status, name='change_status'),
    path('all-users/', admin_views.all_users, name='all_users'),
    path('block-ethereum/<int:user_id>/', admin_views.block_ethereum, name='block_ethereum'),
    path('upload-dataset/', admin_views.upload_dataset, name='upload_dataset'),
    path('view-dataset/', admin_views.view_dataset, name='view_dataset'),
    path('Train-Test-model/', admin_views.trainTestmodel, name='trainTestmodel'),
    path('latest-posts/', admin_views.latest_posts, name='latest_posts'),
    path('blockchain-details/<int:user_id>/', admin_views.admin_blockchain_details, name='admin_blockchain_details'),
    path('RF-model/', admin_views.rf, name='rf'),
    path('BI-model/', admin_views.bi, name='bi'),
    path('Nb-model/', admin_views.nb, name='nb'),
    path('DT-model/', admin_views.dt, name='dt'),
    path('LR-model/', admin_views.lr, name='lr'),
    path('AB-model/', admin_views.ab, name='ab'),
    path('XGB-model/', admin_views.xb, name='xb'),
    path('Graph-analysis/', admin_views.graph, name='graph'),
    path('pending-users/', admin_views.pending_users, name='pending_users'),
    path('accept-user/<int:user_id>/', admin_views.accept_user, name='accept_user'),
    path('reject-user/<int:user_id>/', admin_views.reject_user, name='reject_user'),
    path('delete-user/<int:user_id>/', admin_views.delete_user, name='delete_user'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)