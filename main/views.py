from django.urls import path

from django.urls import path

from .views import *

urlpatterns = [
    path('add/', add_to_session),
    path('get/', get_to_session),
    path('delete/', delete_to_session),
    path('update/', update_to_session),
]