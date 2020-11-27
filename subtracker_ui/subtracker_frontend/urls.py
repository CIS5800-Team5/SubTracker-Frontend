from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('frontend.urls')),
    path('user-auth/', admin.site.urls),
    path('auth/', include('microsoft_auth.urls', namespace='microsoft')),
]
