from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegiter
from .models import User

# This function add and show the user 
def add_and_show(request):
    if request.method == 'POST':
        stu_form = StudentRegiter(request.POST)
        if stu_form.is_valid():
           # stu_form.save()
           nm = stu_form.cleaned_data['name']
           em = stu_form.cleaned_data['email']
           pw = stu_form.cleaned_data['password']
           # Create Model Object
           reg = User(name=nm, email=em, password=pw)
           reg.save()
           # for clear the form after click on add
           stu_form = StudentRegiter()
    else:
        stu_form = StudentRegiter()
    # Retriving data from model
    stu = User.objects.all()
    return render(request, 'enroll/add_and_show.html', {'form': stu_form, 'students': stu})

# Function for Update and Edit
def update_data(request, id):
    pi = User.objects.get(pk=id)
    stu_form = StudentRegiter(instance=pi)
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        stu_form = StudentRegiter(request.POST, instance=pi)
        if stu_form.is_valid():
           stu_form.save()
    return render(request, 'enroll/update_student.html', {'form':stu_form})

# This function for for delete the user form the database
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        # Page redirect to home after deleting the id
        return HttpResponseRedirect('/')
    
    
