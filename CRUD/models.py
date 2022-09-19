from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_np=models.IntegerField('employee number',primary_key=True)
    birth_date=models.DateField('birthday')
    first_name=models.CharField('first name',max_length=14)
    last_name=models.CharField('last name',max_length=16)
    gender=models.CharField('gender',max_length=1)
    hire_date=models.DateField('hire date')

    class Meta:
        db_table='CRUD'

    def str(self):
        return "{} {}".format(self.first_name,self.last_name)