from django.shortcuts import render
from .models import Projects


def home(request):
    form = Projects.objects.all().order_by('-title')[:5]
    return render(request, 'personal_portfolio/home.html', {'form':form})

def projects(request):
    form = Projects.objects.all()
    return render(request, 'personal_portfolio/projects.html', {'form':form})

def about(reqeust):
    return render(reqeust, 'personal_portfolio/about.html')