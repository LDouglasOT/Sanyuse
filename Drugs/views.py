from django.shortcuts import render
from Drugs.models import *
from django.http import HttpResponse
import datetime 
from . import views
from .form import *
from django.shortcuts import redirect


# Create your views here.
def get_Employees_view(request):
    Employees=employee.objects.all()
    context={
        "Employees":Employees
    }
    return render(request,"",context)

def drugs_view(request):
    form=DrugForm()
    if(request.method=="GET"):
        lists=Drug.objects.all()
        TotalCost=0
        ExpectedProfit=0
        for listing in lists:
            TotalCost+=listing.get_full_cost()
            ExpectedProfit+=listing.checkProfit()
    if(request.method=="POST"):
        post_data = request.data
        if(post_data.is_valid()):
            post_data.save()
        
    context = {
            "Profit":ExpectedProfit,
            "TotalCost":TotalCost,
            "Drugs":lists,
            "form":form
    }
    return render(request,"Drugs/Druglist.html",context)


def get_Expense_view(request):
    form=Expensesform()
    print(request)
    TotalExpenses=0
    listings = Expense.objects.filter(Date=datetime.date.today())
    if request.method == "GET":
        for expense in listings:
            TotalExpenses += expense.Amount
    if request.method == "POST":
        print("got")
        form = Expensesform(request.POST)
        if form.is_valid():
            form.save()
            listings = Expense.objects.filter(Date=datetime.date.today())
            for expense in listings:
                TotalExpenses += expense.Amount
            context={
                "expenses":listings,
                "TotalExpenses":TotalExpenses,
                'form':form
                    }
            return render(request,"Drugs/Expenses.html",context)

    context={
        "expenses":listings,
        "TotalExpenses":TotalExpenses,
        'form':form
    }
    return render(request,"Drugs/Expenses.html",context)

def Patient_view(request):
    if(request.method=="GET"):

        patientqs=views.models.Patients.objects.all()
    if(request.method=="POST"):
        Patients=request.data
        if(Patients.is_valid()):
            Patient.save()
            

    context={
        "Patients":patientqs,
        "Count":patientqs.count 
    }
    
    return render(request,"Drugs/Patients.html",context)

def delete_expense(request,slug):
    form=Expensesform()
    if slug:
        item=Expense.objects.filter(Reason=slug)
        item.delete()
        TotalExpenses=0
        listings = Expense.objects.filter(Date=datetime.date.today())
        for expense in listings:
            TotalExpenses += expense.Amount
        context={
                "expenses":listings,
                "TotalExpenses":TotalExpenses,
                'form':form
                }
        return redirect("/expenses")
    else:
        return
def new_order(request,slug):
    if slug:
        selected=Drug.objects.filter(DrugName=slug)
        print(selected)
        return redirect("Drugs/Expenses.html")

