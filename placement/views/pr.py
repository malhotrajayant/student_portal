from django.shortcuts import render, redirect
from django.contrib import messages
from placement import forms
from placement.models import Offer, Company, Lab, Application
from placement.forms import OfferForm, CompanyForm, LabForm, ShortlistForm

def offer(request):
    if(request.user.is_superuser or request.user.profile.u_type == 'PR'):
        if request.method=='POST':
            o_form = OfferForm(request.POST)
            if(o_form.is_valid()):
                o_form.save()
                return redirect('/offer')
            else:
                offer_list = Offer.objects.all()
                return render(request, 'placement/manage-offer.html', {'o_form': o_form, 'offer_list': offer_list})
        else: 
            offer_list = Offer.objects.all()
            o_form = OfferForm()
            return render(request, 'placement/manage-offer.html', {'o_form': o_form, 'offer_list': offer_list})
        return redirect('/')
    else:
        messages.error(request, "Access denied!")
        return redirect('/')

def company(request):
    if(request.user.is_superuser or request.user.profile.u_type == 'PR'):
        if request.method=='POST':
            c_form = CompanyForm(request.POST)
            if(c_form.is_valid()):
                c_form.save()
                return redirect('/company')
            else:
                companies = Company.objects.all()
                return render(request, 'placement/manage-company.html', {'c_form': c_form, 'company_list': companies})
        else: 
            companies = Company.objects.all()
            c_form = CompanyForm()
            return render(request, 'placement/manage-company.html', {'c_form': c_form, 'company_list': companies})
        return redirect('/')
    else:
        messages.error(request, "Access denied!")
        return redirect('/')

def lab(request):
    if(request.user.is_superuser or request.user.profile.u_type == 'PR'):
        if request.method=='POST':
            l_form = LabForm(request.POST)
            if(l_form.is_valid()):
                l_form.save()
                return redirect('/lab')
            else:
                labs = Lab.objects.all()
                return render(request, 'placement/manage-lab.html', {'l_form': l_form, 'lab_list': labs})
        else: 
            labs = Lab.objects.all()
            l_form = LabForm()
            return render(request, 'placement/manage-lab.html', {'l_form': l_form, 'lab_list': labs})
        return redirect('/')
    else:
        messages.error(request, "Access denied!")
        return redirect('/')

def shortlist(request):
    if(request.user.is_superuser or request.user.profile.u_type == 'PR'):
        if request.method=='POST':
            s_form = ShortlistForm(request.POST)
            if(s_form.is_valid()):
                selected_applications = Application.objects.filter(offer=s_form.cleaned_data['offer']).order_by('-student__profile__current_cgpa')[:s_form.cleaned_data['count']]
                Application.objects.filter(pk__in = selected_applications).update(status = 'A')
                Application.objects.exclude(pk__in = selected_applications).update(status = 'R')
                return redirect('/shortlist')
            else:
                return render(request, 'placement/shortlist.html', {'s_form': s_form})
        else: 
            s_form = ShortlistForm()
            return render(request, 'placement/shortlist.html', {'s_form': s_form})
        return redirect('/')
    else:
        messages.error(request, "Access denied!")
        return redirect('/')