"""
URL configuration for BlogSphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('user/',include('user.urls')),
    path('register/',userViews.register,name='user-register'),
    path('login/',authViews.LoginView.as_view(template_name='user/login.html'),name='user-login'),
    path('logout/',authViews.LogoutView.as_view(template_name='user/logout.html'),name='user-logout'),
    path('profile/',userViews.profile,name='user-profile'),
    path('api/token/', obtain_auth_token, name='api-token'),
]

if settings.DEBUG:
    urlpatterns+=(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))