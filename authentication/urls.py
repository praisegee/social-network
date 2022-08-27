from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name="register"),
    path('login/', views.UserLoginAPIView.as_view(), name="login"),
    path('users/', views.AuthUserListAPIView.as_view(), name="user-list"),
    path('users/<int:pk>/', views.AuthUserRetrieveAPIView.as_view(), name="user-detail"),
    path('logout/', views.UserLogoutAPIView.as_view(), name="logout"),
]

