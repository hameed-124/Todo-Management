from django.urls import path
from . import views
urlpatterns = [
    path('',views.show, name='show'),
    path('add', views.add, name='add'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('edit/<int:task_id>/', views.edit, name='edit')
]