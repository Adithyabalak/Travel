from django.shortcuts import render,redirect
from backend.models import destinationdb,packagedb,hoteldb,hotel_detailsdb,activitidb
from frntend.models import contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from  django.http import  HttpResponse
from  django.core.mail import send_mail
from  django.contrib import messages

from  django.conf import settings


def indexpage(re):
    return render(re,'index_page.html')

def des_page(re):
    return  render(re,'destination.html')

def save_destination(request):
    if request.method=="POST":
        a=request.POST.get("place")
        b=request.POST.get("des")
        img=request.FILES["image"]
        obj=destinationdb(place=a,description=b,profile=img)
        obj.save()
        return redirect(des_page)

def display_des(request):
    data=destinationdb.objects.all()
    return render(request,'displaydestination.html',{'data':data})


def edit_des(request,destid):
    data = destinationdb.objects.get(id=destid)
    return render(request,'editdestination.html',{'data':data})

def update_des(request,destid):
    if request.method=="POST":
        a = request.POST.get("place")
        b = request.POST.get("des")
    try:
        img=request.FILES['image']
        fs=FileSystemStorage()
        file = fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=destinationdb.objects.get(id=destid).profile
    destinationdb.objects.filter(id=destid).update(place=a,description=b,profile=file)
    return redirect(display_des)

def delete_page(request,destid):
    x=destinationdb.objects.filter(id=destid)
    x.delete()
    return redirect(display_des)


def packages(request):
    pack=destinationdb.objects.all()
    return render(request,'hotels_page.html',{'pack':pack})


def save_package(request):
    if request.method=="POST":
        a=request.POST.get("place")
        b=request.POST.get("country")
        c=request.POST.get("des")
        f=request.POST.get("days" )
        g=request.POST.get("price" )
        img=request.FILES["image"]
        img1=request.FILES["image1"]
        img2=request.FILES["image2"]
        obj=packagedb(country1=b,place=a,description=c,days=f,profile3=img,profile1=img1,profile2=img2,price=g)
        obj.save()
        return redirect(packages)

def display_packages(request):
    data=packagedb.objects.all()
    return render(request,'displaypackage.html',{'data':data})

def edit_pack(request,packid):
    pack=destinationdb.objects.all()
    data = packagedb.objects.get(id=packid)
    return render(request,'editpackage.html',{'data':data,'pack':pack})

def update_package(request, packid):
    if request.method == "POST":
        a = request.POST.get("place")
        b = request.POST.get("country")
        c = request.POST.get("des")
        f = request.POST.get("days")
        g = request.POST.get("price")
        try:
            img=request.FILES["image"]
            fs1 = FileSystemStorage()
            file1 = fs1.save(img.name, img)
        except MultiValueDictKeyError:
            file1 = packagedb.objects.get(id=packid).profile3

        try:
            img1 = request.FILES["image1"]
            fs2 = FileSystemStorage()
            file2 = fs2.save(img1.name, img1)
        except MultiValueDictKeyError:
            file2 = packagedb.objects.get(id=packid).profile1

        try:
            img2 = request.FILES["image2"]
            fs3 = FileSystemStorage()
            file3 = fs3.save(img2.name, img2)
        except MultiValueDictKeyError:
            file3 = packagedb.objects.get(id=packid).profile2

        packagedb.objects.filter(id=packid).update(country1=b,place=a,description=c,days=f,price=g,profile3=file1,profile1=file2,profile2=file3)
        return redirect(display_packages)

def delete_package(request,packid):
    x=packagedb.objects.filter(id=packid)
    x.delete()
    return redirect(display_packages)


def hotel_page(request):
    return render(request,'hotel.html')


def save_hotel(request):
    if request.method=="POST":
        a=request.POST.get("place")
        img=request.FILES["image"]
        obj=hoteldb(place=a,profile=img)
        obj.save()
        return redirect(hotel_page)

def display_hotel(request):
    data=hoteldb.objects.all()
    return render(request,'display_hotel.html',{'data':data})

def edit_hotel(request,hotelid):
    data = hoteldb.objects.get(id=hotelid)
    return render(request,'edit_hotel.html',{'data':data})

def update_hotel(request,hotelid):
    if request.method=="POST":
        a = request.POST.get("place")
    try:
        img=request.FILES['image']
        fs=FileSystemStorage()
        file = fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=hoteldb.objects.get(id=hotelid).profile
    hoteldb.objects.filter(id=hotelid).update(place=a,profile=file)
    return redirect(display_hotel)

def delete_hotel(request,hotelid):
    x=hoteldb.objects.filter(id=hotelid)
    x.delete()
    return redirect(display_hotel)


def  hotel_details(request):
    hotl = hoteldb.objects.all()
    return  render(request,'hotel_details.html',{'hotl':hotl})


def save_hotel_details(request):
    if request.method=="POST":
        a=request.POST.get("place")
        b=request.POST.get("hotel")
        c=request.POST.get("des")
        f=request.POST.get("price" )
        img=request.FILES["image"]
        img1=request.FILES["image1"]
        img2=request.FILES["image2"]
        img3=request.FILES["image3"]
        img4=request.FILES["image4"]
        obj=hotel_detailsdb(place=a,name=b,description=c,price=f,profile1=img,profile2=img1,profile3=img2,profile4=img3,profile5=img4)
        obj.save()
        return redirect(hotel_details)

def display_details(request):
    data=hotel_detailsdb.objects.all()
    return render(request,'display_hotel_details.html',{'data':data})

def edit_details(request,detid):
    hotl=hoteldb.objects.all()
    data = hotel_detailsdb.objects.get(id=detid)
    return render(request,'edit_hotl_details.html',{'data':data,'hotl':hotl})


def update_hotel_details(request, detid):
    if request.method == "POST":
        a = request.POST.get("place")
        b = request.POST.get("hotel")
        c = request.POST.get("des")
        f = request.POST.get("price")
        try:
            img=request.FILES["image"]
            fs1 = FileSystemStorage()
            file1 = fs1.save(img.name, img)
        except MultiValueDictKeyError:
            file1 = hotel_detailsdb.objects.get(id=detid).profile1

        try:
            img1 = request.FILES["image1"]
            fs2 = FileSystemStorage()
            file2 = fs2.save(img1.name, img1)
        except MultiValueDictKeyError:
            file2 = hotel_detailsdb.objects.get(id=detid).profile2

        try:
            img2 = request.FILES["image2"]
            fs3 = FileSystemStorage()
            file3 = fs3.save(img2.name, img2)
        except MultiValueDictKeyError:
            file3 = hotel_detailsdb.objects.get(id=detid).profile3

        try:
            img3 = request.FILES["image3"]
            fs4 = FileSystemStorage()
            file4 = fs4.save(img3.name, img3)
        except MultiValueDictKeyError:
            file4 = hotel_detailsdb.objects.get(id=detid).profile4

        try:
            img4 = request.FILES["image4"]
            fs5 = FileSystemStorage()
            file5 = fs5.save(img4.name, img4)
        except MultiValueDictKeyError:
            file5 = hotel_detailsdb.objects.get(id=detid).profile5
        hotel_detailsdb.objects.filter(id=detid).update(place=a,name=b,description=c,price=f,profile1=file1,profile2=file2,profile3=file3,profile4=file4,profile5=file5)
        return redirect(display_details)


def delete_hotel_details(request,detid):
    x=hotel_detailsdb.objects.filter(id=detid)
    x.delete()
    return redirect(display_details)
def login_pages(request):
    return render(request,'login_pagess.html')

def admin_login(request):
    if request.method=="POST":
       u=request.POST.get('u_name')
       p=request.POST.get('p_name')
       if User.objects.filter(username__contains=u).exists():
           x = authenticate(username=u, password=p)

           if x is not None:
               login(request, x)
               request.session['username']=u
               request.session['password']=p
               return redirect(indexpage)

           else:
                return redirect(login_pages)
       else:
            return redirect(login_pages)



def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_pages)


def contact_data(re):
    data = contactdb.objects.all()
    return render(re, 'contact_page.html', {'data':data})

def delete_contact(request,conid):
    x=contactdb.objects.filter(id=conid)
    x.delete()
    return redirect(contact_data)



def mail_page(request):
    if request.method=='POST':
        message=request.POST['message']
        email=request.POST['email']
        name=request.POST['name']
        send_mail(
             name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False)
    return render(request,'mail_page.html')


def activity(request):
    return render(request,'activities.html')

def save_activity(request):
    if request.method=="POST":
        a=request.POST.get("activity")
        b=request.POST.get("hour")
        c=request.POST.get("price")
        img=request.FILES["image"]
        obj=activitidb(activity=a,profile=img,hour=b,price=c)
        obj.save()
        return redirect(activity)

def display_activities(request):
    data=activitidb.objects.all()
    return render(request,'dis_activities.html',{'data':data})


def edit_activity(request,acid):
    data = activitidb.objects.get(id=acid)
    return render(request,'edit_activitis.html',{'data':data})

def update_activity(request,acid):
    if request.method=="POST":
        a = request.POST.get("activity")
        b = request.POST.get("hour")
        c = request.POST.get("price")
    try:
        img=request.FILES['image']
        fs=FileSystemStorage()
        file = fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=activitidb.objects.get(id=acid).profile
    activitidb.objects.filter(id=acid).update(activity=a,hour=b,price=c,profile=file)
    return redirect(display_activities)

def delete_act(request,acid):
    x=activitidb.objects.filter(id=acid)
    x.delete()
    return redirect(display_activities)


# Create your views here.
