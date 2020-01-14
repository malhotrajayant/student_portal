from django.contrib import admin

# Register your models here.
import users.models as m

admin.site.register(m.BranchYear)
admin.site.register(m.Profile)