from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.all_users, name='users_list'),
    path('signup/',views.sign_up, name='sign_up'),
    path('<str:name>/', views.single_user, name='single_user'),
]
