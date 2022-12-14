from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Hours(models.Model):
    # Fields of the Model
    name = models.CharField(max_length=255)  # Name of Club Member
    # date_charity = models.DateTimeField("date serviced"),  # Date of Community Service Performed
    hours_work = models.IntegerField()  # Number of Hours of Community Service
    type_work = models.CharField(max_length=20)  # type of service: admin/charity
    service_work = models.CharField(max_length=140)  # name of Program
    describe = models.CharField(max_length=255)  # Description of Service Performed

    # rename the instances of the model
    def __str__(self):
        return self.name




