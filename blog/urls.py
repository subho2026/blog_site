from . import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
