from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from Payment_Gateway_Interface import settings
import time

def user_login(request):
    form = Login(request.POST)
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        auth.logout(request)
        if user is not None:
            auth.login(request, user)
            return redirect('login:home')
        if user is None:
            return redirect('login:user_login')
    return render(request,'login/login_page.html',{'form':form})


def logout(request):
    auth.logout(request)
    return render(request,'login/logout.html')

@login_required
@csrf_exempt
def home_page(request):
    return render(request,'login/home.html')

@login_required
def process_payment(request):
    host = request.get_host()
    order = str('donate')
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount' : '50',
        'item_name': 'donation',
        'invoice': 'Happy to hear -HELP!!!',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('login:payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('login:payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'ecommerce/process_payment.html', {'order': order, 'form': form})


@csrf_exempt
@login_required
def payment_done(request):
    time.sleep(10)
    reverse('login:home')
    return render(request, 'ecommerce/payment_done.html')


@login_required
@csrf_exempt
def payment_canceled(request):
    return render(request, 'ecommerce/payment_cancelled.html')