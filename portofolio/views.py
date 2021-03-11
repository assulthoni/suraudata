from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : "Portofolio",
        'brand' : "Portofolio"
    }
    return render(request, 'index.html', context=context)