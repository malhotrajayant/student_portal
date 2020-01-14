from django.contrib import admin

# Register your models here.
import placement.models as m

admin.site.register(m.Company)
admin.site.register(m.Offer)
admin.site.register(m.Lab)
admin.site.register(m.Application)
admin.site.register(m.SeatingPlan)