from django.db import models

# Create your models here.


class Customers(models.Model):
    customer_Name = models.CharField(max_length=200)
    customer_Email = models.CharField(max_length=200)
    customer_Phone = models.CharField(max_length=11)
    starting_date = models.DateField('Contract Start date')
    due_date = models.DateField('Contract end date')
    Comment = models.TextField()

    def __str__(self):
        return self.customer_Name