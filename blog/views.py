from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

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
def user_blogs(request,username):
    
    context={
        'blogs':Post.objects.filter(author__username=username).order_by('-date_posted'),
        'posted_by':username
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



''' 
APIs 
'''
@api_view(['GET'])
def api_home(request):
    blogs=Post.objects.all()
    serializer=PostSerializer(blogs,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_blog(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)  
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_update_blog(request, pk):
    try:
        post = Post.objects.get(pk=pk, author=request.user) 
    except Post.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = PostSerializer(post, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_blog(request,pk):
    try:
        blog=Post.objects.get(pk=pk,author=request.user)
    except Post.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
        
    serializer=PostSerializer(blog)
    blog.delete()
    return Response(serializer.data)
        