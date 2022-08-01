from django.urls import path
# from django.conf.urls import include
from .views import login_page, logout_page

urlpatterns = [
    path('login/', login_page, name='login'),
    # path('signup/', SignUp.as_view(), name='signup'),
    #  path('registration/',views.SignUp.as_view(),name='registration'),
    path('logout/', logout_page, name='logout'),
]
