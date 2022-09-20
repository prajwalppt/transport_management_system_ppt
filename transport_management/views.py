from django.shortcuts import render
from functools import partial
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from django.core.validators import validate_email
from django.db.models import Avg, Max, Min, Sum
# Create your views here.

from users.models import User

from .models import Client, Vehicle, VehicleMaintanance, Driver, Product, Booking, Expense, Pod, Payment

from .forms import (
    ClientForm,
    VehicleForm,
    VehicleMaintananceForm,
    DriverForm,
    ProductForm,
    BookingForm,
    BookingUpdateForm,
    ExpenseForm,
    PodForm,
    PodUpdateForm,
    PaymentForm

    )


@login_required(login_url='login')
def create_invoice(request):
    return render(request, 'transport_management/invoice.html')

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
            messages.success(request, 'Client added succesfully')
            print(email)
            return redirect('client-list')
            print(email)

        else:
            form = ClientForm()
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_client.html', context)


class ClientListView(ListView):
    model = Client
    template_name = 'transport_management/client_list.html'
    context_object_name = 'client'


#total exp views
def totexp(request):
    diesel_expense = Expense.objects.aggregate(diesel = Sum('diesel'))['diesel']
    fastag_expense = Expense.objects.aggregate(fastag = Sum('fastag'))['fastag']
    driver_expense = Expense.objects.aggregate(driver_expense = Sum('driver_expense'))['driver_expense']
    uncertainty_expense = Expense.objects.aggregate(uncertainty = Sum('uncertainty'))['uncertainty']
    miscellaneous_expense = Expense.objects.aggregate(miscellaneous = Sum('miscellaneous'))['miscellaneous']
    # model = Expense
    template_name = 'transport_management/popup.html'
    # context_object_name = 'totalexp'
    context = {
        'diesel_expense': diesel_expense,
        'fastag_expense': fastag_expense,
        'driver_expense': driver_expense,
        'uncertainty_expense': uncertainty_expense,
        'miscellaneous_expense': miscellaneous_expense,
        

    }

    return render(request, 'transport_management/popup.html', context)

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
            messages.success(request, 'Vehicle added succesfully')
            return redirect('vehicle-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_vehicle.html', context)


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'transport_management/vehicle_list.html'
    # context_object_name = 'drop'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle'] = Vehicle.objects.all().order_by('-id')
        return context

# class VehicleListView(ListView):
#     model = Vehicle
#     template_name = 'transport_management/vehicle_list.html'
#     context_object_name = 'vehicle'


#Vehiclemaintanance views
@login_required(login_url='login')
def create_vehiclemaintanance(request):
    forms = VehicleMaintananceForm()
    if request.method == 'POST':
        forms = VehicleMaintananceForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Vehicle Maintanance record added succesfully')
            return redirect('vehiclemaintanance-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_vehiclemaintanance.html', context)
    queryset = VehicleMaintanance.objects.filter( Q(under_maintanance='yes'))


class VehicleMaintananceListView(ListView):
    model = VehicleMaintanance
    template_name = 'transport_management/vehiclemaintanance_list.html'
    # context_object_name = 'drop'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiclemaintanance'] = VehicleMaintanance.objects.all().order_by('-id')
        return context

#Vehicle_under_maintanance_views
class VehicleUnderMaintananceListView(ListView):
    model = VehicleMaintanance
    template_name = 'transport_management/vehicle_under_maintanance.html'
    context_object_name = 'vehicleundermaintanance'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicleundermaintanance"] = VehicleMaintanance.objects.filter(under_maintanance ='yes')
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
            messages.success(request, 'Driver added succesfully')
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
                weight =forms.cleaned_data['weight'],
                value =forms.cleaned_data['value']
            )
            messages.success(request, 'Product added succesfully')
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'transport_management/create_product.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'transport_management/product_list.html'
    context_object_name = 'product'


# Booking new views
@login_required(login_url='login')
def create_booking(request):
    forms = BookingForm()
    product = Product.objects.all()

    if request.method == 'POST':
        forms = BookingForm(request.POST)
        if forms.is_valid():
            Booking.objects.create(
                client =forms.cleaned_data['client'],
                vehicle =forms.cleaned_data['vehicle'],
                product =forms.cleaned_data['product'],
                no_of_product =forms.cleaned_data['no_of_product'],
                driver =forms.cleaned_data['driver'],
                weight =forms.cleaned_data['weight'],
                location_from =forms.cleaned_data['location_from'],
                location_to =forms.cleaned_data['location_to'],
                loading_date =forms.cleaned_data['loading_date'],
                freight_amount =forms.cleaned_data['freight_amount'],
                # status =forms.cleaned_data['status']
            )
            messages.success(request, 'Booking created succesfully')
            return redirect('booking-list')
    context = {
        'form': forms, 'product': product
    }
    return render(request, 'transport_management/create_booking.html', context)


#Booking Pending 
class BookingPendingListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_pending_list.html'
    context_object_name = 'bookingpending'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookingpending"] = Booking.objects.filter(status='pending')
        return context

#Booking Processing 
class BookingProcessingListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_processing_list.html'
    context_object_name = 'bookingprocessing'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookingprocessing"] = Booking.objects.filter(status='processing')
        return context

#Booking Delivered 
class BookingDeliveredListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_delivered_list.html'
    context_object_name = 'bookingdelivered'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookingdelivered"] = Booking.objects.filter(status='deliverd')
        return context


#Booking Approved 
class BookingApprovedListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_approved_list.html'
    context_object_name = 'bookingapproved'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookingapproved"] = Booking.objects.filter(status='approved')
        return context

#Booking Complete 
class BookingCompleteListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_complete_list.html'
    context_object_name = 'bookingcomplete'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookingcomplete"] = Booking.objects.filter(status='complete')
        return context

#Booking Decline 
class BookingDeclineListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_decline_list.html'
    context_object_name = 'bookingdecline'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookingdecline"] = Booking.objects.filter(status='decline')
        return context



def amount(request):
    result = Product.objects.all()
    return render(request, 'transport_management/create_booking.html', {'Product': result})

class BookingListView(ListView):
    model = Booking
    template_name = 'transport_management/booking_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking'] = Booking.objects.all().order_by('-id')
        return context

#bookingupdate
@login_required(login_url='login')
def update_booking(request,id):
    data = Booking.objects.get(pk=id)
    context = {
        'data': data,
        }


    if request.method == 'POST':
        BookingUpdateForm(request.POST,instance=data).save()
        messages.success(request, 'Booking status updated succesfully')
        return redirect('booking-list')
    else:
        form = BookingUpdateForm(instance=data)
        context = { 'form': form }
        # messages.success(request, 'Booking status updated succesfully')
        return render(request, 'transport_management/update_booking.html', context)
    
#Expense views
@login_required(login_url='login')
def create_expense(request):
    forms = ExpenseForm()
    if request.method == 'POST':
        forms = ExpenseForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Expense record added succesfully')
            return redirect('expense-list')
    return render(request, 'transport_management/create_expense.html', {'form': forms })

class ExpenseListView(ListView):
    model = Expense
    template_name = 'transport_management/expense_list.html'
    context_object_name = 'expense'

#POD views
@login_required(login_url='login')
def create_pod(request):
    forms = PodForm()
    if request.method == 'POST':
        forms = PodForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'POD record added succesfully')
            return redirect('pod-list')
    return render(request, 'transport_management/create_pod.html', {'form': forms })


#podupdate
@login_required(login_url='login')
def update_pod(request,id):
    data = Pod.objects.get(pk=id)

    if request.method == 'POST':
        PodUpdateForm(request.POST,instance=data).save()
        messages.success(request, 'Pod status updated succesfully')
        return redirect('pod-list')
    else:
        form = PodUpdateForm(instance=data)
        context = { 'form': form }
        # messages.success(request, 'Booking status updated succesfully')
        return render(request, 'transport_management/update_pod.html', context)


class PodListView(ListView):
    model = Pod
    total_received_pod = Pod.objects.filter(received='yes')
    template_name = 'transport_management/pod_list.html'
    context_object_name = 'pod'

 #Podreceivedview   
class PodReceivedListView(ListView):
    model = Pod
    template_name = 'transport_management/pod_received_list.html'
    context_object_name = 'podreceived'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["podreceived"] = Pod.objects.filter(received='yes')
        return context

 #Podnotreceived   
class PodNotReceivedListView(ListView):
    model = Pod
    template_name = 'transport_management/pod_not_received_list.html'
    context_object_name = 'podnotreceived'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["podnotreceived"] = Pod.objects.filter(received='no')
        return context


class AkNotOkListView(ListView):
    model = Pod
    template_name = 'transport_management/ak_notok_list.html'
    context_object_name = 'aknotok'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["aknotok"] = Pod.objects.filter(aknowledgement='not ok')
        return context


class AkOkListView(ListView):
    model = Pod
    template_name = 'transport_management/ak_ok_list.html'
    context_object_name = 'akok'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["akok"] = Pod.objects.filter(aknowledgement='ok')
        return context



#Payment views
@login_required(login_url='login')
def create_payment(request):
    forms = PaymentForm()
    if request.method == 'POST':
        forms = PaymentForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Payment record added succesfully')
            return redirect('payment-list')
    return render(request, 'transport_management/create_payment.html', {'form': forms })

class PaymentListView(ListView):
    model = Payment
    template_name = 'transport_management/payment_list.html'
    context_object_name = 'payment'
