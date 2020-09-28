from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Posts
# Create your views here.
def index(request):
    queryset = Posts.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts' : posts,

    }
    return render(request, 'work.html', context=context)

def get_article(request, id):
    queryset = Posts.objects.get(pk=id),
    context = {
        'post' : queryset
    }
    return render(request, 'work_detail.html', context=context)
