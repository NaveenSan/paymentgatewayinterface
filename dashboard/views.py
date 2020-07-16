from django.shortcuts import render


def front_page(request):
    #front page has only either login or signup
    return render(request,'dashboard/front_page.html')
# Create your views here.
