from django.db import models
from django.utils import timezone
from datetime import date
PRORITY = [
    ['low','LOW'],
    ['medium','Medium'],
    ['high','Heigh'],
    ['urgent','Urgent']
]

STATUS = [
    ['todo','TODO'],
    ['in_progres','IN_prognez'],
    ['review','Review'],
    ['done','Done'],
    ['canclled','Cancled']
]

class Task(models.Model): #--bu jadval yaratib beradi
    name         = models.CharField(max_length=50)
    title        = models.CharField(max_length=200,default='')
    description  = models.TextField(blank=True,null=True,default="medium")
    status       = models.CharField(choices=STATUS,blank=True,default='todo')
    priorty      = models.CharField(choices=PRORITY,default='')
    start_date   = models.DateField(default=date.today())
    due_date     = models.DateTimeField(default=timezone.now)
    email        = models.EmailField(max_length=200,blank=True)


    def __str__(self):
        return f"Task(id={self.id}, name='{self.name}')"
