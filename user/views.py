from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Congrats! Account has been created for {username}. You can login now.")
            return redirect('user-login')
    else:
        form=UserRegistrationForm()
    return render(request,template_name='user/register.html',context={'form':form})

@login_required
def profile(request):
    return render(request,template_name='user/profile.html')