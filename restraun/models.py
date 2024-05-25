from django.db import models
from datetime import date

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField(default=date.today, help_text='Enter date in YYYY-MM-DD format')
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name

class Menu(models.Model):
    name = models.CharField(max_length=200) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='') 

    def __str__(self):
        return self.name
