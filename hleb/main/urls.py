from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('search/', views.Search.as_view(), name='search')

]
