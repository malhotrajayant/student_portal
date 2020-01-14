from django import forms
from placement.models import Offer, Company, Lab

class ManagePRForm(forms.Form):
    OP_CHOICES = [('R', 'Remove'), ('A', 'Add')]
    username = forms.CharField(max_length = 256)
    operation = forms.ChoiceField(choices = OP_CHOICES)

class OfferForm(forms.ModelForm):

	class Meta:
		model = Offer
		exclude = ['active']

class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		exclude = []

class LabForm(forms.ModelForm):

	class Meta:
		model = Lab
		exclude = ['active']

class ShortlistForm(forms.Form):
	count = forms.DecimalField()
	offer = forms.ModelChoiceField(queryset = Offer.objects.filter(active=True))