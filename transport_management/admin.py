from django.contrib import admin
from django.views.generic import ListView
from .models import Client, Vehicle, VehicleMaintanance, Driver, Product, Booking
# Register your models here.

admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(VehicleMaintanance)
admin.site.register(Driver)
admin.site.register(Product)
admin.site.register(Booking)
# from .models import (
#     Booking,
#     Supplier,
#     Buyer,
#     Season,
#     Drop,
#     Product,
#     Order,
#     Delivery,
#     Vehical,
#     Driver,
#     Goods,
#     VehicleMaintanance,
#     Booking
# )


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'address', 'created_date']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['registration_no', 'owner_name', 'manufacture_company', 'insurance_valid_till', 'permit_tax_valid_till', 'fitness_valid_till']

class VehicleMaintananceAdmin(admin.ModelAdmin):
    list_display = ['id']
    # list_display = ['vehicle_no', 'date_of_initialization', 'odometer_reading', 'oil_changed', 'spare_parts_replaced', 'total_cost_of_maintenance']

class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number','aadhar_card_no', 'liscence_no', 'liscence_expiry_date', 'joining_date', 'remarks']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight_in_kg','rate']


# class SupplierAdmin(admin.ModelAdmin):
#     # list_display = ['user', 'name', 'address', 'created_date']
#     list_display = ['name', 'address', 'created_date']


# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ['name', 'address', 'created_date']
#     # list_display = ['user', 'name', 'address', 'created_date']

# class VehicalAdmin(admin.ModelAdmin):
#     # list_display = ['registration_No','owner_name','manufacture_company']
#     list_display = ['registration_No','owner_name','manufacture_company','insurance_valid_till','permit_tax_valid_till','fitness_valid_till']

# class DriverAdmin(admin.ModelAdmin):
#     list_display = ['name','phone_number','liscence_no','liscence_expiry_date','aadhar_card_no','joining_date']

# class GoodsAdmin(admin.ModelAdmin):
#     list_display = ['name','phone_number', 'weight']

# class VehicleMaintananceAdmin(admin.ModelAdmin):
#     list_display = ['id']

# class BookingAdmin(admin.ModelAdmin):
#     list_display = ['client','vehicle','product','driver','Frighe_amount','loading_date','weight_in_tons','location_from','location_to']


# admin.site.register(Booking, BookingAdmin)
# admin.site.register(VehicleMaintanance, VehicleMaintananceAdmin)
# admin.site.register(Vehical, VehicalAdmin)
# admin.site.register(Supplier, SupplierAdmin)
# admin.site.register(Buyer, BuyerAdmin)
# admin.site.register(Season)
# admin.site.register(Driver)
# admin.site.register(Goods)
# admin.site.register(Drop)
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(Delivery)
