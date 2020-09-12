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
from .views import AlbumLV, AlbumDV, PhotoDV
from .views import AlbumPhotoCV, AlbumChangeLV, AlbumPhotoUV, AlbumDeleteView
from .views import PhotoCreateView, PhotoChangeLV, PhotoUpdateView, PhotoDeleteView

app_name = 'photoApp'

urlpatterns = [
    path('', AlbumLV.as_view(), name='index'),
    path('album/', AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>/', AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:pk>/', PhotoDV.as_view(), name='photo_detail'),

    path('album/add/', AlbumPhotoCV.as_view(), name='album_add'),
    path('album/change/', AlbumChangeLV.as_view(), name='album_change'),
    path('album/<int:pk>/update/', AlbumPhotoUV.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/change/', PhotoChangeLV.as_view(), name='photo_change'),
    path('photo/<int:pk>/update/', PhotoUpdateView().as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView().as_view(), name='photo_delete'),
]
