from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    # decending order with "-" before "date"
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts':posts })