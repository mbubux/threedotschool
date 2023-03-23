from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic

# Create your views here.

# Sign-up/Register account
def signupPage(request):
    if request.method == 'POST':
        # Get form input data
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # school_name = request.POST = ['school-name']
        # address = request.POST = ['address']
        # admin_photo = request.FILES.get('admin-photo')
        # school_logo = request.FILES.get('school-logo')

        print(fname, lname, email, username, password1)

        # Check if passwords match
        if password1 != password2:
            raise ValidationError("Passwords do not match!")

        else:
            # Check if username already exists in database
            if User.objects.filter(username=username).exists():
                raise ValidationError("Username already exists!")
            else:
                # Create user object
                new_user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=fname, last_name=lname)
                new_user.save()

                # Authenticate and login user
                # new_admin = authenticate(request, username=username, password=password1)
                # login(request, new_admin)

                # Redirect to login page
                return redirect('signup')
        # Set user profile fields
        # user.profile.school_name = school_name
        # user.profile.address = address
        # user.profile.admin_photo = admin_photo
        # user.profile.school_logo = school_logo
        # user.save()

    else:
        return render(request, 'registration/signup.html')


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

# Login user if already registered
def loginPage(request):
    if request.method == "POST":
        # Get form input data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate and login user
        my_user = authenticate(request, username=username, password=password)
        if my_user is not None:
            login(request, my_user)
            return render(request, 'home.html')
        else:
            return HttpResponse("No user is found!")

    # Else redirect to login page again
    return render(request, 'registration/login.html')


# Logout user
def logoutPage(request):
    logout(request)
    return redirect('login')