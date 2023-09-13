from django.db import models

# Create your models here.
class Boarder(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number=models.CharField(max_length=255)
    room_number=models.CharField(max_length=255)
    ##phone = models.IntegerField()
    ##joined_date = models.DateField()
    user_id=models.IntegerField(null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Roomt(models.Model):
    room_num = models.CharField(max_length=255)
    monthly_rent = models.CharField(max_length=255)
    availability=models.CharField(max_length=255)


class Maintenance(models.Model):
    room_id = models.ForeignKey(Roomt, on_delete=models.CASCADE)
    issue_desc = models.CharField(max_length=500)
    status= models.CharField(max_length=255)   
    

class Bills(models.Model):
    boarder_id = models.ForeignKey(Boarder, on_delete=models.CASCADE)
    month=models.CharField(max_length=255)
    rent = models.CharField(max_length=255)
    electricity=models.CharField(max_length=255)
    water=models.CharField(max_length=255)
    due_date=models.DateField()
    status=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.month} {self.due_date} {self.rent} {self.electricity} {self.water} {self.status}"

