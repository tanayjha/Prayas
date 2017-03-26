from django.shortcuts import render
from .forms import * 
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from main.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

@require_http_methods(['GET', 'POST'])
@login_required
def addstudent(request):
	if request.method == 'POST':
		f = CreateStudentForm(request.POST)
		if f.is_valid():
			# print ("HERE")
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
			# print ("ELSE")
			data = {'addstudentform' : f}
			#return redirect('127.0.0.1:8000/warden/student#add')
			return render(request, 'students/student.html', data)
	else:
		# print ("NOW")
		f = CreateStudentForm()
		data = {'addstudentform' : f}
		return render(request, 'students/student.html', data)


@require_http_methods(['GET', 'POST'])
@login_required
def searchstudent(request):
	if request.method == 'POST':
		searchedstudent = []
		data = {}
		f = SearchStudentForm(request.POST)
		if f.is_valid():
			name = f.cleaned_data.get('name')
			try:
				stu = students.objects.filter(name__contains=name)
				data['searchedstudentnotfound'] = 'no'
			except ObjectDoesNotExist:
				data['searchedstudentnotfound'] = 'yes'
			if data['searchedstudentnotfound'] == 'no':
				for student in stu:
					searchedstudent.append(student)
			data['searchedstudent'] = searchedstudent
			data['searchstudentform'] = f
			return render(request, 'students/searchstudent.html', data)
		else:
			f = SearchStudentForm()
			data = {'searchstudentform' : f}
			return render(request, 'students/searchstudent.html', data)
	else:
		f = SearchStudentForm()
		data = {'searchstudentform' : f}
		return render(request, 'students/searchstudent.html', data)


@require_http_methods(['GET', 'POST'])
@login_required
def studentProfile(request, student_rollNo):
	if request.method == 'GET':
		data = {}
		stu = students.objects.get(rollNo = student_rollNo)
		data['student'] = stu
		return render(request, 'students/studentProfile.html', data)


@require_http_methods(['GET', 'POST'])
@login_required
def editStudent(request, student_rollNo):
	u = students.objects.get(rollNo=student_rollNo)
	if request.method == 'POST':
		data = {}
		data['rollNo'] = student_rollNo
		f = EditStudentForm(request.POST)
		if f.is_valid():
			u.delete()
			# print ("HERE")
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
		return render(request, 'students/editStudent.html', data)
	else:
		data = {}
		f = EditStudentForm(user=request.user, rollNo=student_rollNo, instance=u)
		data['editstudentform'] = f
		data['rollNo'] = student_rollNo
		return render(request, 'students/editStudent.html', data)

