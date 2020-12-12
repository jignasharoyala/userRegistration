from django.shortcuts import render, redirect
from userRegistrationApp.forms import UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from userRegistrationApp.models import UserProfileDetails, Email
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):
    try:
        if not 'user_id' in request.session:
            return render(request, 'userRegistrationApp/login.html', {})
        else:

            user = UserProfileDetails.objects.filter(user_id=request.session['user_id'])
            return render(request,'userRegistrationApp/index.html',{
                               'user':user,})
        
    except Exception as e:
        return render(request, 'userRegistrationApp/login.html', {})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    request.session.flush()
    logout(request)
    return render(request, 'userRegistrationApp/login.html', {})

def register(request):
    try:
        registered = False
        if request.method == 'POST':
            profile_form = UserProfileInfoForm(data=request.POST)
            if  profile_form.is_valid():
                Registration_data = UserProfileDetails.objects.create(
                    user_name = request.POST['user_name'],
                    user_email1 = request.POST['user_email1'],
                    user_email2 = request.POST['user_email2'],
                
                    user_password = request.POST['user_password'],
                    user_location = get_client_ip(request)
                    
                    )

                Registration_data.save()
                
                registered = True
            else:
                print(user_form.errors,profile_form.errors)
        else:
            profile_form = UserProfileInfoForm()
        return render(request,'userRegistrationApp/registration.html',
                              {'profile_form':profile_form,
                               'registered':registered})
        
    except Exception as e:

        return render(request,'userRegistrationApp/registration.html')
        

def user_login(request):
    try:
        
        if not 'user_id' in request.session:
            return render(request, 'userRegistrationApp/login.html', {})
        else:
            if request.method == 'POST':

                user =  UserProfileDetails.objects.filter(Q(user_email1=request.POST['user_email']) | Q(user_email2=request.POST['user_email']), user_password=request.POST['password'])
                if user:
                    
                    if user[0].user_role == "Admin":
                
                        primary_email = Email.objects.filter(user_id_id=user[0].user_id)
                      
                        if primary_email[0].email == request.POST['user_email'] and primary_email[0].primary == True:

                                request.session['user_id'] = user[0].user_id
                                UserProfileDetails.objects.filter(user_id=user[0].user_id).update(login_failed_count=0)
                                return render(request,'userRegistrationApp/index.html',{
                                           'user':user,})
                        else:
                            failed_counter = UserProfileDetails.objects.filter(user_id=user[0].user_id).values_list('login_failed_count',flat=True)
                            if failed_counter >= 3:
                                UserProfileDetails.objects.filter(user_id=user[0].user_id).update(login_failed_count=failed_counter+1)
                                return HttpResponse("Invalid login details given")
                            else:
                                UserProfileDetails.objects.filter(user_id=user[0].user_id).update(login_failed_count=0)
                                return HttpResponse("Invalid login details given")

                    else:

                        return redirect('adminView')
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(request.POST['user_email'],request.POST['password']))
                    return HttpResponse("Invalid login details given")
            else:
                return render(request, 'userRegistrationApp/login.html', {})
    except Exception as e:
        
        return render(request, 'userRegistrationApp/login.html', {})



def set_primary_email(request):
    try:
        if request.method == 'POST':

            user = UserProfileDetails.objects.filter(user_id=request.POST['user_id']).first()
            Email.objects.update_or_create(user_id=user, email=request.POST['user_email'], primary=True)
        
            user =  UserProfileDetails.objects.filter(user_id=request.POST['user_id'])
            return render(request,'userRegistrationApp/index.html',{
                               'user':user,})
        else:
            return render(request, 'userRegistrationApp/index.html', {})
        
    except Exception as e:
        return render(request, 'userRegistrationApp/index.html', {})

def upload_file(request):

    if not 'User_id' in request.session:
        return render(request, 'userRegistrationApp/login.html', {})
    else:
        try:
            if request.method == 'POST': 
                UserProfileDetails.objects.filter(user_id=request.POST['user_id']).update(user_file=request.FILES['user_file'])
            
                user =  UserProfileDetails.objects.filter(user_id=request.POST['user_id'])
                return render(request,'userRegistrationApp/index.html',{
                                   'user':user,})
            else:
                return render(request, 'userRegistrationApp/index.html', {})
            
        except Exception as e:
            return render(request,'userRegistrationApp/index.html')
           


def replay_to_comment(request):
    try:
        if not 'user_id' in request.session:
            return render(request, 'userRegistrationApp/login.html', {})
        else:
            if request.method == 'POST':
                UserProfileDetails.objects.filter(user_id=request.POST['user_id']).update(user_replay=request.POST['user_replay'])
                user = UserProfileDetails.objects.filter(user_id=request.POST['user_id'])
                return render(request,'userRegistrationApp/index.html',{
                                   'user':user,})
        
    except Exception as e:
        return render(request,'userRegistrationApp/index.html')


def get_client_ip(request):
    try:
        from django.contrib.gis.utils import GeoIP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        g = GeoIP()
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            city = g.city(ip)['city']
        else:
            ip = request.META.get('REMOTE_ADDR')
            city = g.city(ip)['city']
        return city
        
    except Exception as e:
        return "xyz"


def adminView(request):
    try:
        if not 'user_id' in request.session:
            return render(request, 'userRegistrationApp/login.html', {})
        else:
            if request.method == 'GET':       
                userRegData = UserProfileDetails.objects.all()   
                print(userRegData)         
                return render(request, 'userRegistrationApp/admin.html', {'userRegData': userRegData })
        
    except Exception as e:
        return render(request,'userRegistrationApp/login.html')

def adminAddNote(request):
    try:
        if not 'user_id' in request.session:
            return render(request, 'userRegistrationApp/login.html', {})
        else:
            if request.method == 'POST':
                UserProfileDetails.objects.filter(user_id=request.POST['user_id']).update(addmin_comment=request.POST['addmin_comment'])
                userRegData = UserProfileDetails.objects.all()
                return redirect('adminView')
        
    except Exception as e:
        return render(request,'userRegistrationApp/login.html')