from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import redirect


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
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def create_blog(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            messages.success(request,f"Your blog has been posted.")
            return redirect('blog-home')
        else:
            messages.error(request,f"Please correct the errors below.")
    else:
        form=PostForm()
    return render(request,'blog/create_blog.html',{'form':form})