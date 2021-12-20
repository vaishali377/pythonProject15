from django.db import models

class ContactForm(models.Model):
    username= models.CharField(max_length=100)
    email= models.EmailField()
    password1= models.CharField(max_length=50)
    password2= models.CharField(max_length=50)

    def __str__(self):
        return self.username