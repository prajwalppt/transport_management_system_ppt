from django.urls import path
from django.conf.urls import include


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


    ClientListView,
    VehicleListView,
    VehicleMaintananceListView,
    DriverListView,
    ProductListView,
    BookingListView,
    ExpenseListView,
    PodListView,


)


urlpatterns = [
    path('create-client/', create_client, name='create-client'),
    path('client-list/', ClientListView.as_view(), name='client-list'),
    path('create-vehicle/', create_vehicle, name='create-vehicle'),
    path('vehicle-list/', VehicleListView.as_view(), name='vehicle-list'),
    path('create-vehiclemaintanance/', create_vehiclemaintanance, name='create-vehiclemaintanance'),
    path('vehiclemaintanance-list/', VehicleMaintananceListView.as_view(), name='vehiclemaintanance-list'),
    path('create-driver/', create_driver, name='create-driver'),
    path('driver-list/', DriverListView.as_view(), name='driver-list'),
    path('create-product/', create_product, name='create-product'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('create-booking/', create_booking, name='create-booking'),
    path('booking-list/', BookingListView.as_view(), name='booking-list'),
    path('update-booking/<int:id>/', update_booking, name='update-booking'),
    path('create-expense/', create_expense, name='create-expense'),
    path('expense-list/', ExpenseListView.as_view(), name='expense-list'),
    path('create-pod/', create_pod, name='create-pod'),
    path('pod-list/', PodListView.as_view(), name='pod-list'),
]


# urlpatterns = [
#     path('create-supplier/', create_supplier, name='create-supplier'),
#     path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
#     path('supplier-delete/<int:id>/', delete_supplier, name='supplier-delete'),
#     path('supplier-update/<int:id>/', update_supplier, name='update-supplier'),



#     path('create-buyer/', create_buyer, name='create-buyer'),
#     path('create-season/', create_season, name='create-season'),
#     path('create-drop/', create_drop, name='create-drop'),
#     path('create-product/', create_product, name='create-product'),

#     path('create-order/', create_order, name='create-order'),
#     path('order-list/', OrderListView.as_view(), name='order-list'),
#     path('order-update/<int:id>/', order_update, name='order-update'),



#     path('create-delivery/', create_delivery, name='create-delivery'),

#     path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
#     path('season-list/', SeasonListView.as_view(), name='season-list'),
#     path('drop-list/', DropListView.as_view(), name='drop-list'),

#     path('product-list/', ProductListView.as_view(), name='product-list'),

    
#     path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
# ]
