# from django.shortcuts import render, redirect
# from .models import Doctor, Description
# from .forms import OPPatientForm
# from django.contrib import messages

# def op_ticket_view(request):
#     if request.method == 'POST':
#         form = OPPatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Op Ticket saved successfully!")
#             return redirect('op_ticket')
#         else:
#             messages.error(request,"Invalid form data!")
#     else:
#         form = OPPatientForm()
#         doctors = Doctor.objects.all()
#         descriptions = Description.objects.all()
#     return render(request, 'opticket/op_ticket.html', { 'doctors': doctors,'description':descriptions})

from django.shortcuts import render, redirect
from .models import Doctor, Description
from .forms import OPPatientForm
from django.contrib import messages

def op_ticket_view(request):
    doctors = Doctor.objects.all()
    descriptions = Description.objects.all()

    if request.method == 'POST':
        form = OPPatientForm(request.POST)
        if form.is_valid():
            oppatient = form.save(commit=False)
            print("Saving OPPatient:", oppatient)
            oppatient.save()
            form.save_m2m()
            print("POST data:", request.POST)
            # form.save()
            messages.success(request, "OP Ticket saved successfully!")
            return redirect('op_ticket')
        else:
            messages.error(request, "Invalid form data!")
            print(form.errors)
    else:
        form = OPPatientForm()

    return render(request, 'opticket/op_ticket.html', {
        'form': form,
        'doctors': doctors,
        'description': descriptions,
        
    })