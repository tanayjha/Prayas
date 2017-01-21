from django.db import models
from django.utils import timezone
# Create your models here.

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
BLOOD_GROUP = (('B+','B Positive'),('A+','A Positive'),('AB+','AB Positive'),
	('A-','A Neagtive'),('B-','B Negative'),('AB-','AB Negative'),('O+','O Positive'),('O-','O Negative'))
def student_photo_name(instance, filename):
	ext = filename.split('.')[-1]
	return 'student/images/'+instance.name+'.'+ext
class Students(models.Model):
	name = models.CharField(max_length=50 , null = False, default='');
	date_of_birth = models.DateField(null=False,default=timezone.now())
	gender = models.CharField(max_length = 10, choices = GENDER_CHOICES, default = GENDER_CHOICES[0][0])
	blood_group = models.CharField(max_length=5, choices = BLOOD_GROUP, default = BLOOD_GROUP[0][0])
	student_phone_num = models.CharField(null = False, max_length=20)
	student_email = models.EmailField(null=False,unique=True)
	student_optional_phone_num = models.CharField(null = True, blank = True, max_length=20)
	father_name = models.CharField(null=False, max_length=100)
	mother_name = models.CharField(null=False, max_length=100)
	parent_email = models.EmailField(null=False)
	parent_phone_num = models.CharField(null = False, max_length=20)
	parent_optional_phone_num = models.CharField(null = True, blank = True, max_length=20)
	permanent_address = models.CharField(null=False, max_length=200)
	permanent_address_zipcode = models.IntegerField(null=False,default = 0 )
	student_photo = models.ImageField(upload_to=student_photo_name, null = False)
	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (self.name)