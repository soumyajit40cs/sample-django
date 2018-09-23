"""infyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import *
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from blog import views
from django.conf import settings
from django.urls import NoReverseMatch, reverse
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', auth_views.LoginView.as_view(),name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(),name='logout'),
    path('posts/', views.AllPostList.as_view(), name='all_posts'),
    path('posts_details/<int:pk>/', views.PostDetails.as_view(), name='post_detials'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Blog Admin"
admin.site.site_title = "Demo Blog Portal"
admin.site.index_title = "Welcome to Django POC Portal"
