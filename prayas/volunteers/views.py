from django.shortcuts import render
from .forms import * 
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from main.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

@require_http_methods(['GET', 'POST'])
@login_required
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
		f1 = CreateVolunteerForm()
		f2 = SearchVolunteerForm()
		data = {'addvolunteerform' : f1, 'searchvolunteerform' : f2}
		return render(request, 'volunteers/volunteer.html', data)


@require_http_methods(['GET', 'POST'])
@login_required
def searchvolunteer(request):
	if request.method == 'POST':
		searchedvolunteer = []
		data = {}
		f = SearchVolunteerForm(request.POST)
		if f.is_valid():
			name = f.cleaned_data.get('name')
			try:
				volu = volunteers.objects.filter(name__contains=name)
				data['searchedvolunteernotfound'] = 'no'
			except ObjectDoesNotExist:
				data['searchedvolunteernotfound'] = 'yes'
			if data['searchedvolunteernotfound'] == 'no':
				for volunteer in volu:
					searchedvolunteer.append(volunteer)
			data['searchedvolunteer'] = searchedvolunteer
			data['searchvolunteerform'] = f
			data['addvolunteerform'] = CreateVolunteerForm()
			return render(request, 'volunteers/volunteer.html', data)
		else:
			f1 = CreateVolunteerForm()
			f2 = SearchVolunteerForm()
			data = {'addvolunteerform' : f1, 'searchvolunteerform' : f2}
			return render(request, 'volunteers/volunteer.html', data)
	else:
		f1 = CreateVolunteerForm()
		f2 = SearchVolunteerForm()
		data = {'addvolunteerform' : f1, 'searchvolunteerform' : f2}
		return render(request, 'volunteers/volunteer.html', data)


@require_http_methods(['GET', 'POST'])
@login_required
def volunteerProfile(request, volunteer_roll_no):
	if request.method == 'GET':
		data = {}
		volu = volunteers.objects.get(collegeRollNo = volunteer_roll_no)
		data['volunteer'] = volu
		return render(request, 'volunteers/volunteerProfile.html', data)


@require_http_methods(['GET', 'POST'])
@login_required
def editVolunteer(request, volunteer_roll_no):
	u = volunteers.objects.get(collegeRollNo=volunteer_roll_no)
	if request.method == 'POST':	
		data = {}
		data['rollNo'] = volunteer_roll_no
		f = EditVolunteerForm(request.POST)
		if f.is_valid():
			u.delete()
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
		return render(request, 'volunteers/editVolunteer.html', data)
	else:
		data = {}
		f = EditVolunteerForm(user=request.user, rollNo=volunteer_roll_no, instance=u)
		data['editvolunteerform'] = f
		data['rollNo'] = volunteer_roll_no
		return render(request, 'volunteers/editVolunteer.html', data)