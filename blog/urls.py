from django.urls import path

from . import views
urlpatterns = [
    path('',views.landing, name='landing'),
    path('logout', views.logoutView, name='logoutView'),
    path('mainfeed', views.mainFeed, name='mainFeed'),
    path('registration', views.registration, name='registration'),
    path('home/<int:id>', views.home,name='home')
]
