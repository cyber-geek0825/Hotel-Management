from django.urls import path,include
from . import views

app_name='homepage'

urlpatterns = [
    path('',view=views.home,name='homepage'),
    path('search_result/',view=views.search_result,name='search_result'),
    path('booking_page/',view=views.booking_page,name='booking_page'),
    path('final_page/',view=views.final_page,name='final_page'),
]