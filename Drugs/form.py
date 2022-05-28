from django.forms import ModelForm
from Drugs.models import Expense

class Expensesform(ModelForm):
    class Meta:
        model = Expense
        fields ="__all__"