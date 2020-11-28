from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oauth/', include("social_django.urls")),
#    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('profile/', views.profile, name='profile'),
#    path('user/', views.user, name='user'),
    ]
