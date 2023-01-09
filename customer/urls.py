from django.urls import path,include
from . import views

app_name = 'customer_app'


urlpatterns = [
    path('customer_home',views.customer_home,name='customer_home'),
    path('cus_profile',views.cus_profile,name='cus_profile'),

]