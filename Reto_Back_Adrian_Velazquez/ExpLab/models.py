from django.db import models

class Employee(models.Model):
 
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   email_address = models.EmailField(max_length=100)
   phone_num = models.CharField(max_length=15)
   years_of_experience = models.IntegerField(default=0)
   username = models.CharField(max_length=50, unique=True, primary_key=True)

class Experience(models.Model):
    
   employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

   organization_one = models.CharField(max_length=100, null=True, blank=True)
   job_position_one = models.CharField(max_length=100, null=True, blank=True)
   description = models.TextField(max_length=500, null=True, blank=True)
   year = models.PositiveIntegerField(default=0)
   departure = models.CharField(max_length=100, null=True, blank=True, verbose_name='Motivo de la salida')

   organization_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Empresa')
   job_position_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Posicion')
   description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Descripcion del puesto')
   year = models.PositiveIntegerField(default=0)
   departure = models.CharField(max_length=100, null=True, blank=True, verbose_name='Motivo de la salida')

   organization_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Empresa')
   job_position_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Posision')
   description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Descripcion del puesto')
   year = models.PositiveIntegerField(default=0)
   departure = models.CharField(max_length=100, null=True, blank=True, verbose_name='Motivo de la salida')

   organization_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Empresa')
   job_position_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Posision')
   description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Descripcion del puesto')
   year = models.PositiveIntegerField(default=0)
   departure = models.CharField(max_length=100, null=True, blank=True, verbose_name='Motivo de la salida')

   organization_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Empresa')
   job_position_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Posision')
   description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Descripcion del puesto')
   year = models.PositiveIntegerField(default=0)
   departure = models.CharField(max_length=100, null=True, blank=True, verbose_name='Motivo de la salida')

   organization_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Empresa')
   job_position_one = models.CharField(max_length=100, null=True, blank=True, verbose_name='Posision')
   description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Descripcion del puesto')
   year = models.PositiveIntegerField(default=0)
   departure = models.CharField(max_length=100, null=True, blank=True, verbose_name='Motivo de la salida')