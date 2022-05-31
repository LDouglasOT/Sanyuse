from django.forms import ModelForm
from Drugs.models import *

class Expensesform(ModelForm):
    class Meta:
        model = Expense
        fields ="__all__"

class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields ="__all__"