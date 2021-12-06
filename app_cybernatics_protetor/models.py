from django.db import models
class adminlogin(models.Model):
    id=models.IntegerField(primary_key=True,default='1')
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    department=models.CharField(max_length=20,default='Defence')
    photo=models.ImageField(upload_to='admin_image/',default=None)

class success_stories(models.Model):
    story_title = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    image=models.ImageField(upload_to='crime_story/',default=None)

class Job_Postings(models.Model):
    Job = models.CharField(max_length=30,default=False)
    Title = models.CharField(max_length=30)
    Qualification = models.CharField(max_length=50)
    Percentage = models.IntegerField()
    Experience = models.IntegerField(help_text="In Years")
    Last_date = models.DateField()
    Location = models.CharField(max_length=100)
    Salary = models.DecimalField(max_digits=10,decimal_places=2)
class CaseCreation(models.Model):
    case_id = models.AutoField(primary_key=True,default=None)
    case_name = models.CharField(max_length=30)
    doc = models.DateField()
    file = models.FileField(default=None, upload_to='case_files/')
    status=models.CharField(default='Pending',max_length=20)

class CreateAgent(models.Model):
    agent_id = models.AutoField(primary_key=True,default=None)
    Agent_Name = models.CharField(max_length=30)
    Password =models.CharField(max_length=50)
    Dob = models.DateField()
    Contact_Number = models.IntegerField(unique=True,default=None)
    Email=models.EmailField(unique=True,default=None)
    Qualification = models.CharField(max_length=30)
    Address	= models.CharField(max_length=100)
    image = models.ImageField(upload_to='agent/', default=None)



class Tips(models.Model):
    Name = models.CharField(max_length=30)
    Location = models.CharField(max_length=50)
    Suggession = models.CharField(max_length=100)

class Applicants(models.Model):
    JOB_TITLE = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    Dob = models.DateField()
    Qualification = models.CharField(max_length=30)
    percentage = models.IntegerField()
    Institute = models.CharField(max_length=30)
    Experience = models.IntegerField()
    Contact_Number = models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    status=models.CharField(default='Pending',max_length=10)

class Assign_Agent(models.Model):
    agent_id = models.IntegerField()
    CaseCreation_Agent = models.OneToOneField(CaseCreation, on_delete=models.CASCADE, default="1")

class CaseDetails(models.Model):
    agent_id = models.IntegerField()
    case_id = models.IntegerField()
    case_name= models.CharField(max_length=30)

    status= models.CharField(max_length=30)

    file=models.FileField(default=None,upload_to='case_files/')

class Defence_Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)


class Staff(models.Model):
    idno=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=30)
    Contact=models.IntegerField(unique=True)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=20)
    Status=models.CharField(max_length=10,default='Pending')
    Photo=models.ImageField(default=None,upload_to='staff_image/')