from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models


from django.db import models
from django.core.validators import RegexValidator

class ClassST(models.Model):
    name = models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^(LKG|UKG|[1-9][A-Z]|1[0-2][A-Z])$',
                message="Class name must be in the format 'LKG', 'UKG', '1A', '2B', ..., '12A'."
            )
        ]
    )

    def __str__(self):  # Fix incorrect __str_ method
        return self.name


class Subject(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class CustomUser(AbstractUser):


    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username}"






class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    class_assigned = models.ForeignKey(ClassST, on_delete=models.CASCADE, null=True,blank=True)
    def __str__(self):
        return self.user.username



class Staff(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject,blank=True)
    class_assigned = models.ForeignKey(ClassST,blank=True,null=True,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username




class Student(models.Model):

    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth=models.DateField()
    class_assigned=models.ForeignKey(ClassST,on_delete=models.SET_NULL,null=True)
    parent=models.ForeignKey(Parent,on_delete=models.SET_NULL,null=True,blank=True)
    attendence_percentage=models.FloatField(default=0.0)
    enrollment_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user.username





class Assigned(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.SET_NULL,null=True,blank=True)
    subject = models.ManyToManyField(Subject,blank=True)
    class_assigned = models.ForeignKey(ClassST,on_delete=models.SET_NULL,null=True,blank=True)


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # ForeignKey fields with null=True and blank=True to allow flexibility
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True)
    class_assigned = models.ForeignKey(ClassST, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title