from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import CustomerFeedback
from .forms import GetAppoinment

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    banner = Banner.objects.all()
    return render(request, 'home.html', {'banner':banner})
 
def error404(request):    
    return render(request,'pages/404.html')
 
def about(request):    
    return render(request,'pages/about.html')
 
def Blog(request):    
    return render(request,'pages/blog.html')
 
def blog_single(request):    
    return render(request,'pages/blog_single.html')
 
def career(request):    
    return render(request,'pages/career.html')
 
def careers(request):    
    return render(request,'pages/careers.html')
 
def lowerbackpain(request):    
    return render(request,'pages/lowerbackpain.html')
 
def occupational_health(request):    
    return render(request,'pages/occupational_health.html')
 
def partners(request):    
    return render(request,'pages/partners.html')
 
def patientinformation(request):    
    return render(request,'pages/patientinformation.html')
 
def resources(request):    
    return render(request,'pages/resources.html')
 
def service_single(request):    
    return render(request,'pages/service_single.html')

def working_with_nhs(request):    
    return render(request,'pages/working_with_nhs.html')

def info(request): 
    return render(request,'info.html')

def appointment(request):  
    if request.method == 'POST':
        fm = GetAppoinment(request.POST)
        if fm.is_valid():
            obj = AppointmentBook() 
            obj.name = fm.cleaned_data['name']
            obj.email= fm.cleaned_data['email']
            obj.phone = fm.cleaned_data['phone']
            obj.requirements = fm.cleaned_data['requirements']
            #finally save the object in db
            obj.save()
            return HttpResponseRedirect('/')

    else:
        fm = GetAppoinment()  
        print(fm)
    return render(request,'pages/appointment.html',{'froms':fm})

def customer(request):
    if request.method == 'POST':
        fm = CustomerFeedback(request.POST)
        if fm.is_valid():
            obj = User() #gets new object
            obj.customer_name = fm.cleaned_data['customer_name']
            obj.designation = fm.cleaned_data['designation']
            obj.feedback = fm.cleaned_data['feedback']
            
            #finally save the object in db
            obj.save()
            return HttpResponseRedirect('/')


    else:
        fm = CustomerFeedback()
    return render(request, 'pages/feedback.html',{'form':fm})
           



