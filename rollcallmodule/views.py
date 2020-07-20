from django.shortcuts import render

# Create your views here.

def r1(request):
    return render(request, 'ComparingPage.html')

def r2(request):
    return render(request, 'coursepopup.html')

def r3(request):
    return render(request, 'ExtractingComparing.html')

def r4(request):
    return render(request, 'History.html')

def r5(request):
    return render(request, 'MyAttendace.html')

def r6(request):
    return render(request, 'RollCall.html')

def r7(request):
    return render(request, 'RollCallPage.html')

def r8(request):
    return render(request, 'StudenRecord.html')
