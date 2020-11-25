from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('profile/', views.profile, name='profile'),
    ]
