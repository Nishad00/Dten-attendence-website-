from django.db import models
#remaining 
   # str methods in all the classes to return the maina attributes of that file

#commands for migrations when an change is made 
# python manage.py makemigrations
# python manage.py migrate

#model for person - This is used for both the student as well as teacher 
class Person(models.Model):
    id_person = models.CharField(max_length=100, default='SOME STRING')
    name = models.CharField(max_length=100, default='SOME STRING')#common attributes
    surname = models.CharField(max_length=100, default='SOME STRING')
    mailid = models.CharField(max_length=100, default='SOME STRING')
    college = models.CharField(max_length=100, default='SOME STRING')
    profession = models.CharField(max_length=100, default='SOME STRING')
    department = models.CharField(max_length=100, default='SOME STRING')#uncommon attributes 
    division = models.CharField(max_length=100, default='SOME STRING')
    password = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.id_person + ". " + self.mailid + " = " + self.profession    

#model for subject 
class Subject(models.Model):
    id_subject = models.CharField(max_length=100, default='SOME STRING')
    department = models.CharField(max_length=100, default='SOME STRING') 
    division = models.CharField(max_length=100, default='SOME STRING')
    name = models.CharField(max_length=100, default='SOME STRING')
    creator = models.CharField(max_length=100, default='SOME STRING')
    type_of_subject = models.CharField(max_length=100, default='SOME STRING')
    batch = models.CharField(max_length=100, default='SOME STRING')
    total_l_or_p = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return   self.name +" : "+ self.division +" : "+ self.department     


#model for division
class Division(models.Model):
    id_division = models.CharField(max_length=100, default='SOME STRING')
    department = models.CharField(max_length=100, default='SOME STRING')
    name = models.CharField(max_length=100, default='SOME STRING')
    enrol_key = models.CharField(max_length=100, default='SOME STRING')
    creator = models.CharField(max_length=100, default='SOME STRING')
    total_students = models.CharField(max_length=100, default='SOME STRING')
    division_dict = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.department + " : " + self.name    

#model for batches in divisions 
class batch(models.Model):
    id_batch = models.CharField(max_length=100, default='SOME STRING')
    department = models.CharField(max_length=100, default='SOME STRING')
    division = models.CharField(max_length=100, default='SOME STRING')
    name = models.CharField(max_length=100, default='SOME STRING')
    start_roll_no = models.CharField(max_length=100, default='SOME STRING')
    end_roll_no = models.CharField(max_length=100, default='SOME STRING')

#model for attendance sheet
class Attend(models.Model):
    id_attend = models.CharField(max_length=100, default='SOME STRING')
    attend_serial_no = models.CharField(max_length=100, default='SOME STRING')# to serialize to find out percentage , we can loop sheets by using this attriute
#   will be unique in just one subject
    department = models.CharField(max_length=100, default='SOME STRING')
    division = models.CharField(max_length=100, default='SOME STRING')
    Subject = models.CharField(max_length=100, default='SOME STRING')
    batch = models.CharField(max_length=100, default='SOME STRING')
    date = models.CharField(max_length=100, default='SOME STRING')
    time = models.CharField(max_length=100, default='SOME STRING')
    present_list = models.CharField(max_length=100, default='SOME STRING')
    absent_list = models.CharField(max_length=100, default='SOME STRING')
        
    

# ------- This mind not be used ------------------------
class Student(models.Model):
    college = models.CharField(max_length=100, default='SOME STRING')
    department = models.CharField(max_length=100, default='SOME STRING')
    profession = models.CharField(max_length=100, default='SOME STRING')
    division = models.CharField(max_length=100, default='SOME STRING')