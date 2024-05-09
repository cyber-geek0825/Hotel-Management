from django.shortcuts import render
from .models import HotelLocation,Hotels,Users,Booking

# Create your views here.

def home(request):
    return render(request,'index.html',{})

def search_result(request):
    if request.method=="POST":
        loc=request.POST['loc'].capitalize()
        check_in=request.POST['check_in']
        check_out=request.POST['check_out']
        hotel_loc=HotelLocation.objects.get(location=loc)
        print(hotel_loc)
        hotels_in_loc=hotel_loc.hotels_set.all()
        print(hotels_in_loc)
        return render(request,'search_result.html', {'qs':hotels_in_loc,'loc':loc,'check_in':check_in,'check_out':check_out})
    else:
        return render(request,'search_result.html',{})

def booking_page(request):
    if request.method=="POST":
        hotel_name=request.POST['hotel_name']
        # hotel=Hotels.objects.get(hotel_names=hotel_name)
        # loc=hotel.hotel_location.location
        in_date=request.POST['in_date']
        out_date=request.POST['out_date']
        location=request.POST['location']
        base_price=request.POST['base_price']
        tax_price=request.POST['tax_price']
        total_price=request.POST['total_price']
        # hotel=request.POST['hotel']
        # print(hotel)
        # hotel_name=request.POST['hotel_name']
        return render(request,'hotel_booking_form.html',{'hotel_name':hotel_name,'check_in':in_date,'check_out':out_date,'location':location,'base_price':base_price,'tax_price':tax_price,'total_price':total_price})
    else:
        return render(request,'hotel_booking_form.html',{})
    


def final_page(request):
    if request.method=="POST":
        first_name=request.POST['first-name'].strip(' ')
        last_name=request.POST['last-name'].strip(' ')
        hotel_name=request.POST['hotel_name'].strip(' ')
        check_in=request.POST['in_date']
        check_out=request.POST['out_date']
        location=request.POST['location'].strip(' ')
        user_email=request.POST['email'].strip(' ')
        user_phone=request.POST['phone'].strip(' ')
        title=request.POST['title'].strip(' ')
        special_request=request.POST['special-requests']
        # if user_phone not in  Users.objects.all():
        if not Users.objects.filter(user_phone=user_phone).exists():
            t=Users(title=title,user_first_name=first_name,user_last_name=last_name,user_email=user_email,user_phone=user_phone)
            t.save()
        else:
            t=Users.objects.get(user_phone=user_phone)
        # t=Booking(user_phone=user_phone,check_in=check_in,check_out=check_out,user_hotel=hotel_name,special_request=special_request)
        # t.save()
        t.booking_set.create(first_name=first_name,last_name=last_name,check_in=check_in,check_out=check_out,user_hotel=hotel_name,special_request=special_request)
        return render(request,'final_page.html',{})
    else:
        return render(request,'final_page.html',{})
