from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min, Sum

# from transport_management.models import Product, Supplier, Buyer, Order
from transport_management.models import Client, Vehicle, VehicleMaintanance, Driver, Product, Booking, Expense, Pod, Payment

def total_expense(self):
    total = Expense.objects.aggregate(TOTAL = Sum('diesel'))['TOTAL']
    print(total)
    return total
@login_required(login_url='login')
def dashboard(request):

    total_client = Client.objects.count()
    total_vehicle = Vehicle.objects.count()
    total_vehiclemaintanance = VehicleMaintanance.objects.filter(under_maintanance='yes').count()
    # total_vehiclemaintanance = VehicleMaintanance.objects.count()
    total_driver = Driver.objects.count()
    total_product = Product.objects.count()
    total_booking = Booking.objects.count()
    # total_expense = Expense.objects.filter().aggregate(data=Sum('diesel'))
    total_expense = Expense.objects.aggregate(total = Sum('diesel'))['total']
    print(total_expense)
    bookings = Booking.objects.all().order_by('-id')
    total_pod = Pod.objects.filter(received='yes').count()
    total_aknowledgement = Pod.objects.filter(aknowledgement='not ok').count()
    total_payment = Payment.objects.aggregate(total = Sum('amount'))['total']


    context = {
        'client': total_client,
        'vehicle': total_vehicle,
        'vehiclemaintanance': total_vehiclemaintanance,
        'driver': total_driver,
        'product': total_product,
        'booking': total_booking,
        'bookings': bookings,
        'expenses': total_expense,
        'pod': total_pod,
        'aknowledgement': total_aknowledgement,
        'payment': total_payment,
        

    }
  


    return render(request, 'dashboard.html', context)


