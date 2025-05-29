from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),

    # Log in Log out urls

    path('my-login', views.my_login, name='my-login'),

    # Log in Log out urls

    path('user-logout', views.user_logout, name='user-logout'),

     # Dashboard / profile urls

    path('dashboard', views.dashboard, name='dashboard'),

    path('profile-management', views.profile_management, name='profile-management'),

    path('delete-account', views.delete_account, name='delete-account'),


   
]
