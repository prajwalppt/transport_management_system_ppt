from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min, Sum
from django.contrib import messages
from django.db.models import F
from transport_management.models import Client, Vehicle, VehicleMaintanance, Driver, Product, Booking, Expense, Pod, Payment


@login_required(login_url='login')
def dashboard(request):

    total_client = Client.objects.count()
    total_vehicle = Vehicle.objects.count()
    total_vehiclemaintanance = VehicleMaintanance.objects.filter(under_maintanance='yes').count()

    total_driver = Driver.objects.count()
    total_product = Product.objects.count()
    total_booking = Booking.objects.count()
    diesel_expense = Expense.objects.aggregate(diesel = Sum('diesel'))['diesel']
    fastag_expense = Expense.objects.aggregate(fastag = Sum('fastag'))['fastag']
    driver_expense = Expense.objects.aggregate(driver_expense = Sum('driver_expense'))['driver_expense']
    uncertainty_expense = Expense.objects.aggregate(uncertainty = Sum('uncertainty'))['uncertainty']
    miscellaneous_expense = Expense.objects.aggregate(miscellaneous = Sum('miscellaneous'))['miscellaneous']
    print(int(diesel_expense+fastag_expense+driver_expense+uncertainty_expense+miscellaneous_expense))
    total_expense = diesel_expense+fastag_expense+driver_expense+uncertainty_expense+miscellaneous_expense
    total_payment = Payment.objects.aggregate(total = Sum('amount'))['total']
    print(total_payment-total_expense)
    profit = total_payment-total_expense
    bookings = Booking.objects.all().order_by('-id')
    total_pod = Pod.objects.filter(received='yes').count()
    total_pod_no = Pod.objects.filter(received='no').count()
    total_aknowledgement = Pod.objects.filter(aknowledgement='not ok').count()
    total_aknowledgement_ok = Pod.objects.filter(aknowledgement='ok').count()
    



    context = {
        'client': total_client,
        'vehicle': total_vehicle,
        'vehiclemaintanance': total_vehiclemaintanance,
        'driver': total_driver,
        'product': total_product,
        'booking': total_booking,
        'bookings': bookings,
        'diesel_expense': diesel_expense,
        'fastag_expense': fastag_expense,
        'driver_expense': driver_expense,
        'uncertainty_expense': uncertainty_expense,
        'miscellaneous_expense': miscellaneous_expense,
        'expenses': total_expense,
        'pod': total_pod,
        'podno': total_pod_no,
        'aknowledgement': total_aknowledgement,
        'aknowledgementok': total_aknowledgement_ok,
        'payment': total_payment,
        'profit': profit,
        

    }
  


    return render(request, 'dashboard.html', context)


