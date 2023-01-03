from django.urls import path
# from django.conf.urls import include
from .views import login_page, logout_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
