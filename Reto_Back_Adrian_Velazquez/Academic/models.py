from django.db import models

class Student(models.Model):
       
   id = models.PositiveIntegerField(default=0, primary_key=True)
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   email_address = models.EmailField(max_length=100)
   phone_num = models.CharField(max_length=15)
   years_of_cursed = models.IntegerField(default=0)
   username = models.CharField(max_length=50, unique=True)
   

class AcademicHistory(models.Model):
    
   student = models.ForeignKey(Student, on_delete=models.CASCADE)

   course = models.CharField(max_length=100, null=True, blank=True)
   career = models.CharField(max_length=100, null=True, blank=True)
   name_of_university = models.TextField(max_length=100, null=True, blank=True)
   year_of_study = models.PositiveIntegerField(default=0)
   description_study_area = models.CharField(max_length=100, null=True, blank=True, verbose_name='Descripcion de la carrera')
   average = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)