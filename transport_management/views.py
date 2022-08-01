from django.shortcuts import render
from functools import partial
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.

from users.models import User

from .models import Client, Vehicle, VehicleMaintanance, Driver, Product, Booking

from .forms import (ClientForm, VehicleForm, VehicleMaintananceForm, DriverForm, ProductForm, BookingForm, BookingUpdateForm)


# from users.models import User
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
#     VehicleMaintanance
# )
# from .forms import (
#     BookingForm,
#     BookingUpdateForm,
#     SupplierForm,
#     BuyerForm,
#     SeasonForm,
#     DriverForm,
#     DropForm,
#     ProductForm,
#     OrderForm,
#     DeliveryForm,
#     VehicalForm,
#     GoodsForm,
#     VehicleMaintenaceForm,
#     SupplierFormUpdate
# )


# Client views
@login_required(login_url='login')
def create_client(request):
    forms = ClientForm()
    if request.method == 'POST':
        forms = ClientForm(request.POST)
        if forms.is_valid():
            # forms.save()
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            phone_number = forms.cleaned_data['phone_number']
            Client.objects.create(name=name, address=address, email=email, phone_number=phone_number)
        
            return redirect('client-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_client.html', context)


class ClientListView(ListView):
    model = Client
    template_name = 'transport_management/client_list.html'
    context_object_name = 'client'


# Vehicle views
@login_required(login_url='login')
def create_vehicle(request):
    forms = VehicleForm()
    if request.method == 'POST':
        forms = VehicleForm(request.POST)
        if forms.is_valid():
            Vehicle.objects.create(
               registration_no=forms.cleaned_data['registration_no'],
                owner_name=forms.cleaned_data['owner_name'],
                manufacture_company=forms.cleaned_data['manufacture_company'],
                insurance_valid_till=forms.cleaned_data['insurance_valid_till'],
                permit_tax_valid_till=forms.cleaned_data['permit_tax_valid_till'],
                fitness_valid_till=forms.cleaned_data['fitness_valid_till'],
            )
            return redirect('vehicle-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_vehicle.html', context)


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'transport_management/vehicle_list.html'
    context_object_name = 'vehicle'


#Vehiclemaintanance views
@login_required(login_url='login')
def create_vehiclemaintanance(request):
    forms = VehicleMaintananceForm()
    if request.method == 'POST':
        forms = VehicleMaintananceForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('vehiclemaintanance-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_vehiclemaintanance.html', context)


class VehicleMaintananceListView(ListView):
    model = VehicleMaintanance
    template_name = 'transport_management/vehiclemaintanance_list.html'
    # context_object_name = 'drop'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiclemaintanance'] = VehicleMaintanance.objects.all().order_by('-id')
        return context


# Driver views
@login_required(login_url='login')
def create_driver(request):
    forms = DriverForm()
    if request.method == 'POST':
        forms = DriverForm(request.POST)
        if forms.is_valid():
            Driver.objects.create(
                name =forms.cleaned_data['name'],
                phone_number=forms.cleaned_data['phone_number'],
                aadhar_card_no=forms.cleaned_data['aadhar_card_no'],
                liscence_no=forms.cleaned_data['liscence_no'],
                liscence_expiry_date=forms.cleaned_data['liscence_expiry_date'],
                joining_date=forms.cleaned_data['joining_date'],
                remarks =forms.cleaned_data['remarks']
            )
            return redirect('driver-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_driver.html', context)

class DriverListView(ListView):
    model = Driver
    template_name = 'transport_management/driver_list.html'
    context_object_name = 'driver'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            Product.objects.create(
                name =forms.cleaned_data['name'],
                weight_in_kg =forms.cleaned_data['weight_in_kg'],
                rate =forms.cleaned_data['rate']
            )
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_product.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'transport_management/product_list.html'
    context_object_name = 'product'


# Booking views
@login_required(login_url='login')
def create_booking(request):
    forms = BookingForm()
    if request.method == 'POST':
        forms = BookingForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('booking-list')
    return render(request, 'transport_management/create_booking.html', {'form': forms })


class BookingListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking'] = Booking.objects.all().order_by('-id')
        return context

@login_required(login_url='login')
def update_booking(request,id):
    data = Booking.objects.get(pk=id)

    if request.method == 'POST':
        BookingUpdateForm(request.POST,instance=data).save()
        return redirect('booking-list')
    else:
        form = BookingUpdateForm(instance=data)
        context = { 'form': form }
        return render(request, 'transport_management/update_booking.html', context)

# @login_required(login_url='login')
# def delete_supplier(request,id):
#     print(id,request.method)
#     supplier = Supplier.objects.get(pk=id)
#     supplier.delete()
#     return redirect('supplier-list')

# @login_required(login_url='login')
# def update_supplier(request,id):
#     data = Supplier.objects.get(pk=id)
#     if request.method == 'POST':
#         SupplierFormUpdate(request.POST,instance=data).save()
#         return redirect('supplier-list')
#     else:
#         form = SupplierFormUpdate(instance=data)
#         context = { 'form': form }
#         return render(request, 'store/update_supplier.html', context)


# # # Season views
# # @login_required(login_url='login')
# # def create_season(request):
# #     forms = DriverForm()
# #     if request.method == 'POST':
# #         forms = DriverForm(request.POST)
# #         if forms.is_valid():
# #             forms.save()
# #             return redirect('season-list')
# #     context = {
# #         'form': forms
# #     }
# #     return render(request, 'store/create_season.html', context)

# # Driver views
# @login_required(login_url='login')
# def create_season(request):
#     forms = DriverForm()
#     if request.method == 'POST':
#         forms = DriverForm(request.POST)
#         if forms.is_valid():
#             Driver.objects.create(
#                 name =forms.cleaned_data['name'],
#                 phone_number=forms.cleaned_data['phone_number'],
#                 liscence_no=forms.cleaned_data['liscence_no'],
#                 liscence_expiry_date=forms.cleaned_data['liscence_expiry_date'],
#                 aadhar_card_no=forms.cleaned_data['aadhar_card_no'],
#                 joining_date=forms.cleaned_data['joining_date'],
#             )
#             return redirect('season-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/create_season.html', context)

# class SeasonListView(ListView):
#     model = Driver
#     template_name = 'store/season_list.html'
#     context_object_name = 'driver'


# # Drop views
# # @login_required(login_url='login')
# # def create_drop(request):
# #     forms = DropForm()
# #     if request.method == 'POST':
# #         forms = DropForm(request.POST)
# #         if forms.is_valid():
# #             forms.save()
# #             return redirect('drop-list')
# #     context = {
# #         'form': forms
# #     }
# #     return render(request, 'store/create_drop.html', context)




# # Order views
# @login_required(login_url='login')
# def create_order(request):
#     forms = BookingForm()
#     if request.method == 'POST':
#         forms = BookingForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('order-list')
#     return render(request, 'store/create_order.html', {'form': forms })


# class OrderListView(ListView):
#     model = Booking
#     template_name = 'store/order_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['booking'] = Booking.objects.all().order_by('-id')
#         return context

# # def update_supplier(request,id):
# #     data = Supplier.objects.get(pk=id)
#     # if request.method == 'POST':
#     #     SupplierFormUpdate(request.POST,instance=data).save()
#     #     return redirect('supplier-list')
#     # else:
#     #     form = SupplierFormUpdate(instance=data)
#     #     context = { 'form': form }
#     #     return render(request, 'store/update_supplier.html', context)

# @login_required(login_url='login')
# def order_update(request,id):
#     data = Booking.objects.get(pk=id)

#     if request.method == 'POST':
#         BookingUpdateForm(request.POST,instance=data).save()
#         return redirect('order-list')
#     else:
#         form = BookingUpdateForm(instance=data)
#         context = { 'form': form }
#         return render(request, 'store/order_update.html', context)

    

# # Delivery views
# @login_required(login_url='login')
# def create_delivery(request):
#     forms = DeliveryForm()
#     if request.method == 'POST':
#         forms = DeliveryForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('delivery-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/create_delivery.html', context)


# class DeliveryListView(ListView):
#     model = Delivery
#     template_name = 'store/delivery_list.html'
#     context_object_name = 'delivery'
