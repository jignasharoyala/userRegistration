from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_email1 = models.EmailField()
    user_email2 = models.EmailField()
    user_location = models.CharField(max_length=50)
    user_file = models.FileField(upload_to='documents', blank=True)
    addmin_comment = models.TextField()
    user_replay = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.user_name

class Email(models.Model):
    user_id = models.ForeignKey(UserProfileDetails, on_delete=models.CASCADE,)
    email = models.EmailField()
    primary = models.BooleanField()