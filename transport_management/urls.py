from django.urls import path
from django.conf.urls import include
from . import views

from .views import (
    create_client,
    create_vehicle,
    create_vehiclemaintanance,
    create_driver,
    create_product,
    create_booking,
    update_booking,
    create_expense,
    create_pod,
    create_payment,
    update_pod,
    create_invoice,
    totexp,
  


    ClientListView,
    VehicleListView,
    VehicleMaintananceListView,
    DriverListView,
    ProductListView,
    BookingListView,
    BookingPendingListView,
    BookingProcessingListView,
    BookingCompleteListView,
    BookingDeliveredListView,
    BookingApprovedListView,
    BookingDeclineListView,
    ExpenseListView,
    PodListView,
    PaymentListView,
    PodReceivedListView,
    PodNotReceivedListView,
    AkNotOkListView,
    AkOkListView,
    VehicleUnderMaintananceListView,
    
    


)


urlpatterns = [
    path('create-client/', create_client, name='create-client'),
    path('client-list/', ClientListView.as_view(), name='client-list'),
    path('create-vehicle/', create_vehicle, name='create-vehicle'),
    path('vehicle-list/', VehicleListView.as_view(), name='vehicle-list'),
    path('create-vehiclemaintanance/', create_vehiclemaintanance, name='create-vehiclemaintanance'),
    path('vehiclemaintanance-list/', VehicleMaintananceListView.as_view(), name='vehiclemaintanance-list'),
    path('vehicle-under-maintanance-list/', VehicleUnderMaintananceListView.as_view(), name='vehicle-under-maintanance-list'),
    path('create-driver/', create_driver, name='create-driver'),
    path('driver-list/', DriverListView.as_view(), name='driver-list'),
    path('create-product/', create_product, name='create-product'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('create-booking/', create_booking, name='create-booking'),
    path('booking-list/', BookingListView.as_view(), name='booking-list'),
    path('update-booking/<int:id>/', update_booking, name='update-booking'),
    path('booking-pending/', BookingPendingListView.as_view(), name='booking-pending'),
    path('booking-processing/', BookingProcessingListView.as_view(), name='booking-processing'),
    path('booking-complete/', BookingCompleteListView.as_view(), name='booking-complete'),
    path('booking-delivered/', BookingDeliveredListView.as_view(), name='booking-delivered'),
    path('booking-approved/', BookingApprovedListView.as_view(), name='booking-approved'),
    path('booking-decline/', BookingDeclineListView.as_view(), name='booking-decline'),
    path('create-expense/', create_expense, name='create-expense'),
    path('expense-list/', ExpenseListView.as_view(), name='expense-list'),
    path('create-pod/', create_pod, name='create-pod'),
    path('update-pod/<int:id>/', update_pod, name='update-pod'),
    path('pod-list/', PodListView.as_view(), name='pod-list'),
    path('pod-received-list/', PodReceivedListView.as_view(), name='pod-received-list'),
    path('pod-not-received-list/', PodNotReceivedListView.as_view(), name='pod-not-received-list'),
    path('ak-notok-list/', AkNotOkListView.as_view(), name='ak-notok-list'),
    path('ak-ok-list/', AkOkListView.as_view(), name='ak-ok-list'),
    path('create-payment/', create_payment, name='create-payment'),
    path('payment-list/', PaymentListView.as_view(), name='payment-list'),
    path('invoice/', create_invoice, name='invoice'),

    path('popup/', totexp, name='popup'),
    path('',views.amount)
]

