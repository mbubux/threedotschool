from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from students.models import admittedStudent
from django.contrib import messages

# Create your views here.
# Students page
def students(request):
    students_list = admittedStudent.objects.all()
    total_count = admittedStudent.objects.count()
    
    context = {
        'students_list': students_list,
        'total_count': total_count,
    }
    return render(request, 'students.html', context)




# Search student
def search_student(request):
    query = request.GET['student']
    if len(query) > 255:
        students_list = admittedStudent.objects.none()
    else:
        student_name = admittedStudent.objects.filter(student_name__icontains=query)
        class_admitted = admittedStudent.objects.filter(class_admitted__icontains=query)
        students_list = student_name.union(class_admitted)

    total_count = students_list.count()

    if total_count == 0:
        messages.warning(request, 'Please enter someting!')
        
    context = {
        'students_list': students_list,
        'total_count': total_count,
        }
    return render(request, 'search_student.html', context)
    # return HttpResponse('This is search!')




# Add student page
def add_student(request):
    if request.method == "POST":
        student_name = request.POST['student-name']
        father_name = request.POST['father-name']
        mother_name = request.POST['mother-name']
        dob = request.POST['dob']
        sex = request.POST['sex']
        mobile_number = request.POST['mobile-number']
        alternate_mobile_number = request.POST['alternate-mobile-number']
        aadhaar_number = request.POST['aadhaar-number']
        vill_town = request.POST['vill-town']
        post_office = request.POST['post-office']
        police_station = request.POST['police-station']
        gaon_panchayat = request.POST['gaon-panchayat']
        educational_block = request.POST['educational-block']
        cluster = request.POST['cluster']
        district = request.POST['district']
        state = request.POST['state']
        country = request.POST['country']
        pin = request.POST['pin']
        class_admitted = request.POST['class-admitted']
        bank_name = request.POST['bank-name']
        account_number = request.POST['account-number']
        branch_name = request.POST['branch-name']
        ifsc = request.POST['ifsc']
        student_photo = request.POST['st_photo']
        dob_certificate = request.POST['dob_certificate']

        if len(student_name) < 3:
            messages.error(request, 'Please fill the form correctly!')
        else:
            admitted_student = admittedStudent(student_name=student_name, father_name=father_name, mother_name=mother_name, date_of_birth=dob, sex=sex, mobile_number=mobile_number, alternate_mobile_number=alternate_mobile_number, aadhaar_number=aadhaar_number, village_town=vill_town, post_office=post_office, police_station=police_station,
                                               gaon_panchayat=gaon_panchayat, educational_block=educational_block, cluster=cluster, district=district, state=state, country=country, pin=pin, class_admitted=class_admitted, bank_name=bank_name, account_number=account_number, bank_branch_name=branch_name, ifsc_code=ifsc, student_photo=student_photo, student_document=dob_certificate)
            admitted_student.save()
            messages.success(
                request, 'New student has been admitted successfully!')

    return render(request, 'add_student.html')


# View details of each individual students - page
# def viewDetails(request, student_id):
#     student = get_object_or_404(admittedStudent, pk=student_id)
#     context = {'student': student}
#     return render(request, 'student_detail.html', context)


def student_detail(request, pk):
    student = get_object_or_404(admittedStudent, pk=pk)
    return render(request, 'student_detail.html', {'student': student})
