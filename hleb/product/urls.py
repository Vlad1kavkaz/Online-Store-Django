from django.urls import path
from . import views


urlpatterns = [
    path('hleb', views.hleb, name='hleb'),
    path('bluda-na-mangale', views.mangal, name='mangal'),
    path('torti-i-pirozhnie', views.cake, name='cake'),
    path('pirogi-myasnie', views.meat, name='meat'),
    path('pirogi-s-ovoshnoy-nachinkoy', views.vegetable, name='vegetable'),
    path('zapekanie-myasa', views.meatin, name='meatin'),
    path('zapekanie-ptitsi', views.bird, name='bird'),
    path('zapekanie-ribi', views.fish, name='fish'),
    path('zharkoe-s-ovoshami', views.pot, name='pot'),
    path('salati', views.salad, name='salad'),
    path('rogaliki-bulki-i-pechenie', views.croissant, name='croissant'),
    path('izdeliya-s-makovoy-nachinkoy', views.poppy, name='poppy'),
    path('blini', views.hotcakes, name='hotcakes'),
    path('pelmeni-i-vareniki', views.dumplings, name='dumplings'),
    path('tvorog', views.milk, name='milk'),
    path('med', views.honey, name='honey'),
    path('goryachie-napitki', views.hotdrink, name='hotdrinks'),
]

