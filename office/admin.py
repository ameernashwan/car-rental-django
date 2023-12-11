from django.contrib import admin
from .models import (
    Category,
    Car,
    Branch,
    Employee,
    TaskEmployee,
    Customer,
    Reservation,
    Invoice,
    Accident,
    AccidentCauser,
    AccidentBill,
    Review,
    User,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "description")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "vin", "description", "color", "brand", "model", "category")


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "salary", "date_hired", "job_title", "branch", "user")


@admin.register(TaskEmployee)
class TaskEmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "task", "car")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "area_name",
        "city_name",
        "country_name",
        "identification_number",
        "user",
    )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "car", "customer", "start_date", "end_date", "branch")


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "reservation",
        "issue_date",
        "total_amount",
        "status",
        "discount_amount",
        "amount_due",
        "employee",
    )


@admin.register(Accident)
class AccidentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "causer",
        "car",
        "reservation",
        "accident_date",
        "car_status",
    )


@admin.register(AccidentCauser)
class AccidentCauserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "area_name",
        "city_name",
        "country_name",
        "identification_number",
    )


@admin.register(AccidentBill)
class AccidentBillAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "accident",
        "causer",
        "damage_rate",
        "total_amount",
        "status",
        "employee",
        "customer",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "reservation", "customer")


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "first_name",
#         "last_name",
#         "email",
#         "mobile",
#         "age",
#         "gender",
#         "language",
#         "created_at",
#         "update_at",
#     )
