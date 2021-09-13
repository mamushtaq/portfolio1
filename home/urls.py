from . import views
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name ='home'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('sendmail', views.sendmail, name='sendmail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)