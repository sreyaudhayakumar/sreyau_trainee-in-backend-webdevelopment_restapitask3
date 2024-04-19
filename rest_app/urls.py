
from django.urls import path
from .views import *

urlpatterns = [
    path('users/create/', CreateUserAPIView.as_view(), name='create-user'),
    path('users/<int:pk>/', RetrieveUserAPIView.as_view(), name='retrieve-user'),
    path('users/', CreateRetrieveUserAPI.as_view(), name='create-retrieve-user'),
    path('users/<int:pk>/update/', UpdateUserAPIView.as_view(), name='update-user'),
    path('users/<int:pk>/delete/', DeleteUserAPIView.as_view(), name='delete-user'),
    path('users/bulk-delete/', BulkDeleteUserAPIView.as_view(), name='bulk-delete-users'),
]
