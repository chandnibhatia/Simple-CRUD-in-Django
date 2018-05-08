from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Client(models.Model):
    client_name = models.CharField(max_length=20, unique=True, help_text="Client name should be unique.")
    contact_name = models.CharField(max_length=200, help_text="Please! Enter your full name.")
    birth_date = models.DateField()
    email_address = models.EmailField()
    area_code = models.PositiveSmallIntegerField()
    phone_number = models.PositiveIntegerField()
    mobile_number = models.PositiveIntegerField(max_length=10, blank=True)
    street_name = models.CharField(max_length=200, blank=True)
    suburb = models.CharField(max_length=100)
    postcode = models.PositiveIntegerField(max_length=9)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name
