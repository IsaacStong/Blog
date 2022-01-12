from django.urls import path, include
from .views import UserRegistration, UserEdit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view()),
]