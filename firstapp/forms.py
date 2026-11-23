from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=10)
    age = forms.IntegerField()
