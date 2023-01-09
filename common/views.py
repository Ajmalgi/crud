from django.shortcuts import render
from . models import Customer
from . models import Seller
from random import randint
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def common_index(request):
    return render(request, 'common_templates/index.html')


def cart(request):
    return render(request, 'common_templates/cart.html')


def checkout(request):
    return render(request, 'common_templates/checkout.html')


def customer_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        new_customer = Customer(name=username, email=email, password=password)
        new_customer.save()  # inserting in to table as row

    return render(request, 'common_templates/customer_reg.html')


def customer_login(request):
    return render(request, 'common_templates/customer_login.html')


def seller_login(request):
    return render(request, 'common_templates/seller_login.html')


def seller_reg(request):
    msg = ''
    if request.method == 'POST':

            seller_name = request.POST['seller_name']
            email = request.POST['email']
            phone = request.POST['phone']
            account = request.POST['account']
            ifsc = request.POST['ifsc']
            seller_pic = request.FILES['seller_pic']
            address = request.POST['address']
            user_name= randint(1111, 9999)
            pwd = 'sell-'+str(user_name)+'-'+phone[6:10]

            newseller = Seller(name=seller_name, email=email, phone=phone, account=account,ifsc=ifsc,
             seller_pic=seller_pic, address=address, user_name=user_name,password=pwd)
            newseller.save()
            msg = 'created successfully'
            email_subject='account user name and password'
            email_content='user name :'+str(user_name) + 'password' + pwd

            send_mail(
                email_subject,
                email_content,
                settings.EMAIL_HOST_USER,
                [email,]
            )
    return render(request, 'common_templates/seller_reg.html',{'message':msg})

    
