from django.shortcuts import render

# Create your views here.

def seller_home(request):
    return render(request,'seller_templates/seller_home.html')