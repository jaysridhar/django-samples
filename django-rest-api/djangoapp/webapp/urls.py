from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index),
    path('self', views.self_view),
]
