"""trydjango2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from articles.views import (articles_details_view, 
                            articles_search_view ,
                            articles_post_view)
from accounts.views import login_view, logout_view, register_view

from .views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view),
    path('articles/', articles_search_view),
    path('articles/<int:id>/', articles_details_view),
    path('articles/create/', articles_post_view),
    path('accounts/login/', login_view),
    path('accounts/logout/', logout_view),
    path('accounts/register', register_view)

]
