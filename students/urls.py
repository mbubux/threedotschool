from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('add_student/', views.add_student, name='add_student'),
    path('view_detail/', views.student_detail, name='view_detail'),
    path('search_student/', views.search_student, name='search_student'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    # path('view_detail/<int:student_id>/', views.viewDetails, name='view_detail'),
]