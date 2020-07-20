from django.shortcuts import render

# Create your views here.
#def UserType(request):
 #   return render(request,'Index.html')

def AdminLogin(request):
    return render(request,'AdminLoginPage.html')

def StudLogin(request):
    return render(request,'StudentLoginPage.html')

def ALoginAction(request):
    if request.method=="POST":
        username =request.POST.get("username")
        password =request.POST.get("userpwd")
        print(username)
        print(password)
        return render(request,'RollCall.html')

def SLoginAction(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("userpwd")
        print(username)
        print(password)
        return render(request,'MyAttendancePage.html')