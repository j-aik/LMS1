from django import forms
from .models import CustomUser,Parent,Staff,Student # Import your User model
from .models import Staff, Subject, ClassST

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Ensure this is correctly imported
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }



class ParentEditForm(forms.ModelForm):
    class Meta:
        model =  Parent
        fields = ['phone_number', 'address', 'class_assigned']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'class_assigned': forms.Select(attrs={'class': 'form-select'}),
        }


class StaffEditForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
        exclude = ['user']


class StudentEditForm(forms.ModelForm):
    class_assigned = forms.ModelChoiceField(
        queryset=ClassST.objects.all(),
        empty_label="Select a class",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Student
        fields = ['date_of_birth', 'class_assigned', 'parent', 'attendence_percentage']  # Exclude 'user'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'class_assigned': forms.Select(attrs={'class': 'form-select'}),
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'attendence_percentage': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '100'}),
        }
