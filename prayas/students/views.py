from django.shortcuts import render
from .forms import * 
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from main.models import *

@require_http_methods(['GET', 'POST'])
def addstudent(request):
	if request.method == 'POST':
		f = CreateStudentForm(request.POST)
		if f.is_valid():
			print ("HERE")
			name = f.cleaned_data.get('name')
			rollNo = f.cleaned_data.get('rollNo')
			address = f.cleaned_data.get('address')
			isActive = f.cleaned_data.get('isActive')
			guardianName = f.cleaned_data.get('guardianName')
			guardianPhone = f.cleaned_data.get('guardianPhone')
			guardiansRelationWithChild = f.cleaned_data.get('guardiansRelationWithChild')
			referenceName = f.cleaned_data.get('referenceName')
			referencePhone = f.cleaned_data.get('referencePhone')
			referenceAddress = f.cleaned_data.get('referenceAddress')
			joiningDate = f.cleaned_data.get('joiningDate')


			s = students(name=name, rollNo=rollNo, address=address,
						 isActive=isActive, guardianName=guardianName, guardianPhone=guardianPhone,
						 guardiansRelationWithChild=guardiansRelationWithChild, referenceName=referenceName,
						 referencePhone=referencePhone, referenceAddress=referenceAddress, joiningDate=joiningDate)
			# user = MyUser.objects.create_user(f.cleaned_data.get(
			# 	'username'), datetime.now(), pas)
			s.save()
			data = {'form' : f}
			# user.save()
			return render(request, 'students/student.html', data)
		else:
			print ("ELSE")
			data = {'addstudentform' : f}
			#return redirect('127.0.0.1:8000/warden/student#add')
			return render(request, 'students/student.html', data)
	else:
		print ("NOW")
		f = CreateStudentForm()
		data = {'addstudentform' : f}
		return render(request, 'students/student.html', data)
	