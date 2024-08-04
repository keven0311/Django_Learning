from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth.forms import UserCreationForm

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
    
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:users_list')
    else:
        form = UserCreationForm()
    return render(request, 'users/sign_up.html',{
        "form": form
    })