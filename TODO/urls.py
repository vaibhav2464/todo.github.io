from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addtask, name='addtask'),
    path('register', views.register, name='register'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('update/<int:task_id>', views.update, name='update'),
    path('update/edit/<int:task_id>', views.edit, name='edit'),
]
