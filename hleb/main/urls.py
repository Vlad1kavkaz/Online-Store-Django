from django.urls import path
from . import views

app_name = ''

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('search/', views.Search.as_view(), name='search'),
]
