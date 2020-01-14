from django.urls import path
from .views import admin as admin_views, pr as pr_views, student as student_views, common as common_views

urlpatterns = [
    path('', common_views.home, name='main-home'),
    path('pr/', admin_views.PR_list,name='manage_pr'),
    path('offer/', pr_views.offer,name='manage_offer'),
    path('company/', pr_views.company,name='manage_company'),
    path('lab/', pr_views.lab,name='manage_lab'),
    path('status/', common_views.status , name='status'),
    path('shortlist/', pr_views.shortlist , name='shortlist'),
]