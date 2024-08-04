from django.shortcuts import render
from .models import Users

# Create your views here.
def all_users(request):
    all_users = Users.objects.all().order_by('name')
    return render(request, 'users/users_list.html', {
        'all_users': all_users
    })
    
def single_user(request,name):
    user = Users.objects.get(name=name)
    return render(request, 'users/single_user.html',{
        'single_user':user
    })