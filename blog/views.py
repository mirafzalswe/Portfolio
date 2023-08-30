from django.shortcuts import render, redirect, get_object_or_404
from .models import Model
from .forms import AddBlock

def blog(request):
    form = Model.objects.all()
    return render(request, 'blog/blog.html', {'form':form })

def create_blog(request):
    if request.method == "POST":
        form = AddBlock(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = AddBlock()
    return render(request, 'blog/create.html', {'form': form})


def detail(request, blog_id):
    blog = get_object_or_404(Model, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


