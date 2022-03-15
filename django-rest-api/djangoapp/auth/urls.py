from django.urls import path
from auth import views

urlpatterns = [
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('token/', views.get_auth_token),
]
