from django.db import models
from .utils import wakeonlan, WakeOnLanException, ping, PingException
from django.utils.timezone import datetime

# Create your models here.


class Machine(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default=None, null=True, blank=True)
    mac_address = models.CharField(max_length=17)
    ip_address = models.GenericIPAddressField(default=None, null=True, blank=True)
    last_wake = models.DateTimeField(default=None, null=True, blank=True)
    wake_error = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=None, null=True, blank=True)
    last_ping = models.DateTimeField(default=None, null=True, blank=True)

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

    @property
    def is_up(self):
        return self.is_active()

    def awake(self):
        try:
            wakeonlan(self.mac_address)
            self.set_last_wake()
        except WakeOnLanException as e:
            self.set_wake_error()
            pass

    def ping(self):
        if not self.ip_address:
            pass

        try:
            if ping(self.ip_address):
                self.is_active = True
            else:
                self.is_active = False
            self.last_ping = datetime.now()
            self.save()
        except PingException as e:
            pass
