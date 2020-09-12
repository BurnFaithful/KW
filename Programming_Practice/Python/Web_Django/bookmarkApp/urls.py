"""Web_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from bookmarkApp.views import *

app_name = 'bookmarkApp'

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),

    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('change/', BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name='delete'),
]
