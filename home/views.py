

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Websites, Videos, Graphics
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def portfolio(request):
    return render(request, 'home/portfolio.html', {
        'websites':Websites.objects.all().reverse(),
        'graphics': Graphics.objects.all().reverse(),
        'videos' : Videos.objects.all().reverse() 
    })

def sendmail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        mes = f"Name: {name}\nEmail Address: {email}\n{message}"
        send_mail(
            subject,
            mes,
            settings.EMAIL_HOST_USER,
            ['mamushtaq00995@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'home/home.html')
    else:
        return render(request, 'home/home.html')
