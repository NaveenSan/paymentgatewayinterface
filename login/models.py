from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import ForeignKey, CASCADE, Model
from gst_field.modelfields import GSTField, PANField
from phone_field import PhoneField


#user_details to be stored
class User_details(models.Model):
    pan_card = PANField(blank=False)
    mobile_number =PhoneField(blank=False, help_text='Contact phone number')

#using inheritence of User model name - User_model
class User_model(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE)
    details = models.ForeignKey(User_details,on_delete=CASCADE,null=True)

