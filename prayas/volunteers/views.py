from django.shortcuts import render
from .forms import * 
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from main.models import *
from django.core.exceptions import ObjectDoesNotExist

@require_http_methods(['GET', 'POST'])
def addvolunteer(request):
	if request.method == 'POST':
		f = CreateVolunteerForm(request.POST)
		if f.is_valid():
			# print ("HERE")
			name = f.cleaned_data.get('name')
			collegeRollNo = f.cleaned_data.get('collegeRollNo')
			joiningDate = f.cleaned_data.get('joiningDate')
			email = f.cleaned_data.get('email')
			contactNo = f.cleaned_data.get('contactNo')
			
			v = volunteers(name=name, collegeRollNo=collegeRollNo, joiningDate=joiningDate, email=email,
							contactNo=contactNo)
			# user = MyUser.objects.create_user(f.cleaned_data.get(
			# 	'username'), datetime.now(), pas)
			v.save()
			data = {'form' : f}
			# user.save()
			return render(request, 'volunteers/volunteer.html', data)
		else:
			# print ("ELSE")
			data = {'addvolunteerform' : f}
			#return redirect('127.0.0.1:8000/warden/student#add')
			return render(request, 'volunteers/volunteer.html', data)
	else:
		# print ("NOW")
		f = CreateVolunteerForm()
		data = {'addvolunteerform' : f}
		return render(request, 'volunteers/volunteer.html', data)


@require_http_methods(['GET', 'POST'])
def searchvolunteer(request):
	if request.method == 'POST':
		searchedvolunteer = []
		data = {}
		f = SearchVolunteerForm(request.POST)
		if f.is_valid():
			name = f.cleaned_data.get('name')
			try:
				volu = volunteers.objects.filter(name=name)
				data['searchedvolunteernotfound'] = 'no'
			except ObjectDoesNotExist:
				data['searchedvolunteernotfound'] = 'yes'
			if data['searchedvolunteernotfound'] == 'no':
				for volunteer in volu:
					searchedvolunteer.append(volunteer)
			data['searchedvolunteer'] = searchedvolunteer
			data['searchvolunteerform'] = f
			return render(request, 'volunteers/searchvolunteer.html', data)
		else:
			f = SearchVolunteerForm()
			data = {'searchvolunteerform' : f}
			return render(request, 'volunteers/searchvolunteer.html', data)
	else:
		f = SearchVolunteerForm()
		data = {'searchvolunteerform' : f}
		return render(request, 'volunteers/searchvolunteer.html', data)


@require_http_methods(['GET', 'POST'])
def volunteerProfile(request, volunteer_roll_no):
	if request.method == 'GET':
		data = {}
		volu = volunteers.objects.get(collegeRollNo = volunteer_roll_no)
		data['volunteer'] = volu
		return render(request, 'volunteers/volunteerProfile.html', data)
