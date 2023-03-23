from django.urls import path
# from .views import SignUpView
from . import views



urlpatterns = [
    # path("signup/", SignUpView.as_view(), name="signup"),
    path('', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]