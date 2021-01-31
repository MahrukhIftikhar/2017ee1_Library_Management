from django.shortcuts import render,redirect
from django.db import connection
from .forms import RegisterForm,bookForm,staffForm,loanForm,pubForm,userForm
from django.contrib.auth.decorators import login_required
from web.models import BookDetails, PubDetails, UserDetails, LoanDetails, pubsDetails
from web.models import StaffDetails, usersDetails,booksDetails,loansDetails,staffsDetails,AdminDetails
from .urls import url 
from django.contrib import auth
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request,'index1.html')

def indexView(request):
    return render(request,'index.html')
def serView(request):
    return render(request,'service.html')
def abView(request):
    return render(request,'about.html')
def coView(request):
    return render(request,'contact.html')
def booksView(request):
    resultdisplay = BookDetails.objects.all()
    return render(request,'books.html',{'BookDetails':resultdisplay})
def sbookView(request):
    resultdisplay = BookDetails.objects.all()
    return render(request,'sbook.html',{'BookDetails':resultdisplay})
def bookView(request):
    resultdisplay = BookDetails.objects.all()
    return render(request,'booknad.html',{'BookDetails':resultdisplay})

def loginuser(request):
    return render(request,'userlogin.html',{'Userverify':request.user})
def staffView(request):
    result = StaffDetails.objects.all()
    return render(request,'staff.html',{'StaffDetails':result})
def userView(request):
    resultdisplay = UserDetails.objects.all()
    return render(request,'user.html',{'UserDetails':resultdisplay})
def usersView(request):
    resultdisplay = UserDetails.objects.all()
    return render(request,'suser.html',{'UserDetails':resultdisplay})
def loanView(request):
    resultdisplay = LoanDetails.objects.all()
    return render(request,'loan.html',{'LoanDetails':resultdisplay})
def pubView(request):
    resultdisplay = PubDetails.objects.all()
    return render(request,'publisher.html',{'PubDetails':resultdisplay})
@login_required(login_url='loginst.html')
def view(request):
    return render(request,'view.html')

def login(request):
    if request.method=="POST":
        try:
            userverify = UserDetails.objects.get(email_id = request.POST['email_id'],password=request.POST['password'])
            print("Username= ",userverify)
            request.session['email_id']=userverify.email_id
            return render(request,"userlogin.html",{'Username':userverify})
        except UserDetails.DoesNotExist as e:
            messages.success(request,'Username or Password is Invalid...!!!')
    return render(request,"registration/login.html")
def login1(request):
    if request.method=="POST":
        try:
            userverify1 = AdminDetails.objects.get(login_id = request.POST['email_id'],password=request.POST['password'])
            print("Username= ",userverify1)
            request.session['email_id']=userverify1.login_id
            return render(request,"index.html",{'Username':userverify1})
        except AdminDetails.DoesNotExist as e:
            messages.success(request,'Username or Password is Invalid...!!!')
    return render(request,"registration/login.html")
def login2(request):
    if request.method=="POST":
        try:
            userverify2 = StaffDetails.objects.get(SSN = request.POST['email_id'],password=request.POST['password'])
            print("Username= ",userverify2)
            request.session['email_id']=userverify2.SSN
            return render(request,"view.html",{'Username':userverify2})
        except StaffDetails.DoesNotExist as e:
            messages.success(request,'Username or Password is Invalid...!!!')
            messages.success(request,'Please enter your SSN inplace of username')
    return render(request,"registration/login.html")
def register(request):
    form = RegisterForm()
    context = {'form':form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if request.POST.get('password1') != request.POST.get('password2'):
                messages.success(request,"The New User cannot be registered. Your passwords didn't match.")
                return render(request,"register/register.html")
        if request.POST.get('SSN') and request.POST.get('username') and request.POST.get('L_name') and request.POST.get('Address') and request.POST.get('email') and request.POST.get('password1') and request.POST.get('catagery') and request.POST.get('phone_no'):
            saverec = UserDetails()
            saverec.SSN = request.POST.get('SSN')
            saverec.F_name = str(request.POST.get('username'))
            saverec.L_name = request.POST.get('L_name')
            saverec.Address = request.POST.get('Address')
            saverec.email_id = request.POST.get('email')
            saverec.password = request.POST.get('password1')
            saverec.catagery = request.POST.get('catagery') 
            saverec.phone_no = request.POST.get('phone_no')
            saverec.save()
            messages.success(request,"The New User " +saverec.F_name+ " is Registered Successfully...!!!")
            return render(request,"register/register.html")
        else:
            messages.success(request,"Form details are not filled correctly. Or the password entered is not fullfilling the requirement(too short or too similar to your username)")
    return render(request,'register/register.html',context)
def ebView(request,ISNB):
    resultdisplay = BookDetails.objects.get(ISNB=ISNB)
    return render(request,'editbook.html',{'BookDetails':resultdisplay})
def updatebook(request,ISNB):
    result = BookDetails.objects.get(ISNB=ISNB)
    form = bookForm(request.POST,instance= result)
    if form.is_valid:
        form.save()
        messages.success(request,'Record Updated Successfully...!!!')
        return render(request,'editbook.html',{'BookDetails':result})
def dbView(request,ISNB):
    resultdisplay = BookDetails.objects.get(ISNB=ISNB)
    resultdisplay.delete()
    result = BookDetails.objects.all()
    return render(request,'books.html',{'BookDetails':result})
def dsView(request,SSN):
    resultdisplay = StaffDetails.objects.get(SSN=SSN)
    resultdisplay.delete()
    result = StaffDetails.objects.all()
    return render(request,'staff.html',{'StaffDetails':result})
def dpView(request,ID):
    resultdisplay = PubDetails.objects.get(ID=ID)
    resultdisplay.delete()
    result = PubDetails.objects.all()
    return render(request,'publisher.html',{'PubDetails':result})
def duView(request,SSN):
    resultdisplay = UserDetails.objects.get(SSN=SSN)
    resultdisplay.delete()
    result = UserDetails.objects.all()
    return render(request,'user.html',{'UserDetails':result})
def dlView(request,SSN,ISNB):
    resultdisplay = LoanDetails.objects.get(SSN=SSN,ISNB=ISNB)
    resultdisplay.delete()
    result = LoanDetails.objects.all()
    return render(request,'loan.html',{'LoanDetails':result})
def esView(request,SSN):
    resultdisplay = StaffDetails.objects.get(SSN=SSN)
    return render(request,'editstaff.html',{'StaffDetails':resultdisplay})
def updatestaff(request,SSN):
    result = StaffDetails.objects.get(SSN=SSN)
    form = staffForm(request.POST,instance= result)
    if form.is_valid:
        form.save()
        messages.success(request,'Record Updated Successfully...!!!')
        return render(request,'editstaff.html',{'StaffDetails':result})
def elView(request,SSN,ISNB):
    resultdisplay = LoanDetails.objects.get(SSN=SSN,ISNB=ISNB)
    return render(request,'editloan.html',{'LoanDetails':resultdisplay})
def updateloan(request,SSN,ISNB):
    result = LoanDetails.objects.get(SSN=SSN,ISNB=ISNB)
    form = loanForm(request.POST,instance= result)
    if form.is_valid:
        form.save()
        messages.success(request,'Record Updated Successfully...!!!')
        return render(request,'editloan.html',{'LoanDetails':result})
def epView(request,ID):
    resultdisplay = PubDetails.objects.get(ID=ID)
    return render(request,'editpub.html',{'PubDetails':resultdisplay})
def updatepub(request,ID):
    result = PubDetails.objects.get(ID=ID)
    form = pubForm(request.POST,instance= result)
    if form.is_valid:
        form.save()
        messages.success(request,'Record Updated Successfully...!!!')
        return render(request,'editpub.html',{'PubDetails':result})
def euView(request,SSN):
    resultdisplay = UserDetails.objects.get(SSN=SSN)
    return render(request,'edituser.html',{'UserDetails':resultdisplay})
def updateuser(request,SSN):
    result = UserDetails.objects.get(SSN=SSN)
    form = userForm(request.POST,instance= result)
    if form.is_valid:
        form.save()
        messages.success(request,'Record Updated Successfully...!!!')
        return render(request,'edituser.html',{'UserDetails':result})
def useradd(request):
    if request.method=="POST":
        if request.POST.get('SSN') and request.POST.get('F_name') and request.POST.get('L_name') and request.POST.get('Address') and request.POST.get('email_id') and request.POST.get('password') and request.POST.get('catagery') and request.POST.get('phone_no'):
            saverec = usersDetails()
            saverec.SSN = request.POST.get('SSN')
            saverec.F_name = request.POST.get('F_name')
            saverec.L_name = request.POST.get('L_name')
            saverec.Address = request.POST.get('Address')
            saverec.email_id = request.POST.get('email_id')
            saverec.password = request.POST.get('password') 
            saverec.catagery = request.POST.get('catagery') 
            saverec.phone_no = request.POST.get('phone_no')
            cursor = connection.cursor()
            cursor.execute("call project('"+saverec.SSN+"','"+saverec.F_name+"','"+saverec.L_name+"','"+saverec.Address+"','"+saverec.email_id+"','"+saverec.password+"','"+saverec.catagery+"','"+saverec.phone_no+"')")
            messages.success(request,"The user "+saverec.F_name+ " is added successfully...!!!")
            return render(request,"adduser.html")
    else:
        return render(request,"adduser.html")
def bookadd(request):
    if request.method=="POST":
        if request.POST.get('ISNB') and request.POST.get('price') and request.POST.get('noofcopies') and request.POST.get('title') and request.POST.get('edition') and request.POST.get('author') and request.POST.get('pbid') and request.POST.get('status') and request.POST.get('catagery'):
            saverec = booksDetails()
            saverec.ISNB = request.POST.get('ISNB')
            saverec.price = request.POST.get('price')
            saverec.noofcopies = request.POST.get('noofcopies')
            saverec.title = request.POST.get('title')
            saverec.edition = request.POST.get('edition')
            saverec.author = request.POST.get('author') 
            saverec.pbid = request.POST.get('pbid')
            saverec.status = request.POST.get('status')
            saverec.catagery = request.POST.get('catagery') 
            cursor = connection.cursor()
            cursor.execute("call addbook('"+saverec.ISNB+"','"+saverec.price+"','"+saverec.noofcopies+"','"+saverec.title+"','"+saverec.edition+"','"+saverec.author+"','"+saverec.pbid+"','"+saverec.status+"','"+saverec.catagery+"')")
            messages.success(request,"The Book "+saverec.title+ " is Added Successfully...!!!")
            return render(request,"addbook.html")
    else:
        return render(request,"addbook.html")
def loanadd(request):
    if request.method=="POST":
        if request.POST.get('SSN') and request.POST.get('ISNB') and request.POST.get('issue_date') and request.POST.get('return_date') and request.POST.get('fine'):
            saverec = loansDetails()
            saverec.SSN = request.POST.get('SSN')
            saverec.ISNB = request.POST.get('ISNB')
            saverec.issue_date = request.POST.get('issue_date')
            saverec.return_date = request.POST.get('return_date')
            saverec.fine = request.POST.get('fine')
            cursor = connection.cursor()
            cursor.execute("call addloan('"+saverec.SSN+"','"+saverec.ISNB+"','"+saverec.issue_date+"','"+saverec.return_date+"','"+saverec.fine+"')")
            messages.success(request,"The Loan for the person "+saverec.SSN+ "and for the book "+saverec.ISNB+" is Added Successfully...!!!")
            return render(request,"addloan.html")
    else:
        return render(request,"addloan.html")

def lend(request):
    if request.method=="POST":
        if request.POST.get('SSN') and request.POST.get('ISNB') and request.POST.get('issue_date') and request.POST.get('return_date'):
            saverec = loansDetails()
            saverec.SSN = request.POST.get('SSN')
            saverec.ISNB = request.POST.get('ISNB')
            saverec.issue_date = request.POST.get('issue_date')
            saverec.return_date = request.POST.get('return_date')
            userverify = BookDetails.objects.get(ISNB = request.POST['ISNB'])
            if userverify.status=="booked":
                messages.success(request,'You cannot lend this book as it is already occupied')
                return render(request,'lendbook.html')
            saverec.fine = str(userverify.price)
            cursor = connection.cursor()
            cursor.execute("call addloan('"+saverec.SSN+"','"+saverec.ISNB+"','"+saverec.issue_date+"','"+saverec.return_date+"','"+saverec.fine+"')")
            messages.success(request,"The person "+saverec.SSN+ "has lended the book "+saverec.ISNB+" Successfully...!!!")
            return render(request,"lendbook.html")
    else:
        return render(request,"lendbook.html") 
def slend(request):
    if request.method=="POST":
        if request.POST.get('SSN') and request.POST.get('ISNB') and request.POST.get('issue_date') and request.POST.get('return_date'):
            saverec = loansDetails()
            saverec.SSN = request.POST.get('SSN')
            saverec.ISNB = request.POST.get('ISNB')
            saverec.issue_date = request.POST.get('issue_date')
            saverec.return_date = request.POST.get('return_date')
            userverify = BookDetails.objects.get(ISNB = request.POST['ISNB'])
            if userverify.status=="booked":
                messages.success(request,'You cannot lend this book as it is already occupied')
                return render(request,'slend.html')
            saverec.fine = str(userverify.price)
            cursor = connection.cursor()
            cursor.execute("call addloan('"+saverec.SSN+"','"+saverec.ISNB+"','"+saverec.issue_date+"','"+saverec.return_date+"','"+saverec.fine+"')")
            messages.success(request,"The person "+saverec.SSN+ "has lended the book "+saverec.ISNB+" Successfully...!!!")
            return render(request,"slend.html")
    else:
        return render(request,"slend.html")     
def staffadd(request):
    if request.method=="POST":
        if request.POST.get('SSN') and request.POST.get('F_name') and request.POST.get('L_name') and request.POST.get('Address') and request.POST.get('salary') and request.POST.get('specified_task'):
            saverec = staffsDetails()
            saverec.SSN = request.POST.get('SSN')
            saverec.F_name = request.POST.get('F_name')
            saverec.L_name = request.POST.get('L_name')
            saverec.Address = request.POST.get('Address')
            saverec.salary = request.POST.get('salary')
            saverec.specified_task = request.POST.get('specified_task') 
            saverec.password = request.POST.get('password') 
            cursor = connection.cursor()
            cursor.execute("call addstaff('"+saverec.SSN+"','"+saverec.F_name+"','"+saverec.L_name+"','"+saverec.Address+"','"+saverec.salary+"','"+saverec.specified_task+"','"+saverec.password+"')")
            messages.success(request,"The Staff "+saverec.F_name+ " is Added Successfully...!!!")
            return render(request,"addstaff.html")
    else:
        return render(request,"addstaff.html")
def pubadd(request):
    if request.method=="POST":
        if request.POST.get('ID') and request.POST.get('Name') and request.POST.get('pub_year'):
            saverec = pubsDetails()
            saverec.ID = request.POST.get('ID')
            saverec.Name = request.POST.get('Name')
            saverec.pub_year = request.POST.get('pub_year')
            cursor = connection.cursor()
            cursor.execute("call addpub('"+saverec.ID+"','"+saverec.Name+"','"+saverec.pub_year+"')")
            messages.success(request,"The Publisher "+saverec.Name+ " is Added Successfully...!!!")
            return render(request,"addpub.html")
    else:
        return render(request,"addpub.html")
def emailsend(request):
    subject = "Updates about Library Management System"
    message = "Thanks for Checking out our website Library Management System. You will get updates about our app. Thank you so much. Regards Admin"
    sendfrom = 'settings.EMAIL_HOST_USER'
    c_email = ['mahrukhiftikhar1999@gmail.com']
    send_mail(subject,message,sendfrom,c_email)
    return render(request,"dashboard.html",{'message_name':c_email})
def contact(request):
    if request.method == "POST":
        message_name = request.POST['contact_name'] 
        message_email = request.POST['contact_email']
        message = request.POST['contact_message']
        send_mail(message_name,message,message_email,['2017ee1@student.uet.edu.pk'])
        return render(request,'dashboard.html',{'message_name':message_name})
    else:
        return render(request,'dashboard.html')

