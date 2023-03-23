from django.db import models
import datetime


# Create your models here.
class admittedStudent(models.Model):
    # Models Table
    student_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=17)
    mobile_number = models.CharField(max_length=15)
    alternate_mobile_number = models.CharField(max_length=15)
    aadhaar_number = models.CharField(max_length=15)
    village_town = models.CharField(max_length=255)
    post_office = models.CharField(max_length=255)
    police_station = models.CharField(max_length=255)
    gaon_panchayat = models.CharField(max_length=255)
    educational_block = models.CharField(max_length=255)
    cluster = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pin = models.CharField(max_length=6)
    # CLASS_CHOICES = (
    #     'Class 1',
    #     'Class 2',
    #     'Class 3',
    #     'Class 4',
    #     'Class 5',
    #     'Class 6',
    #     'Class 7',
    #     'Class 8',
    #     'Class 9',
    #     'Class 11',
    # )
    # class_admitted = models.CharField(max_length=20, choices=CLASS_CHOICES)
    class_admitted = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=30)
    bank_branch_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=11)
    student_photo = models.ImageField(upload_to="student_photos")
    student_document = models.FileField(upload_to="student_documents")
    # timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    # registration_id = models.CharField(max_length=10, unique=True)

    # def save(self, *args, **kwargs):
        # Generate a unique registration ID before saving the instance
        # self.registration_id = generate_registration_id(self.student_name, self.class_admitted)
        # super().save(*args, **kwargs)

    def __str__(self):
        return self.student_name




# Function to generate unique registration id
def generate_registration_id(name, admitted_class):
    # Get the current year and next year for the session
    current_year = datetime.datetime.now().year
    next_year = current_year + 1

    # Get the initials of the student's name
    initials = ''.join([word[0] for word in name.split()])

    # Format the registration ID
    registration_id = f"{current_year}{next_year}{initials.upper()}{admitted_class:02d}"

    return registration_id