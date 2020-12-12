from django.db import models

# Create your models here.

class UserProfileDetails(models.Model):
    user_id = models.AutoField(primary_key=True,editable=False)
    user_name = models.CharField(max_length=50)
    user_email1 = models.EmailField()
    user_email2 = models.EmailField()
    user_location = models.CharField(max_length=50)
    user_file = models.FileField(upload_to='documents')
    addmin_comment = models.TextField()
    user_replay = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)


class Email(models.Model):
    user_id = models.ForeignKey(UserProfileDetails, on_delete=models.CASCADE,)
    email = models.EmailField()
    primary = models.BooleanField()