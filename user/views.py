from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method=='POST':
        user_instance = request.user
        uForm=UserUpdateForm(request.POST,instance=user_instance)
        pForm=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request,f"Your Profile has been Updated.")
            return redirect('user-profile')
            
    else:
        uForm=UserUpdateForm(instance=request.user)
        pForm=ProfileUpdateForm(instance=request.user.profile)
    request.user.refresh_from_db()
    print("Request Method:", request.method)
    print("User Form Data:", uForm.data if request.method == 'POST' else "N/A")
    print("Is User Form Valid?", uForm.is_valid())
    print("Errors in User Form:", uForm.errors if not uForm.is_valid() else "No Errors")
    print("Current User Username:", request.user.username)
    context={
        'uForm':uForm,
        'pForm':pForm,
        'user_data': request.user,
    }
    return render(request,template_name='user/profile.html', context=context)