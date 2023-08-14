from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ProfileForm
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/login/')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile': profile}
    return render(request, 'profile.html', context)

def edit_profile(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        profil = get_object_or_404(Profile, user=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            print("-----1-----")
            print(form)
            if form.is_valid():
                print("-----2----")
                image = form.cleaned_data.get('image')
                country = form.cleaned_data.get('country')
                address = form.cleaned_data.get('address')
                profil.iage=image
                profil.country=country
                profil.address=address
                profil.save()
                print("-----3-----")

                return redirect(reverse('accounts:profile', kwargs={'slug':request.user}))
        print("----no POST---------")


        form = ProfileForm(instance=profil)




        context = {'form': form}
        return render(request, 'edit_profile.html', context)
    return redirect(reverse('login'))