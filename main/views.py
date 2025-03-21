from django.urls import path

from .views import *
urlpatterns = [
    path('', set_value_in_cookie),
    path('get/', get_value_from_cookie),
    path('update/', update_value_in_cookie),
    path('delete/', delete),
]