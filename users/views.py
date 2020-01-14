from django.shortcuts import render , redirect
from .forms import UserRegisterForm , ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if(request.method == 'POST'):
        u_form = UserRegisterForm(request.POST) #User Form
        p_form = ProfileForm(request.POST) #Extended Form
        if(u_form.is_valid() and p_form.is_valid() ):
            email = u_form.cleaned_data.get('email')
            if(email.find('@thapar.edu')==-1):
                messages.error(request, "You must use thapar.edu email.")
                return render(request,'users/register.html',{'u_form' : u_form,'p_form' : p_form} )
            user = u_form.save()
            profile = p_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, f'Your account had been created! Log in...')
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileForm()

    return render(request,'users/register.html',{'u_form' : u_form,'p_form' : p_form} )

@login_required
def profile(request):
    if(request.user.is_authenticated):
        if request.method=='POST':
            profile = request.user.profile
            p_form = ProfileForm(request.POST, instance = profile)
            if(p_form.is_valid()):
                p_form.save()
                return redirect('/profile')
            else:
                return render(request, 'users/profile.html', {'p_form': p_form})
        else: 
            profile = request.user.profile
            p_form = ProfileForm(instance = profile)
            return render(request, 'users/profile.html', {'p_form': p_form})
    else:
        messages.error(request, "You must be logged in!")
        return request.redirect('/')