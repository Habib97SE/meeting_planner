from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_rooms, name='show_rooms'),
    path('new/', views.new_room, name='new_room'),
    path('edit/', views.edit_room, name='edit_room'),
    path('delete/<int:id>', views.delete_room, name='delete_room'),
]


