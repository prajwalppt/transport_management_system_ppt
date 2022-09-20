from pyexpat import model
# from attr import field, fields
from django import forms
from django.forms import ModelForm
# from matplotlib.pyplot import cla

from .models import Client, Vehicle, VehicleMaintanance, Driver, Booking, Expense, Pod, Payment


#clientform
class ClientForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', max_length=15,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'phone_number',
        'data-val': 'true',
        'data-val-required': 'Please enter phone_number',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))


#vehicleform
class VehicleForm(forms.Form):
    registration_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter Number',
    }))
    owner_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter owner_name',
    }))
    manufacture_company = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter manufacture_company',
    }))
    insurance_valid_till = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control datetimepicker-input',
            'id': 'datepicker1'
        }))
    permit_tax_valid_till = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control datetimepicker-input',
            'id': 'datepicker2'
        }))
    fitness_valid_till = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control datetimepicker-input',
            'id': 'datepicker3'
        }))



#vehiclemaintananceform
class VehicleMaintananceForm(forms.ModelForm):
    class Meta:
        model = VehicleMaintanance
        fields = ['vehicle_no', 'under_maintanance','date_of_initialization','odometer_reading','oil_changed','spare_parts_replaced','total_cost_of_maintenance']

        widgets = {
            'vehicle_no': forms.Select(attrs={
                'class': 'form-control', 'id': 'vehicle_no'
            }),
            'under_maintanance': forms.Select(attrs={
                'class': 'form-control', 'id': 'under_maintanance'
            }),
            'date_of_initialization': forms.DateInput(attrs={
                'class': 'form-control datetimepicker-input', 'id': 'datepicker1'
            }),
            'odometer_reading': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'odometer_reading'
            }),
            'oil_changed': forms.Select(attrs={
                'class': 'form-control', 'id': 'oil_changed'
            }),
            'spare_parts_replaced': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'spare_parts_replaced'
            }),
            'total_cost_of_maintenance': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'total_cost_of_maintenance'
            }),
           
        }

#driverform
class DriverForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', max_length=15,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'phone_number',
        'data-val': 'true',
        'data-val-required': 'Please enter phone_number',
    }))
    aadhar_card_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter aadhar_card_no',
    }))
    liscence_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter liscence_no',
    }))
    liscence_expiry_date = forms.DateField(widget=forms.TextInput(attrs={
            'class': 'form-control datetimepicker-input',
            'id': 'datepicker1'
        }))
    joining_date = forms.DateField(widget=forms.TextInput(attrs={
            'class': 'form-control datetimepicker-input',
            'id': 'datepicker2'
    }))
    remarks = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter remarks',
    }))


#productform
class ProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter name of Goods',
    }))
    value = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter value',
    }))

    weight = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-val': 'true',
        'data-val-required': 'Please enter weight',
    }))


#bookingform
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client','vehicle','product','no_of_product','driver','loading_date','weight','location_from','location_to','freight_amount']

        widgets = {
            'client': forms.Select(attrs={
                'class': 'form-control', 'id': 'client'
            }),
            'vehicle': forms.Select(attrs={
                'class': 'form-control datetimepicker-input', 'id': 'vehicle'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'no_of_product': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'no_of_product'
            }),
            'driver': forms.Select(attrs={
                'class': 'form-control', 'id': 'driver'
            }),
            'freight_amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'freight_amount'
            }),
            'loading_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'datepicker1'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'weight'
            }),
            'location_from': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'location_from'
            }),
           'location_to': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'location_to'
            }),
             'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),
        }

    def multiply_two_integers(value, no_of_product):
        freight_amount = value*no_of_product
        return freight_amount

#bookingupdate
class BookingUpdateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client','vehicle','product','no_of_product','driver','loading_date','weight','location_from','location_to','freight_amount', 'status']

        widgets = {
            'client': forms.Select(attrs={
                'class': 'form-control', 'id': 'client'
            }),
            'vehicle': forms.Select(attrs={
                'class': 'form-control datetimepicker-input', 'id': 'vehicle'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'no_of_product': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'no_of_product'
            }),
            'driver': forms.Select(attrs={
                'class': 'form-control', 'id': 'driver'
            }),
            'freight_amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'freight_amount'
            }),
            'loading_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'datepicker1'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'weight'
            }),
            'location_from': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'location_from'
            }),
           'location_to': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'location_to'
            }),
             'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),
        }
    def __init__(self, *args, **kwargs):
        super(BookingUpdateForm, self).__init__(*args, **kwargs)
        self.fields['client'].disabled = True
        self.fields['vehicle'].disabled = True
        self.fields['product'].disabled = True
        self.fields['no_of_product'].disabled = True
        self.fields['driver'].disabled = True
        self.fields['freight_amount'].disabled = True
        self.fields['loading_date'].disabled = True
        self.fields['weight'].disabled = True
        self.fields['location_from'].disabled = True
        self.fields['location_to'].disabled = True

#expenseform
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['booking_no','diesel','fastag','driver_expense','uncertainty','miscellaneous', 'expense_date']

        widgets = {
            'booking_no': forms.Select(attrs={
                'class': 'form-control', 'id': 'booking_no'
            }),
            'diesel': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'diesel'
            }),
            'fastag': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'fastag'
            }),
            'driver_expense': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'driver_expense'
            }),
            'uncertainty': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'uncertainty'
            }),
            'miscellaneous': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'miscellaneous'
            }),
            'expense_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'datepicker1'
            }),
        }


#podform
class PodForm(forms.ModelForm):
    class Meta:
        model = Pod
        fields = ['booking_no','received','received_date','aknowledgement','remarks']

        widgets = {
            'booking_no': forms.Select(attrs={
                'class': 'form-control', 'id': 'booking_no'
            }),
            'received': forms.Select(attrs={
                'class': 'form-control', 'id': 'received'
            }),
            'received_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'datepicker1'
            }),
            'aknowledgement': forms.Select(attrs={
                'class': 'form-control', 'id': 'aknowledgement'
            }),
            'remarks': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'remarks'
            }),           
        }


class PodUpdateForm(forms.ModelForm):
    class Meta:
        model = Pod
        fields = ['booking_no','received','received_date','aknowledgement','remarks']

        widgets = {
            'booking_no': forms.Select(attrs={
                'class': 'form-control', 'id': 'booking_no'
            }),
            'received': forms.Select(attrs={
                'class': 'form-control', 'id': 'received'
            }),
            'received_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'datepicker1'
            }),
            'aknowledgement': forms.Select(attrs={
                'class': 'form-control', 'id': 'aknowledgement'
            }),
            'remarks': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'remarks'
            }),           
        }

    def __init__(self, *args, **kwargs):
        super(PodUpdateForm, self).__init__(*args, **kwargs)
        self.fields['booking_no'].disabled = True
        

#paymentform
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking_no','amount','mode','transaction_no','payment_date']

        widgets = {
            'booking_no': forms.Select(attrs={
                'class': 'form-control', 'id': 'booking_no'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'mode': forms.Select(attrs={
                'class': 'form-control', 'id': 'mode'
            }),
            'transaction_no': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'transaction_no'
            }),
            'payment_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'datepicker1'
            }),           
        }
