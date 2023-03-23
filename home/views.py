from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.template import loader
from students.models import admittedStudent

# Create your views here.
@login_required(login_url='login')
def home(request):
    students = admittedStudent.objects.all()
    total_students = admittedStudent.objects.count()
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    context = {
        'students': students,
        'total_students': total_students,
    }
    return render(request, 'home.html', context)
