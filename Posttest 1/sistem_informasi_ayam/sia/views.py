from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def katalog(request):
    return render(request, 'homepage/katalog.html')