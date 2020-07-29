from django.shortcuts import render,HttpResponseRedirect
from usermgnt.models import User


# Create your views here.
#def UserType(request):
 #   return render(request,'Index.html')

def AdminLogin(request):
    #userform=UsermgntForm()
    #context={'userform':userform}
    return render(request,'AdminLoginPage.html')#,context

def StudLogin(request):
    #userform = UsermgntForm()
    #context = {'userform': userform}
    return render(request,'StudentLoginPage.html')#,context

def SLoginAction(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password)
        if len(user) > 0:
            request.session['username'] = user[0].username
            request.session['userid'] = user[0].userid
            return render(request, 'MyAttendancePage.html')
        else:
            return HttpResponseRedirect('/usermgnt/student')
    # else:
    #     return HttpResponseRedirect('/users/AdminLoginPage')


def Slogout(request):
    del request.session['username']
    del request.session['userid']
    return HttpResponseRedirect('/usermgnt/student')

def ALoginAction(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password)
        if len(user) > 0:
            request.session['username'] = user[0].username
            request.session['userid'] = user[0].userid
            return render(request, 'RollCall.html')
        else:
            return HttpResponseRedirect('/usermgnt/admin')
    else:
        return HttpResponseRedirect('/users/AdminLoginPage')


def Alogout(request):
    del request.session['username']
    del request.session['userid']
    return HttpResponseRedirect('/usermgnt/admin')