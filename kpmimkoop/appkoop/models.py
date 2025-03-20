from django.db import models

# Create your models here.

class AboutContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    page_type = models.CharField(max_length=20, choices=[
        ('HISTORY', 'Sejarah'),
        ('VISION', 'Visi'),
        ('MISSION', 'Misi'),
    ])
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
class OrganizationMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='org_members/')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.position}"
        
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    BOOKING_TYPES = [
        ('BILIK', 'Bilik Acara'),
        ('DOBI', 'Dobi'),
        ('PARCEL', 'Parcel'),
        ('PAKIR', 'Pakir Berbumbung'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPES)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    time_start = models.TimeField()
    time_end = models.TimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Menunggu'),
        ('APPROVED', 'Diluluskan'),
        ('REJECTED', 'Ditolak'),
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.booking_type} ({self.date_start})"

class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tours/')
    is_edutrip = models.BooleanField(default=False)
    is_csr = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class KoopMartOrder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    order_details = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Menunggu'),
        ('PROCESSING', 'Diproses'),
        ('COMPLETED', 'Selesai'),
        ('CANCELLED', 'Dibatalkan'),
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d/%m/%Y')}"
