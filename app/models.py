from django.db import models

from asyncio import format_helpers
from django.db import models



class Pupil(models.Model):
    name = models.CharField(max_length=400, help_text="Enter Pupil name....")
    date = models.DateField(null=True, blank=True, help_text="Date | Month | Year")
    email_address = models.CharField(max_length=200, help_text="Enter email address ...", null=True)
    phone_number = models.IntegerField()
    passport_id = models.CharField(max_length=200, null=True, blank=True)
    payment = models.BooleanField(help_text="if paid, click the button")
    one_id = models.IntegerField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.name
    @property
    def image_show(self):
        return format_helpers('<img src = {} width="60" height="60" style="border-radius:50%;"'.format(self.image.url))
    def save(self, *args, **kwargs):
        super(Pupil, self).save(*args, **kwargs)
        if self.id:
            self.one_id = self.id +1000
        super(Pupil, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name} | {self.email_address} | {self.phone_number} | {self.payment} | {self.one_id}"
