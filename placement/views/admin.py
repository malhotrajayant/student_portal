from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from placement import forms

def PR_list(request):
    if(request.user.is_superuser):
        pr_list = User.objects.filter(profile__u_type='PR')
        if(request.method == 'POST'):
            pr_form = forms.ManagePRForm(request.POST)
            if(pr_form.is_valid()):
                op = pr_form.cleaned_data.get('operation')
                user = User.objects.filter(username = pr_form.cleaned_data.get('username'))
                if(len(user)):
                    user = User.objects.get(username = pr_form.cleaned_data.get('username'))
                    u_type = user.profile.u_type
                    if(u_type == 'S'):
                        if(op == 'R'):
                            messages.error(request, "Given member is not PR.")
                        if(op == 'A'):
                            user.profile.u_type = 'PR'
                            user.profile.save()
                            messages.success(request, "Success!")
                    elif(u_type == 'PR'):
                        if(op == 'R'):
                            user.profile.u_type = 'S'
                            user.profile.save()
                            messages.success(request, "Success!")
                        if(op == 'A'):
                            messages.error(request, "Given member is already a PR.")
                    else:
                        messages.error(request, "Something went wrong!")
                else:
                    messages.error(request, "User not found!")
                return redirect('/pr')
            else:
                return render(request, 'admin/pr.html', {'pr_form': pr_form, 'pr_list': pr_list})
        else:
            pr_form = forms.ManagePRForm()
            return render(request, 'admin/pr.html', {'pr_form': pr_form, 'pr_list': pr_list})
    else:
        messages.error(request, "Access denied!")
        return redirect('/')