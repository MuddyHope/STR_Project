from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
class TodoList(models.Model):
    username = models.CharField(max_length = 50)
    #slno = models.IntegerField()
    title = models.TextField(max_length = 100)
    num1 = models.IntegerField(default=0)
    num2 = models.IntegerField(default=0)
    num3 = models.IntegerField(default=0,null=False)
    average = models.IntegerField(default=0)



    def __str__(self) -> str:
        return self.username