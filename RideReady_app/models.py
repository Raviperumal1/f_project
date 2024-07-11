
from django.db import models

class Profile(models.Model):
    firstName = models.CharField(max_length=100)
    email = models.EmailField()
class Meta:
    db_tables="profile"

class data(models.Model):
    fullname = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    account_number= models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    branch= models.CharField(max_length=100)
    ex_showroom_price = models.CharField(max_length=100)
    loan_amount = models.CharField(max_length=100)
    initial_amount = models.CharField(max_length=100)
class Meta:
    db_tables="data"

# class Profile2(models.Model):
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipCode = models.CharField(max_length=10)
#     bankName = models.CharField(max_length=100)
#     accountNumber = models.CharField(max_length=20)
#     ifscCode = models.CharField(max_length=20)
# class Meta:
#     db_tables="profile2"

# class Profile3(models.Model):
#     exShowroomPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     initialPayment = models.DecimalField(max_digits=10, decimal_places=2)
#     loanAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     loanApplicationDate = models.DateField()
# class Meta:
#     db_tables="profile3"

    