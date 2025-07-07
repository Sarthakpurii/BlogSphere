from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="blog-home"),
    path('about/',views.about,name="blog-about"),
    path('create/',views.create_blog,name="create-blog"),
    path('update/<int:id>/',views.create_blog,name="update-blog"),
    path('<int:id>/',views.read_blog,name="read-blog"),
    path('<int:id>/delete/',views.delete_blog,name="delete-blog"),
]
