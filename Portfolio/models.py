from django.db import models

# Create your models here.
class Portfolio(models.Model):
    ism = models.CharField(max_length=2000)
    familya = models.CharField(max_length=2000)
    data = models.DateField()
    img = models.ImageField(upload_to="images")
    email = models.EmailField(max_length=2000)
    manzil = models.CharField(max_length=20000)
    uzi_haqida = models.TextField()
    tel = models.IntegerField()



    def __str__(self):
        return f"{self.ism} | {self.familya} | {self.data} | {self.img} | {self.email} | {self.manzil} | {self.uzi_haqida}"



class Statistics(models.Model):
    statistics = models.TextField()
    clients = models.IntegerField()
    projects = models.IntegerField()
    monthly_experience = models.IntegerField()

    def __str__(self):
        return f"{self.statistics} | {self.clients} | {self.projects} | {self.monthly_experience} "

class Skills(models.Model):
    skills_name = models.CharField(max_length=200)
    skills = models.IntegerField()

    def __str__(self):
        return f"{self.skills} | {self.skills_name}"

    class Meta:
        verbose_name = "Skills"
        verbose_name_plural = 'Skills'





class Services(models.Model):
    services_name = models.CharField(max_length=200)
    services_text = models.TextField()
    services_img = models.ImageField(upload_to="images")


    def __str__(self):
        return f"{self.services_text} | {self.services_name} | {self.services_img}"

    class Meta:
        verbose_name = "services"
        verbose_name_plural = 'services'


class Contact(models.Model):
    manzil = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    tel = models.CharField(max_length=2000)
    lokatsya = models.TextField()

    def __str__(self):
        return f"{self.manzil} | {self.email} | {self.tel} | {self.lokatsya}"

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contact"



