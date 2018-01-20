from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse
from .forms import RegistrationForm,EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:home'))
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    args={'form':form}
    return render(request, 'accounts/reg_form.html', args)

def profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    args={'user':user}
    return render(request,'accounts/profile.html',args)

def profile_edit(request):
    if request.method == 'POST':
        form= EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile'))
        else:
            print(form.errors)
    else:
        form=EditProfileForm(instance=request.user)

    args={'form':form}
    return render(request,'accounts/edit_profile.html',args)

def change_password(request):
    if request.method == 'POST':
        form= PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)     #for user to remain logged in
            return redirect(reverse('accounts:profile'))
        else:
            print(form.errors)
    else:
        form=PasswordChangeForm(user=request.user)

    args={'form':form}
    return render(request,'accounts/change-password.html',args)
