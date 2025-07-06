from django.urls import path
from . import views

urlpatterns = [
    path('delete-profile-image/', views.delete_profile_image, name='delete-profile-image'),
]
