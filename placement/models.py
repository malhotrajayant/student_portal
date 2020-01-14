from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	name = models.CharField(max_length = 256)  
	
	def __str__(self):
		return self.name

class Offer(models.Model):
	OFFER_CHOICES = [
   		('I', 'Internship'),
	    ('F', 'Full Time'),
	    ('IF', 'Internship with Full Time' )
	]
	company = models.ForeignKey(Company , on_delete=models.CASCADE)
	o_type = models.CharField(max_length=2 , choices = OFFER_CHOICES)
	cgpa_cut = models.DecimalField(max_digits = 4, decimal_places = 2)
	job_location = models.CharField(max_length = 256)
	active = models.BooleanField(default = True)

	def get_o_type(self):
		for i in self.OFFER_CHOICES:
			if(i[0]==self.o_type):
				return i[1]

	def __str__(self):
		return self.company.name

class Lab(models.Model):
	name = models.CharField(max_length = 256)
	description = models.CharField(max_length = 256)
	capacity = models.IntegerField()
	active = models.BooleanField(default = True)

class Application(models.Model):
	STATUS_CHOICES = [
   		('N', 'Pending'),
	    ('A', 'Accepted'),
	    ('R', 'Rejected' )
	]
	offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
	student = models.ForeignKey(User, on_delete=models.CASCADE) #import 
	status = models.CharField(max_length = 1, default = 'N', choices = STATUS_CHOICES)

	def get_status(self):
		for i in self.STATUS_CHOICES:
			if(i[0]==self.status):
				return i[1]

	def __str__(self):
		return self.student.first_name +" - "+ self.offer.company.name

class SeatingPlan(models.Model):
	offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
	applicantion = models.ForeignKey(Application, on_delete=models.CASCADE)
	lab = models.ForeignKey(Lab, on_delete=models.CASCADE)