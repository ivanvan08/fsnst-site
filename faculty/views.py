from django.shortcuts import get_object_or_404, render

from .models import Department, ExchangeProgram, FacultyInfo, Program


def home(request):
    info = FacultyInfo.objects.first()
    return render(request, "faculty/home.html", {"info": info})


def program_list(request):
    programs = Program.objects.all()
    return render(request, "faculty/program_list.html", {"programs": programs})


def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    return render(request, "faculty/program_detail.html", {"program": program})


def department_list(request):
    departments = Department.objects.all()
    return render(request, "faculty/department_list.html", {"departments": departments})


def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    return render(request, "faculty/department_detail.html", {"department": department})


def exchange_list(request):
    exchanges = ExchangeProgram.objects.all()
    return render(request, "faculty/exchange_list.html", {"exchanges": exchanges})
