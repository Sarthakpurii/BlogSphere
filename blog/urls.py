from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="blog-home"),
    path('about/',views.about,name="blog-about"),
    path('create/',views.create_blog,name="create-blog"),
    path('update/<int:id>/',views.create_blog,name="update-blog"),
    path('<int:id>/',views.read_blog,name="read-blog"),
    path('<int:id>/delete/',views.delete_blog,name="delete-blog"),
    path('<str:username>/',views.user_blogs,name="user-blogs"),
    
    #APIs
    path('api/blogs/',views.api_home),
    path('api/create/',views.api_create_blog),
    path('api/update/<int:pk>/',views.api_update_blog),
    path('api/delete/<int:pk>/',views.api_delete_blog),
]
