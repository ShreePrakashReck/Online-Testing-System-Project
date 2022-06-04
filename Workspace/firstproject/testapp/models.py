from django.db import models

class Employee(models.Model):
       eno=models.IntegerField()
       ename=models.CharField(max_length=200)
       esal=models.FloatField(max_length=100)
       def __str__(self):
           return "Mr."+self.ename+' '+str(self.esal)       