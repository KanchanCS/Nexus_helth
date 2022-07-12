from django.urls import path
from . import views
 
urlpatterns = [  
     
      path('base/', views.base, name='base'),
     path('', views.home, name='home'),
     path('about', views.about, name='about'),
     path('info', views.info, name='contact'),
     path('404', views.error404, name='404'),
     path('blog', views.Blog, name='blog'),
     path('blog_single', views.blog_single, name='blog_single'),
     path('career', views.career, name='career'),
     path('careers', views.careers, name='careers'),
     path('lowerbackpain', views.lowerbackpain, name='lowerbackpain'),
     path('occupational_health', views.occupational_health, name='occupational_health'),
     path('partners', views.partners, name='partners'),
     path('patientinformation', views.patientinformation, name='patientinformation'),
     path('resources', views.resources, name='resources'),
     path('service_single', views.service_single, name='service_single'),
     path('working_with_nhs', views.working_with_nhs, name='working_with_nhs'),
     path('appointmentbook', views.appointment, name='appointment'),
     path('user', views.customer, name='feedback'),
#      path('book', views.appointment, name = 'appointment')

 

 
]
