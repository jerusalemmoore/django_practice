from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('',views.landing, name='landing'),
    path('logout', views.logoutView, name='logoutView'),
    path('mainfeed', views.mainFeed, name='mainFeed'),
    path('registration', views.registration, name='registration'),
    path('home/<int:id>', views.home,name='home'),
    path('home/unfollow/<int:id>', views.unfollow,name='unfollow'),
    path('home/follow/<int:id>', views.follow, name="follow"),
] 
