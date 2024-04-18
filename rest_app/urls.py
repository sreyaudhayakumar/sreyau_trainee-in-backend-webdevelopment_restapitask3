
from django.urls import path
from .views import CreateUserAPIView, RetrieveUserAPIView, CreateRetrieveUserAPI

urlpatterns = [
    path('users/create/', CreateUserAPIView.as_view(), name='create-user'),
    path('users/<int:pk>/', RetrieveUserAPIView.as_view(), name='retrieve-user'),
    path('users/', CreateRetrieveUserAPI.as_view(), name='create-retrieve-user'),
]
