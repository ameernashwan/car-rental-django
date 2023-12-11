from django.db import models

from config.utils.models import BaseEntity
from account.models import User


class Category(BaseEntity):
    label = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)


class Car(BaseEntity):
    vin = models.IntegerField(unique=True)
    description = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)
    brand = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)


class Branch(BaseEntity):
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)


class Employee(BaseEntity):
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    date_hired = models.DateTimeField(auto_now_add=True, null=False)
    job_title = models.CharField(max_length=255, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class TaskEmployee(BaseEntity):
    task = models.CharField(max_length=255, null=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False)


class Customer(BaseEntity):
    area_name = models.CharField(max_length=255, null=False)
    city_name = models.CharField(max_length=255, null=False)
    country_name = models.CharField(max_length=255, null=False)
    identification_number = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Reservation(BaseEntity):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False)


class Invoice(BaseEntity):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=False)
    issue_date = models.DateTimeField(null=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=255, null=False)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    amount_due = models.IntegerField(null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)


class AccidentCauser(BaseEntity):
    area_name = models.CharField(max_length=255, null=False)
    city_name = models.CharField(max_length=255, null=False)
    country_name = models.CharField(max_length=255, null=False)
    identification_number = models.IntegerField(null=False)


class Accident(BaseEntity):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    causer = models.ForeignKey(AccidentCauser, on_delete=models.CASCADE, null=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=False)
    accident_date = models.DateTimeField(null=False)
    car_status = models.CharField(max_length=255, null=False)


class AccidentBill(BaseEntity):
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE, null=False)
    causer = models.ForeignKey(AccidentCauser, on_delete=models.CASCADE, null=False)
    damage_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=255, null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)


class Review(BaseEntity):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(null=False)
