from django.db import models

# Create your models here.
class HotelLocation(models.Model):
    location=models.CharField(max_length=250)
    
    def __str__(self):
        return self.location


class Hotels(models.Model):
    hotel_location=models.ForeignKey(HotelLocation,on_delete=models.CASCADE)
    hotel_names=models.CharField(max_length=300)
    #room_type=models.CharField(max_length=25)
    base_price=models.IntegerField()
    tax_price=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    # total_price=base_price+tax_price

    def __str__(self):
        return self.hotel_names


class Users(models.Model):
    title=models.CharField(max_length=5)
    user_first_name=models.CharField(max_length=250)
    user_last_name=models.CharField(max_length=250)
    user_email=models.EmailField(max_length=250)
    user_phone=models.CharField(max_length=250)

    def __str__(self):
        return self.user_first_name

    def all_info(self):
        return [self.title,self.user_first_name,self.user_last_name,self.user_email,self.user_phone]
    
class Booking(models.Model):
    user_phone=models.CharField(max_length=250)
    # user_phone=models.ForeignKey(Users,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    user_hotel=models.CharField(max_length=250)
    special_request=models.TextField(null=True)

    def __str__(self):
        return self.user_hotel

    def all_info(self):
        return [self.user_phone,self.check_in,self.check_out,self.user_hotel,self.special_request]
