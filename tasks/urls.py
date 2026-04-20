from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # تأكد من هذا السطر
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
# في ملف urls.py الخاص بالتطبيق
path('update-duration/<int:task_id>/', views.update_duration, name='update_duration'),
]