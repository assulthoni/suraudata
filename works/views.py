from django.shortcuts import render
from .models import Posts
# Create your views here.
def index(request):
    queryset = Posts.objects.all()
    context ={
        'posts' : queryset,
        
    }
    return render(request, 'work.html', context=context)
