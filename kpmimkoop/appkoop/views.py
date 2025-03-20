from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import BookingForm, KoopMartOrderForm
import logging

logger = logging.getLogger(__name__)

def home(request):
    context = {
        'page': 'home'  # Add context to help with template debugging
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about/index.html')

def history(request):
    return render(request, 'about/history.html')

def vision(request):
    return render(request, 'about/vision.html')

def mission(request):
    return render(request, 'about/mission.html')

def organization(request):
    return render(request, 'organization/index.html')

def org_chart(request):
    # Using the model is good if you have actual data
    # If you want to hardcode it for now, you can return an empty context
    return render(request, 'organization/chart.html')

def services(request):
    return render(request, 'services.html')

def cafe_air(request):
    return render(request, 'services/cafe_air.html')

def koop_mart(request):
    return render(request, 'services/koop_mart.html')

def koop_mart_order(request):
    if request.method == 'POST':
        form = KoopMartOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tempahan telah berjaya dihantar!')
            return redirect('koop_mart')
    else:
        form = KoopMartOrderForm()
    
    return render(request, 'services/koop_mart_order.html', {'form': form})

def kios_aok(request):
    return render(request, 'services/kios_aok.html')

def dobi(request):
    return render(request, 'services/dobi.html')

def parcel(request):
    return render(request, 'services/parcel.html')

def bilik_acara(request):
    return render(request, 'services/bilik_acara.html')

def pakir(request):
    return render(request, 'services/pakir.html')

def tourism(request):
    return render(request, 'tourism.html')

def tourism_student(request):
    packages = TourPackage.objects.filter(is_edutrip=False, is_csr=False)
    return render(request, 'tourism/student.html', {'packages': packages})

def edutrip_csr(request):
    edutrips = TourPackage.objects.filter(is_edutrip=True)
    csr_packages = TourPackage.objects.filter(is_csr=True)
    return render(request, 'tourism/edutrip_csr.html', {
        'edutrips': edutrips,
        'csr_packages': csr_packages
    })

def booking(request):
    return render(request, 'booking.html')

def submit_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tempahan telah berjaya dihantar!')
            return redirect('booking')
    else:
        form = BookingForm()
    
    return render(request, 'booking/form.html', {'form': form})
