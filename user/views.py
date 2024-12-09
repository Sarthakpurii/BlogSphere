from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Congrats! Account has been created for {username}.")
            return redirect('blog-home')
    else:
        form=UserRegistrationForm()
    return render(request,template_name='user/register.html',context={'form':form})

