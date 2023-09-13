from django.db import models
from datetime import datetime
# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=256)
    car_title = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email