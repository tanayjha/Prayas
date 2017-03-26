from django.db import models
from datetime import *
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

# def studenPhotoName(instance, filename):
# 	ext = filename.split('.')[-1]
# 	return 'student/images/'+instance.username+'.'+ext

class students(models.Model):
	name = models.CharField(max_length = 50,null = False)
	rollNo = models.CharField(max_length = 20,primary_key = True)
	address = models.CharField(max_length = 200,null = False)
	isActive = models.BooleanField(default = True)
	guardianName = models.CharField(max_length = 50,null = False)
	guardianPhone = models.CharField(max_length = 10,null = False)
	guardiansRelationWithChild = models.CharField(max_length = 20,null = False)
	referenceName = models.CharField(max_length = 50,null = False)
	referencePhone = models.CharField(max_length = 10,null = False)
	referenceAddress = models.CharField(max_length = 200,null = False)
	joiningDate = models.DateField(null = False,default = date.today())
	# photo = models.ImageField(upload_to = studenPhotoName, null = True)

class studentPerformance(models.Model):
	year = models.IntegerField(null = False)
	student = models.ForeignKey(students,null=False)
	percentage = models.IntegerField(null=False)

class volunteers(models.Model):
	name = models.CharField(max_length = 50)
	collegeRollNo = models.CharField(max_length = 10,primary_key = True)
	joiningDate = models.DateField(null = False,default = date.today())
	email = models.EmailField(null =False)
	contactNo = models.CharField(max_length = 10,null = False)
	# photo = models.ImageField(upload_to = volunteerPhotoName,null = False)

class volunteersAttendanceRecord(models.Model):
	date = models.DateField(null = False,default = date.today())
	volunteer = models.ForeignKey(volunteers)
	present = models.BooleanField(default = True)

class studentsAttendanceRecord(models.Model):
	date = models.DateField(null = False,default = date.today())
	student = models.ForeignKey(students)
	present = models.BooleanField(default = True)

def eventImageName(instance, filename):
	ext = filename.split('.')[-1]
	name = instance.name.replace(' ','.')
	return 'main/files/events/'+name+'.'+ext

class events(models.Model):
	name = models.CharField(max_length = 50,null = False)
	description = models.CharField(max_length = 1000,null = False)
	videoLink = models.CharField(max_length = 1000,blank = True)
	image = models.ImageField(upload_to = eventImageName,null = False)

def photoName(instance, filename):
	return 'main/files/events/gallery/'+filename

class photoGallery(models.Model):
	image = models.ImageField(upload_to = photoName,null = False)
	event = models.ForeignKey(events)

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Only pdf file format is supported')

def noticeName(instance, filename):
	ext = filename.split('.')[-1]
	desc = instance.description.replace(' ','')
	da = str(instance.uploadDate).replace(' ','')
	return 'main/files/notices/'+desc+da+'.'+ext

class notices(models.Model):
	uploadDate = models.DateField(default = date.today(),null = False)
	description = models.CharField(max_length = 200,null = False)
	pdf = models.FileField(upload_to = noticeName, validators = [validate_file_extension], null = False)

def calenderName(instance,fileName):
	ext = fileName.split('.')[-1]
	return 'main/files/academic/Academic_Calender.'+ext

class mainPage(models.Model):
	ourMotto = models.CharField(max_length = 400,null = False)
	videoLink = models.CharField(max_length = 300)
	volunteer1 = models.CharField(max_length = 20)
	volunteer2 = models.CharField(max_length = 20)
	volunteer3 = models.CharField(max_length = 20)
	volunteer4 = models.CharField(max_length = 20)
	volunteer5 = models.CharField(max_length = 20)
	student1 = models.CharField(max_length = 20)
	student2 = models.CharField(max_length = 20)
	student3 = models.CharField(max_length = 20)
	student5 = models.CharField(max_length = 20)
	student4 = models.CharField(max_length = 20)
	academicCalender = models.FileField(upload_to = calenderName, validators=[validate_file_extension], null = False)
	# Other things can be added