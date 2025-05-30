from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    
    # About pages
    path('tentang/', views.about, name='about'),
    path('tentang/sejarah/', views.history, name='history'),
    path('tentang/visi/', views.vision, name='vision'),
    path('tentang/misi/', views.mission, name='mission'),
    
    # Organization
    path('organisasi/', views.organization, name='organization'),
    path('organisasi/carta/', views.org_chart, name='org_chart'),
    
    # Services
    path('perkhidmatan/', views.services, name='services'),
    path('perkhidmatan/cafe-air/', views.cafe_air, name='cafe_air'),
    path('perkhidmatan/koop-mart/', views.koop_mart, name='koop_mart'),
    path('perkhidmatan/kios-aok-cafe/', views.kiosk_aok, name='kiosk_aok'),
    path('perkhidmatan/dobi/', views.dobi, name='dobi'),
    path('perkhidmatan/parcel/', views.parcel, name='parcel'),
    path('perkhidmatan/bilik-acara/', views.bilik_acara, name='bilik_acara'),
    path('perkhidmatan/pakir-berbumbung/', views.pakir, name='pakir'),
    path('perkhidmatan/kios-aok-cafe/', views.kios_aok, name='kios_aok'),
    
    # Tourism
    path('pelancongan/', views.tourism, name='tourism'),
    path('pelancongan/siswa/', views.tourism_student, name='tourism_student'),
    path('pelancongan/edutrip-csr/', views.edutrip_csr, name='edutrip_csr'),
    

] 