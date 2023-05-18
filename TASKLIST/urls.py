from django.urls import path
from TASKLIST import views
urlpatterns = [
    path('', views.index, name = 'list'),
    path('UPDATE/<str:pk>/', views.update_task, name = 'update_task'),
    path('DELETE/<str:pk>/', views.delete_task, name = 'delete_task'),
]