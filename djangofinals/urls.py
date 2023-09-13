"""
URL configuration for djangofinals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emro_boarding_house import views ##change . to emro_boarding_house

urlpatterns = [
    ##home
    path('', views.main, name='main'),
    ##boarders
    path('emro_boarding_house/', views.emro_boarding_house, name='emro_boarding_house'),
    path('emro_boarding_house/details/<int:id>',views.details, name='details'),
    ##roomt
    path('emro_boarding_house/roomt', views.roomt, name='roomt'),
    ##maintenance
    path('emro_boarding_house/roomt/maintenance/<int:id>', views.maintenance, name='maintenance'),
    ##bills
    path('emro_boarding_house/bills', views.bills, name='bills'),
    path('emro_boarding_house/bills/<int:id>', views.bills_details, name='bills_details'),


    ##admin
    path('admin/', admin.site.urls),

    
]
