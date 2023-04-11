from django.db import models
from .utils import wakeonlan, WakeOnLanException
from django.utils.timezone import datetime

# Create your models here.


class Machine(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default=None, null=True, blank=True)
    mac_address = models.CharField(max_length=17)
    ip_address = models.GenericIPAddressField(default=None, null=True, blank=True)
    last_wake = models.DateTimeField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=None, null=True, blank=True)
    wake_error = models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def set_wake_error(self):
        self.wake_error = True
        self.save()

    def set_last_wake(self):
        self.last_wake = datetime.now()
        self.save()

    def awake(self):
        try:
            wakeonlan(self.mac_address)
            self.set_last_wake()
        except WakeOnLanException as e:
            self.set_wake_error()
            pass
