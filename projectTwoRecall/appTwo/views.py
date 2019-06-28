from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from appTwo.models import userProfile
from appTwo.forms import userProfileForm, userForm


# loginImports
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'appTwo/index.html')


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def userLogin(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if(user):
            if(user.is_active):
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('<h2>User is not active</h2>')
        else:
            return HttpResponse('<h2>Invalid username or password</h2>')
    else:
        return render(request, 'appTwo/login.html')


def registeration(request):
    registered = False
    userF = userForm()
    profileForm = userProfileForm()
    if(request.method == 'POST'):
        userF = userForm(request.POST)
        profileForm = userProfileForm(request.POST)
        if(profileForm.is_valid() and userF.is_valid()):
            user = userF.save()
            user.set_password(user.password)
            user.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            if('profilePic' in request.FILES):
                profile.profilePic = request.FILES['profilePic']
            profile.save()
            registered = True
        else:
            print(profileForm.errors)
    myDict={
        'registered':registered,
        'userF':userF,
        'profileForm':profileForm,
    }
    return render(request, 'appTwo/userForms.html', myDict)




# def users(request):
#     U = Users.objects.all().order_by('name')
#     myDict = {
#         'userData':U
#     }
#     return render(request, 'appTwo/users.html', context=myDict)
#
#
# def userForms(request):
#     F = userForm()
#
#     myDict = {
#         'userForm':F
#     }
#
#     if(request.method == 'POST'):
#         F = userForm(request.POST)
#         if(F.is_valid()):
#             name = F.cleaned_data['name']
#             email = F.cleaned_data['email']
#             comment = F.cleaned_data['comment']
#             print('\nData Recieved : ')
#             print('name : '+ name)
#             print('email : '+ email)
#             print('comment : '+ comment)
#             Users.objects.get_or_create(name=name, email=email, comment=comment)[0].save()
#             print('\nThis Data has been stored in DB...')
#     else:
#         print('Method is not POST')
#
#     return render(request, 'appTwo/userForms.html', myDict)
#
#
# def userModelForms(request):
#     MF = userModelForm()
#
#     myDict = {
#         'userModelForm':MF
#     }
#
#     if(request.method == 'POST'):
#
#         MF = userModelForm(request.POST)
#
#         if(MF.is_valid()):
#
#             MF.save()
#             return users(request)
#
#         else:
#
#             print('\nForm Data is Not Valid\n')
#             print('\n'+ str(MF.errors) +'\n')
#             myDict['validationError'] = str(MF.errors)
#
#     return render(request, 'appTwo/userForms.html', myDict)
