from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="blog-home"),
    path('about/',views.about,name="blog-about"),
    path('create/',views.create_blog,name="create-blog"),
    path('<int:id>/',views.read_blog,name="read-blog"),
]
