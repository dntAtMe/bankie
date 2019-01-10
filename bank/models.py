from django.db import models
from django.contrib.auth.models import User
import datetime

ACCOUNT_STATUS = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)

#PAYMENT_STATUS = (
 #   ('A', 'Approved'),
 #   ('P','Pending'),
 #   ('D', 'Denied'),
#)

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    number = models.PositiveIntegerField(null=False)
    amount = models.DecimalField(null=False, decimal_places=2, default=0.0, max_digits=10)
    status = models.CharField(max_length=1, choices=ACCOUNT_STATUS, null=False, default='Active')

class Payment(models.Model):
    account_from = models.ForeignKey(User, on_delete=models.PROTECT, related_name='acc_from')
    account_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='acc_to')
    amount = models.DecimalField(null=False, decimal_places=2, default=0.0, max_digits=10)
    description = models.TextField(null=False, default='')
    #status = models.CharField(max_length=1, choices=PAYMENT_STATUS, null=False)
    date = models.DateTimeField(default=datetime.datetime.now())
