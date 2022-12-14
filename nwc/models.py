from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Hours(models.Model):
    # Fields of the Model
    name = models.CharField(_("Name"), max_length=255)  # Name of Club Member
    date_charity = models.DateField(_("Date"), auto_now=True)  # Date of Community Service Performed
    hours_work = models.IntegerField(_("Number of Hours Worked"))  # Number of Hours of Community Service
    type_work = models.CharField(_("type of service hours worked"), max_length=20)  # type of service: admin/charity
    service_work = models.CharField(_("community serviceadmin type"), max_length=140)  # name of Program
    describe = models.CharField(_("Description of what you did"), max_length=255)  # Description of Service Performed

    # rename the instances of the model
    def __str__(self):
        return self.name




