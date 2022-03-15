from django.urls import path
from webapp import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index),
    path('self', csrf_exempt(views.SelfView.as_view())),
    path('selffn', views.self_view),
]
