from django.shortcuts import render

# Create your views here.

def customer_home(request):
    return render(request,'customer_templates/customer_home.html')

def cus_profile(request):
    return render(request,'customer_templates/cus_profile.html')
