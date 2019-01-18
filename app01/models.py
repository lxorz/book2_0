from django.db import models

# Create your models here.


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    #与AuthonDetail建立一对一关系
    authorDetail=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telphone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


class Publish(models.Model):
    nid = models.AutoField()
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

class Book(models.Model):
    nid = models.AutoField()
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)

    #与Publish建立一对多的关系，外键建立在多的一方
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)

    #与Author建立多对多的关系，关系可以建在任意一方，自动创建第三章表
    authors=models.ManyToManyField(to="Author",)


