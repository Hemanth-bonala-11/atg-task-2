from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from swasthcare.models import Contact,Details,Blogs,Draft
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'swasthcare/home.html')
def about(request):
    return render(request,"swasthcare/about.html")
def doctor_login(request):
    return render(request,"swasthcare/doctor_login.html")
def doctor_login_after_signup(request):
    if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name")
        dp=request.FILES.get("profile_pic")
        username=request.POST.get("username")
        mailid=request.POST.get("mailid")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        street=request.POST.get("addressLine1")
        city=request.POST.get("city")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        if confirm_password!=password:
            context = {
                'message': "Enter same password in confirm passwordrd field"
            }
            return render(request,"swasthcare/doctor_signup.html",context)
        else:
            obj=Details(first_name=firstname,last_name=lastname,profile_pic=dp,
                        username=username,mailid=mailid,password=password,
                        lane1=street,city=city,state=state,pincode=pincode,
                        type="Doctor")
            if len(Details.objects.filter(username=username))==0:
                user = User.objects.create_user(username=username, email=mailid, password=password)
                obj.save()
            else:
                context = {

                'message': "Username already exists"

                }
                return render(request, "swasthcare/doctor_signup.html", context)

    return render(request,"swasthcare/doctor_login.html")
def patient_login_after_signup(request):
    if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name")
        dp=request.FILES.get("profile_pic")
        username=request.POST.get("username")
        mailid=request.POST.get("mailid")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        street=request.POST.get("addressLine1")
        city=request.POST.get("city")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        if confirm_password!=password:
            context = {
                'message': "Enter same password in confirm passwordrd field"
            }
            return render(request,"swasthcare/doctor_signup.html",context)
        else:
            obj=Details(first_name=firstname,last_name=lastname,profile_pic=dp,
                        username=username,mailid=mailid,password=password,
                        lane1=street,city=city,state=state,pincode=pincode,
                        type="patient")
            if len(Details.objects.filter(username=username))==0:
                obj.save()
                user=User.objects.create_user(username=username,email=mailid,password=password)
            else:
                context = {

                'message': "Username already exists"

                }
                return render(request, "swasthcare/patient_signup.html", context)

    return render(request,"swasthcare/patient_login.html")
def patient_login(request):
    return render(request,'swasthcare/patient_login.html')
def contact(request):
    return render(request,"swasthcare/contact.html")
def success_contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("mailid")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        obj=Contact(name=name,email=email,
                    phone_no=phone,message=message,date=datetime.today())
        obj.save()
    return render(request,"swasthcare/contact_success.html")
def doctor_signup(request):
    return render(request,'swasthcare/doctor_signup.html')
def patient_signup(request):
    return render(request,"swasthcare/patient_signup.html")
def patient_dashboard(request):
    if request.method=="POST":
        user_name=request.POST.get("Username")
        password=request.POST.get("Password")
    user = authenticate(username=user_name, password=password)
    if user is not None:
        details=Details.objects.filter(username=user_name)

        if details[0].type=="patient":
            login(request,user)

        else:
            context={
                    "message":"Entered wrong credentials"
                }
            return render(request,"swasthcare/patient_login.html",context)
        context={
                'details':details
            }
        return render(request,"swasthcare/dashboard.html",context)

    else:
        return redirect("/patient_signup")
def doctor_dashboard(request):
    if request.method=="POST":
        user_name=request.POST.get("Username")
        password=request.POST.get("Password")
    user = authenticate(username=user_name, password=password)
    if user is not None:

        details=Details.objects.filter(username=user_name)
        drafts=Draft.objects.filter(username=user_name)
        if details[0].type=="Doctor":
            login(request,user)

        else:
            context={
                    "message":"Entered wrong credentials"
                }
            return render(request,"swasthcare/doctor_login.html",context=context)
        if len(drafts)!=0:
            zipped=zip(details,drafts)
            context = {
                'zipped':zipped
            }
        else:
            drafts={
                'title':'',
                'category':'',
                'summary':'',
                'content':''
            }
            zipped=zip(details,drafts)
            context={
                    'zipped':zipped,

                }
        return render(request,"swasthcare/doctor_dashboard.html",context)

    else:
        context = {
            "message": "Entered wrong credentials"
        }
        return render(request, "swasthcare/doctor_login.html", context=context)

def save_blogs(request):
    if request.method == "POST":
        username = request.POST.get('username')
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        summary = request.POST.get('summary')
        content = request.POST.get('content')

        myuser=request.user
        login(request,myuser)
        blogs = Blogs.objects.filter(username=username)
        uniqueid=username+"_"+str(len(blogs)+1)
        obj = Blogs(uniqueid=uniqueid,username=username, title=title, image=image,
                    category=category, summary=summary, content=content)
        obj.save()
        blogs = Blogs.objects.filter(username=username)
        context={
            'blogs':blogs
        }

        return render(request, 'swasthcare/your_blogs.html',context=context)
def see_your_blogs(request):
    myuser = request.user
    login(request, myuser)
    return render(request,'swasthcare/your_blogs.html',)
def save_draft(request):
    if request.method=='POST':
        username = request.POST.get('username')
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        if len(summary)>15:
            summary=summary[:16]+"..."
        draft=Draft(username=username,title=title,image=image,
                    category=category,summary=summary,content=content)
        draft.save()
        return render(request,'swasthcare/home.html')


def logged_out(request):
    logout(request)
    return render(request,"swasthcare/home.html")
def address(request):
    return render(request,"swasthcare/address.html")
def blog_page(request,uniqueid):
    blog=Blogs.objects.filter(uniqueid=uniqueid)
    return render(request,'swasthcare/blog.html',{'blog':blog})
def all_blogs(request):
    blogs=Blogs.objects.all()
    context={
        'blogs':blogs
    }
    return render(request,'swasthcare/all_blogs.html',context=context)
