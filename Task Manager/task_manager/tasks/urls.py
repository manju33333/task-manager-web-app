
# urls.py
# urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
