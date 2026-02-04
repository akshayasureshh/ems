from django.contrib import admin
from django.urls import path
from .views import CreateUserView, LoginView, LogoutView, RefreshTokenView


urlpatterns = [
 
    path('create_user/', CreateUserView.as_view(), name='create-user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]
















