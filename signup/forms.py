from login.models import *
from django import forms
from django.contrib.auth.models import User
from gst_field.formfields import PANField
from phone_field import PhoneField
import re
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.hashers import make_password, check_password


class Signup(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    mobile_number = PhoneNumberField()
    pan_card = PANField()
    password = forms.CharField(widget=forms.PasswordInput())
    alternate_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ['username','first_name','last_name','email','mobile_number','pan_card']

    def save(self):
        clean = self.cleaned_data
        username = clean['username']
        password = clean['password']
        hashed_password = make_password(password)
        first_name = clean['first_name']
        last_name = clean['last_name']
        email = clean['email']
        pattern = r"(([a-z0-9\W]*)(@kct.ac.in))"
        is_staff = False
        if re.fullmatch(pattern,email) is not None:
            is_staff = True
        mobile_number = clean['mobile_number']
        pan_card = clean['pan_card']
        auth_user = User.objects.create(username = username,password=hashed_password,first_name = first_name,last_name = last_name,email = email,is_staff=is_staff)
        user_data = User_details.objects.create(mobile_number = mobile_number,pan_card = pan_card)
        user_signup = User_model.objects.create(user= auth_user,details=user_data)
        return user_signup