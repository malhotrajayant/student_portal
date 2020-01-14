from django.db import models
from django.contrib.auth.models import User

class BranchYear(models.Model):
	branch = models.CharField(max_length=256, null=True)
	group = models.CharField(max_length=256, null=True)
	year = models.IntegerField(null=True)

	def __str__(self):
		return self.group + ", Year-" + str(self.year)

class Profile(models.Model):
	USER_TYPES = [
		('S', 'Student'),
		('PR', 'PR'),
	]
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
	u_type = models.CharField(max_length = 2, choices = USER_TYPES, default = 'S')
	registration_no = models.CharField(max_length = 10, null=True)
	current_cgpa = models.DecimalField(max_digits = 4, decimal_places = 2)
	branch_year = models.ForeignKey(BranchYear,null=True,on_delete = models.SET_NULL)
	dob = models.DateField()
	contact_number = models.CharField(max_length=10)
	personal_email = models.CharField(max_length = 256)




