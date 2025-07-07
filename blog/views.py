from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404


# posts=[
#     {
#         'author':"Sarthak",
#         'title':"Blog Post 1",
#         'content':"First post content",
#         'date_posted':"November 27, 2024"
#     },
#     {
#         'author':"Manan",
#         'title':"Blog Post 2",
#         'content':"Second post content",
#         'date_posted':"November 27, 2024"
#     }
# ]
def home(request):
    
    context={
        'blogs':Post.objects.order_by('-date_posted')
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def create_blog(request,id=None):
    if request.method=='POST':
        if id:
            form = PostForm(request.POST, instance=get_object_or_404(Post, id=id))
            print(f"Updating instance with id={id}")
        else:
            form = PostForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            print(f"Updating blog with id={blog.id}")
            blog.author=request.user
            blog.save()
            print(f"Updated blog with id={blog.id}")
            messages.success(request,f"Your blog has been published.")
            return redirect('blog-home')
        else:
            messages.error(request,f"Please correct the errors below.")
    else:
        if id:
            form=PostForm(instance=get_object_or_404(Post, id=id))
            print(f"Updating instance with id={id}")
        else:
            form=PostForm()
    return render(request,'blog/create_blog.html',{'form':form})

def read_blog(request,id):
    context={
        'blog':get_object_or_404(Post, id=id)
    }
    return render(request,'blog/read_blog.html',context)

def delete_blog(request,id):
    blog=get_object_or_404(Post, id=id)
    if request.method=="POST" and blog.author==request.user:
        blog.delete()
        messages.success(request,f"Your blog has been deleted.")
        return redirect('blog-home')
    return HttpResponseForbidden()