from django.shortcuts import render
from .forms import StudentForm

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                error = "Passwords do not match!"
                return render(request, 'firstapp/register.html', {'form': form, 'error': error})
            return render(request, 'firstapp.success.html', form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'firstapp/register.html', {'form': form})