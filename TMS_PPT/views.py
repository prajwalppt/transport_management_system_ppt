from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from transport_management.models import Product, Supplier, Buyer, Order
from transport_management.models import Client, Vehicle, VehicleMaintanance, Driver, Product, Booking

@login_required(login_url='login')
def dashboard(request):

    total_client = Client.objects.count()
    total_vehicle = Vehicle.objects.count()
    total_vehiclemaintanance = VehicleMaintanance.objects.count()
    total_driver = Driver.objects.count()
    total_product = Product.objects.count()
    total_booking = Booking.objects.count()
    bookings = Booking.objects.all().order_by('-id')
    context = {
        'client': total_client,
        'vehicle': total_vehicle,
        'vehiclemaintanance': total_vehiclemaintanance,
        'driver': total_driver,
        'product': total_product,
        'booking': total_booking,
        'bookings': bookings

    }
  

    # total_product = Product.objects.count()
    # total_supplier = Supplier.objects.count()
    # total_buyer = Buyer.objects.count()
    # total_oder = Order.objects.count()
    # orders = Order.objects.all().order_by('-id')
    # context = {
    #     'product': total_product,
    #     'supplier': total_supplier,
    #     'buyer': total_buyer,
    #     'order': total_oder,
    #     'orders': orders
    # }
    # return render(request, 'dashboard.html', context)

    return render(request, 'dashboard.html', context)