from django.urls import path

from .views import (
    pet_register_view,
    pet_update_view,
    pet_delete_view,
    pet_list_view,
    pet_detail_view,
)
urlpatterns = [
path('register/', pet_register_view, name='pet_register'),
path('list/', pet_list_view, name='list')
path('<int:id>/detail', pet_detail_view, name='detail'),
path('<int:id>/update/', pet_update_view, name='update'),
path('<int:id>/delete', pet_delete_view, name='delete')
]
