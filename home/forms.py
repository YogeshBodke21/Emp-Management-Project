from django import forms
from .models import Employee, Role, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':"ex. Ajay", 'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder':"ex. Kohli",'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'placeholder':"ex. 10,000",'class':'form-control'}),
            'bonus': forms.NumberInput(attrs={'placeholder':"ex. 1,000",'class':'form-control'}),
            'designation': forms.TextInput(attrs={ "class":"custom-select custom-select-lg" }),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'hire_date': forms.DateInput(attrs={'class':'form-control'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Mobile Number',
        }
        