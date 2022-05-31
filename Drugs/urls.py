from django.urls import path
from .views import *

urlpatterns = [
    path('',views.drugs_view,name="Home"),
    path('Patient/',views.Patient_view,name="Patient"),
    path('expenses/',views.get_Expense_view,name="expenses"),


    path('delete_form/<str:slug>',views.delete_expense,name="delete_form"),
    path('new_order/<slug:slug>',views.new_order,name="delete_form"),
   
]
