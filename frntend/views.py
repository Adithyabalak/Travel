from django.shortcuts import render,redirect
from django.shortcuts import render
from backend.models import destinationdb,packagedb,hoteldb,hotel_detailsdb,activitidb
from  frntend.models import registerdb,booking_hoteldb,booking_placedb,resrvationdb,actdb
from frntend.models import contactdb,paymentdb
from  django.contrib import messages
from django.db.models import Sum



def home_page(request):
    des=packagedb.objects.all()
    hot=hoteldb.objects.all()
    act=activitidb.objects.all()
    return render(request,'home.html',{'des':des ,'hot':hot ,'act':act})

def about_page(request):
    return render(request,'about.html')

def hotel_all(request):
    hott = hotel_detailsdb.objects.all()
    return render(request,'hotelsall.html',{'hott':hott})

def all_des(request):
    des=destinationdb.objects.all()
    return render(request,'all_destination.html',{'des':des})


def contact_us(re):
    return render(re,'contact.html')

def save_contact(re):
    if re.method=="POST":
        a=re.POST.get("uname")
        b=re.POST.get("mail")
        c=re.POST.get("subj")
        d=re.POST.get("mess")
        obj=contactdb(name=a,email=b,subject=c,message=d)
        obj.save()
        return redirect(contact_us)

def blog_page(request):
    return render(request,'blog.html')

def single_page(re,pro_id):
    pro = packagedb.objects.get(id=pro_id)
    return render(re, 'single_package.html', {'pro': pro})

def all_hotel(request,ht_name):
    data=hotel_detailsdb.objects.filter(place=ht_name)
    return render(request,'all_hotel.html',{'data':data})

def single_hotel(request,htlid):
    htl = hotel_detailsdb.objects.get(id=htlid)
    return render(request,'singlepage_hotel.html',{'htl':htl})

def login_page(request):
    return render(request,'login_user.html')

def register_page(request):
    return render(request,'register_page.html')

def save_register(re):
    if re.method=="POST":
        a=re.POST.get("uname")
        b=re.POST.get("email")
        p=re.POST.get("pass1")
        img=re.FILES["image"]
        obj=registerdb(name=a,email=b,password=p,profile=img)
        obj.save()
        return redirect(register_page)


def login_user(request):
    if request.method == "POST":
        u = request.POST.get('username')
        n = request.POST.get('pass')
        if registerdb.objects.filter(name=u, password=n).exists():
            request.session['name'] = u
            request.session['password'] = n
            messages.success(request, "welcome")
            return redirect(home_page)
        else:
            messages.warning(request, "Incorrect password or username")
            return redirect(login_page)
    return redirect(login_page)

def logout_user(request):
    del request.session['name']
    del request.session['password']
    return redirect(home_page)




def save_booking_hotel(request):
    if request.method=="POST":
        a=request.POST.get("peo")
        b=request.POST.get("pri")
        c=request.POST.get("name")
        d=request.POST.get("htlname")
        e=request.POST.get("t_price")
        obj=booking_hoteldb(peoples=a,price=b,username=c,hotel_name=d,total_price=e)
        obj.save()
        return redirect(booking_page)

def save_booking_place(request):
    if request.method=="POST":
        a=request.POST.get("peo")
        b=request.POST.get("price")
        c=request.POST.get("user_name")
        d=request.POST.get("place")
        e=request.POST.get("t_price")
        obj=booking_placedb(peoples=a,price=b,username=c,place=d,total_price=e)
        obj.save()
        return redirect(booking_page)

def delete_booking(request,dataid):
    dele=booking_hoteldb.objects.filter(id=dataid)
    dele.delete()
    return redirect(booking_page)

def delete_place(request,plcid):
    x=booking_placedb.objects.filter(id=plcid)
    x.delete()
    messages.success(request, "deleted successfully")
    return redirect(booking_page)


def check_out(request):
    data = booking_hoteldb.objects.filter(username=request.session['name'])
    data1 = booking_placedb.objects.filter(username=request.session['name'])
    total = 0
    for i in data:
        total = total + i.total_price
    for i in data1:
        total = total + i.total_price

    return render(request,'check_out.html',{'data':data,'data1':data1,'total':total })




def payment_page(request):
    return render(request,'payment.html')

def save_payment(request):
    if request.method=="POST":
        u=request.POST.get('User')
        cn=request.POST.get('cname')
        my=request.POST.get('monthyr')
        cvv=request.POST.get('cvv')
        n=request.POST.get('name')
        obj=paymentdb(username=u,cardnumber=cn,monthyear=my,cvv=cvv,name=n)
        obj.save()
        messages.success(request, "paid successfully")
        return redirect(payment_page)


def chatbot_page(request):
    return render(request,'chatbot.html')

def re_page(request):
    return render(request,'resrve_page.html')



def booking_page(request):
    data = booking_hoteldb.objects.filter(username=request.session['name'])
    data1 = booking_placedb.objects.filter(username=request.session['name'])
    data2 = actdb.objects.filter(name=request.session['name'])


    total_activity_price = data.aggregate(total_price=Sum('total_price'))['total_price']
    total_hotel_price = data1.aggregate(total_price=Sum('total_price'))['total_price']
    total_act_price = data2.aggregate(price=Sum('price'))['price']


    total_price = sum(filter(None, [total_activity_price, total_hotel_price,total_act_price]))

    return render(request, "booking_details.html", {
        'data': data,
        'data1': data1,
        'data2': data2,
        'total_price': total_price
    })


def save_reserve(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('phone')
        c=request.POST.get('checkin')
        d=request.POST.get('gust')
        e=request.POST.get('name2')
        f=request.POST.get('email')
        g=request.POST.get('checkout')
        h=request.POST.get('types')
        obj=resrvationdb(name=a,phone=b,ch_in=c,gust=d,l_name=e,mail=f,ch_out=g,types=h)
        obj.save()
        return redirect(re_page)

def single_act(re,actid):
    act= activitidb.objects.get(id=actid)
    return render(re,'single_activity.html',{'act':act})

def save_act(request):
    a = request.POST.get('activity')
    b = request.POST.get('price')
    c = request.POST.get('user_name')
    obj = actdb(activity=a, price=b, name=c)
    obj.save()
    return redirect(booking_page)

def delete_act(request,actid):
    x=actdb.objects.filter(id=actid)
    x.delete()
    messages.success(request, "deleted successfully")
    return redirect(booking_page)

