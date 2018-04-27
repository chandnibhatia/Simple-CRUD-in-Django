from django.db import models


# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=20, unique=True, help_text="Client name should be unique.")
    contact_name = models.CharField(max_length=200, help_text="Please! Enter your full name.")
    email_address = models.EmailField()
    phone_number = models.IntegerField()
    street_name = models.CharField(max_length=100, blank=True)
    suburb = models.CharField(max_length=100)
    postcode = models.IntegerField()
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.client_name
