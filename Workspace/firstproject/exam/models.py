from django.db import models

class Addcontact(models.Model):
       Name = models.CharField(max_length=100)
       city = models.CharField(max_length=100)
       State = models.CharField(max_length=100)
       Createdate = models.DateTimeField()
       PhoneNumber = models.IntegerField()
       Email = models.EmailField(max_length=254)
       def __str__(self):
            return "Mr."+ self.Name +" City = "+self.city+" State = "+self.State+" PhoneNumber = "+str(self.PhoneNumber)+" Email-Id = "+self.Email


