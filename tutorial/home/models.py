from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    post=models.CharField(max_length=100)
    user=models.ForeignKey(User)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'written by %s' % (self.user)

class Friend(models.Model):
    users=models.ManyToManyField(User)
    current_user=models.ForeignKey(User,related_name='owner',null=True)

    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend, created=cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)


class Messages(models.Model):
    content=models.CharField(max_length=500)

