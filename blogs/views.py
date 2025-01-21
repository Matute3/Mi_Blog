from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blogs/home.html')

def blog_list(request):
    return render(request, 'blogs/blog_list.html')

def blog_detail(request, blog_id):
    return render(request, 'blogs/blog_detail.html', {'blog_id': blog_id})

def blog_create(request):
    return render(request, 'blogs/blog_create.html')

def blog_edit(request, blog_id):
    return render(request, 'blogs/blog_edit.html', {'blog_id': blog_id})

def blog_delete(request, blog_id):
    return HttpResponse(f"Eliminar el blog {blog_id}")
