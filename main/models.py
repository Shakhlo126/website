from django.db import models

# Create your models here.

class Users(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    image=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Vd_lessons(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    image=models.CharField(max_length=50)
    vd=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.name
class Client(models.Model):
    vd_id = models.ForeignKey(Vd_lessons, on_delete=models.CASCADE)
    is_pay=models.CharField(max_length=50)
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id

class Payment(models.Model):
    price =models.IntegerField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.price

class About(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    vd=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    name=models.CharField(max_length=50)
    profession=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    image=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Web_sites(models.Model):
    name=models.CharField(max_length=50)
    link=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Web_images(models.Model):
    web_sites=models.ForeignKey(Web_sites, on_delete=models.CASCADE)
    image=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.image