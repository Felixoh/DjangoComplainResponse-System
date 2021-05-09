from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	#user Authenticatin and validation urls
	path('register/',views.register,name='register'),
	path('login/',views.user_login,name='login'),
	path('logout/',views.user_logout,name="logout"),
	#specific user details
	path('user/',views.user,name='user'),
	path('complain/<str:id>',views.complain_form,name="complain_form"),
	path('complains/<str:id>',views.delete_complain,name="delete"),
	#URLs related to output processing and assistance.
	path('exportToPdf/<str:id>',views.print_to_pdf,name="printToPdf"),
	path('help',views.help_page,name='help'),
]