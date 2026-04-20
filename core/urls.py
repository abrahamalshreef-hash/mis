
from django.contrib import admin
from django.urls import path, include # أضف include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')), # أضف هذا السطر
path('accounts/', include('django.contrib.auth.urls')),
]