from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=25, min_length=5)
    email = forms.EmailField()
    mobile = forms.IntegerField(max_value=9999999999)
    password = forms.CharField(
        widget = forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        widget = forms.PasswordInput()
    )
