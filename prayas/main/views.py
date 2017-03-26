from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.contrib.auth import logout
import MySQLdb,os

@require_http_methods(['GET', 'POST'])
def handleLogin(request):
    if request.user.is_authenticated():
        return redirect('add-student')
    f = LoginForm(request.POST or None)
    # forgot = ForgetForm(request.POST or None)
    if request.method=='POST':
        nexturl = request.POST.get('next')
    if f.is_valid():
    	user = f.get_user()
    	login(request, user)
    data = {'form':f}
    return render(request,'main/login.html',data)

@require_http_methods(['GET', 'POST'])
@login_required
def handleLogout(request):	 
	logout(request)
	f = LoginForm(request.POST or None)
	data = {'form':f}
	return render(request, 'main/login.html', data)

@require_http_methods(['GET'])
def homePage(request):
    mainPa = mainPage.objects.all()[0]
    stud1 = students.objects.get(rollNo = mainPa.student1 )
    stud2 = students.objects.get(rollNo = mainPa.student2 )
    stud3 = students.objects.get(rollNo = mainPa.student3 )
    stud4 = students.objects.get(rollNo = mainPa.student4 )
    stud5 = students.objects.get(rollNo = mainPa.student5 )
    volun1 = volunteers.objects.get(collegeRollNo = mainPa.volunteer1 )
    volun2 = volunteers.objects.get(collegeRollNo = mainPa.volunteer2 )
    volun3 = volunteers.objects.get(collegeRollNo = mainPa.volunteer3 )
    volun4 = volunteers.objects.get(collegeRollNo = mainPa.volunteer4 )
    volun5 = volunteers.objects.get(collegeRollNo = mainPa.volunteer5 )
    studentNames = [stud1.name,stud2.name,stud3.name,stud4.name,stud5.name]
    volunteerNames = [volun1.name,volun2.name,volun3.name,volun4.name,volun5.name]
    data = {'studentNames':studentNames,'volunteerNames':volunteerNames,'motto':mainPa.ourMotto,'video':mainPa.videoLink}
    return render(request, 'main/home.html', data);

@require_http_methods(['GET', 'POST'])
@login_required
def manageMain(request):
    h = None
    try:
        h = mainPage.objects.all()[0]
        old = h.academicCalender.path
    except ObjectDoesNotExist:
        pass
    form = editMainForm(request.POST or None, request.FILES or None,instance = h)
    data = {'form': form}
    if form.is_valid():
        try:
            data = {'form': form}
            os.remove(old)
            new = form.save()
        except MySQLdb.Error as e:
            # print(e)
            pass
    return render(request, 'main/editMainPage.html', data)

@require_http_methods(['GET', 'POST'])
@login_required
def manageNotices(request):
    h = None
    try:
        h = notices.objects.all()[:10]
    except ObjectDoesNotExist:
        pass
    form = addNoticeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            form.save()
        except MySQLdb.Error:
            pass
    data = {'notices': h,'form': form}
    return render(request, 'main/manageNotices.html',data)


@require_http_methods(['GET'])
def notice(request,pageNo=1):
    h= None
    pageNo = int(pageNo)
    left = (pageNo-1)*10
    try:
        total = notices.objects.all().count()
        if pageNo<1:
            h = notices.objects.all()[:10]
            pageNo = 1
            left = 0
        elif total<left+1:
            h = notices.objects.all()[total-(total%10):total]
            pageNo = int(total/10+1)
            left = (int(pageNo)-1)*10
        else:
            h = notices.objects.all()[left:left+10]
        if total>(left+10):
            ifNext = True
        else:
            ifNext = False
    except ObjectDoesNotExist:
        pass
    print(pageNo)
    print(type(pageNo))
    data = {'notices': h,'next': pageNo+1,'prev': pageNo-1, 'pageNo': pageNo, 'ifNext':ifNext} 
    return render(request, 'main/allNotices.html',data)


@require_http_methods(['GET', 'POST'])
@login_required
def addEvent(request):
    h= None
    try:
        h = events.objects.all()
    except ObjectDoesNotExist:
        pass
    form = addEventForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        try:
            new = form.save()
            return HttpResponseRedirect(reverse('main:addGallery',kwargs={'pk':new.pk}))
        except MySQLdb.Error:
            pass
    data = {'eventList':h,'form':form}
    return render(request,'main/addEvent.html',data)


@require_http_methods(['GET', 'POST'])
@login_required
def addGallery(request,pk):
    photos = None
    h = None
    try:
        photos = photoGallery.objects.filter(event__pk = pk)
        h = events.objects.get(pk = pk)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('main:addGallery', kwargs={'pk':pk}))
    form = addGalleryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            new = form.save(commit = False)
            new.event = h
            new.save()
        except MySQLdb.Error:
            pass
    data = {'eventPk':pk, 'photos':photos, 'eventName':h.name, 'form':form}
    return render(request, 'main/addGallery.html',data)

@require_http_methods(['GET'])
@login_required
def removeEvent(request,pk):
    try:
        event = events.objects.get(pk = pk)
        os.remove(event.image.path)
        event.delete()
    except ObjectDoesNotExist:
        pass
    except MySQLdb.Error:
        pass
    return HttpResponseRedirect(reverse('main:addEvent'))

@require_http_methods(['GET'])
@login_required
def removeGallery(request, galleryPk):
    try:
        gallery = photoGallery.objects.get(pk = galleryPk)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('main:addEvent'))
    event = events.objects.get(photogallery__pk = galleryPk)
    try:
        os.remove(gallery.image.path)
        gallery.delete()
    except MySQLdb.Error:
        pass
    return HttpResponseRedirect(reverse('main:addGallery', kwargs={'pk':event.pk}))

@require_http_methods(['GET'])
def mainEvents(request):
    h = None
    try:
        h = events.objects.all()
    except ObjectDoesNotExist:
        pass
    data = {'events':h}
    return render(request,'main/mainEvents.html',data)

@require_http_methods(['GET'])
def mainGallery(request, pk):
    h = None
    photos = None
    try:
        h = events.objects.get(pk= pk)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('main:mainEvents'))
    try:
        photos = photoGallery.objects.filter(event = h)
    except ObjectDoesNotExist:
        pass
    data = {'eventName': h.name, 'photos': photos}
    return render(request, 'main/mainGallery.html', data)