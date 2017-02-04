from django.shortcuts import render
from .forms import * 
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@require_http_methods(['GET', 'POST'])
def addstudent(request):
	if request.method == 'POST':
		f = CreateStudentForm()
		if f.is_valid():
			name = self.cleaned_data.get('name')
			rollNo = self.cleaned_data.get('rollNo')
			address = self.cleaned_data.get('address')
			isActive = self.cleaned_data.get('isActive')
			guardianName = self.cleaned_data.get('guardianName')
			guardianPhone = self.cleaned_data.get('guardianPhone')
			guardiansRelationWithChild = self.cleaned_data.get('guardiansRelationWithChild')
			referenceName = self.cleaned_data.get('referenceName')
			referencePhone = self.cleaned_data.get('referencePhone')
			referenceAddress = self.cleaned_data.get('referenceAddress')
			joiningDate = self.cleaned_data.get('joiningDate')


			s = Students(name=name, rollNo=rollNo, address=address,
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
			data = {'addstudentform' : f}
			#return redirect('127.0.0.1:8000/warden/student#add')
			return render(request, 'students/student.html', data)
	else:
		f = CreateStudentForm()
		data = {'addstudentform' : f}
		return render(request, 'students/student.html', data)
	