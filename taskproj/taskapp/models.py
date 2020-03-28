from django.db import models
from enum import Enum
from datetime import date

#an enumeration classes
class TaskType(Enum):
    d = 'daily'
    o = 'other'

class ActivityType(Enum):
    f='completed'
    c='continuing'
    q='quitting'


# Create your models here.
class Category(models.Model):
    categoryname=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.categoryname
    
    class Meta:
        db_table='category'

class Task(models.Model):
    taskname=models.CharField(max_length=255)
    category=models.ManyToManyField(Category)
    tasktype=models.CharField(max_length=5,choices=[(tag, tag.value) for tag in TaskType])
    taskentrydate=models.DateField(default=date.today)
    taskdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.taskname

    class Meta:
        db_table='task'
    
class Activity(models.Model):
    task=models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    activitytype=models.CharField(max_length=10,choices=[(tag, tag.value) for tag in ActivityType])
    activitydescription=models.TextField()

    def __str__(self):
        return self.activitydescription





