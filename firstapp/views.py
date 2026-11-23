from django.shortcuts import render
from .forms import StudentForm

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if(form.is_valid()):
            data = form.cleaned_data
            return render(request, 'firstapp/success.html', {'data':data})

        return render(request, 'firstapp/register.html', {'form':form})

    form = StudentForm()
    return render(request, 'firstapp/register.html', {'form':form})
