from django.urls import path
from pos.views import (
    index,
    getData, update_nick_name, insert_person, delete_person
)

urlpatterns = [
    path('', index, name='index'),
    path('data/', getData, name='get-data'),
    path('update/', update_nick_name, name='update-nickname'),
    path('additional/', insert_person, name='insert-person'),
    path('deletion/', delete_person, name='delete-person'),
]