from django.urls import path
from . import views

app_name = 'thetest'

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('<slug:slug>', views.single_test, name='thetest')
]
