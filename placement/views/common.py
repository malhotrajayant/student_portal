from django.http import HttpResponse
from django.shortcuts import render,redirect
from ..models import Offer , Application
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
	
	if(request.method == 'POST'):

		o = Offer.objects.get(pk=request.POST.get("ofr"))
		if(request.user.profile.current_cgpa < o.cgpa_cut):
			messages.error(request, f'CGPA criterion not Fulfilled')
			return redirect("/")

		cur = Application.objects.filter(student = request.user , offer = o)
		if not len(cur) :
			applicant = Application()
			applicant.offer = o
			applicant.student = request.user
			applicant.save()
			messages.success(request, f'Application Sent - Check Status for more info !')

		else:
			messages.success(request, f'Application already Sent - Check Status for more info !')
		
		return redirect("/")

	else:
		
		return render(request,'placement/home.html' , {'offer' : Offer.objects.all()})


def status(request):
		a = Application.objects.filter(student = request.user)
		return render(request,'placement/status.html', {'applications' : a })