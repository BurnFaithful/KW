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
from blogApp.views import *

app_name = 'blogApp'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('post/', PostLV.as_view(), name='post_list'),
    path('post/<str:slug>', PostDV.as_view(), name='post_detail'),

    path('archive/', PostAV.as_view(), name='post_archive'),
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/<str:month>/', PostMAV.as_view(month_format='%m'), name='post_month_archive'),
    path('<int:year>/<str:month>/<int:day>/', PostDAV.as_view(month_format='%m'), name='post_day_archive'),
    path('today/', PostTAV.as_view(), name='post_today_archive'),
    path('tag/', TagTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', PostTOL.as_view(), name='tagged_object_list'),

    path('search/', SearchFormView.as_view(), name='search'),

    path('add/', PostCreateView.as_view(), name='add'),
    path('change/', PostChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
