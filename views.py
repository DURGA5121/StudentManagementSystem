from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'add.html', {'form': form})

def search_student(request):
    query = request.GET.get('q')
    students = []

    if query:
        students = Student.objects.filter(name__icontains=query)

    return render(request, 'search.html', {'students': students})

def update_student(request, id):
    student = Student.objects.get(id=id)

    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'update.html', {'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'delete.html', {'student': student})