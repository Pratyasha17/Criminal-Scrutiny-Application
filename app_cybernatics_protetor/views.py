from   django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from app_cybernatics_protetor.models import Defence_Login,Applicants,adminlogin, success_stories, Job_Postings, CreateAgent, Tips,Assign_Agent, CaseDetails, CaseCreation,Staff
from django.contrib import messages
from app_cybernatics_protetor.forms import Defenceform,Staff_validation,Agent,Adminform
from django.contrib.messages.views import SuccessMessageMixin

def adminLogin(request):
    username = request.POST.get('name')
    password = request.POST.get('password')
    qs = adminlogin.objects.filter(username=username,password=password)
    if qs:
        res=adminlogin.objects.filter(username=username,password=password).values("id","password","username","photo","department").distinct()
        request.session['user'] = res[0]
        use = request.session.get('user', None)
        request.session.set_expiry(0)
        if request.session.has_key("user"):
            data=adminlogin.objects.all()
            return render(request, 'welcomeadmin.html', {'data':data})
        else:
            messages.error(request, "error")
            return render(request, 'admin.html')

    else:
        messages.error(request,"Invalid Entry")
        return render(request,'admin.html')

def admin_logout(request):
  try:
    if request.session.has_key("user"):
        request.session.flush()
        return render(request, 'admin.html')
    else:
        messages.error(request, 'session expire')
        return render(request, 'admin.html')
  except KeyError:
      messages.error(request,'session expire')
      return render(request, 'admin.html')

def adminpage(request):
    if request.session.has_key("user"):
        qs = adminlogin.objects.all()
        return render(request, 'welcomeadmin.html', {'data': qs})
    else:
        messages.error(request,'session expire')
        return render(request,'admin.html')

class Admin_update(SuccessMessageMixin,UpdateView):
    template_name = 'admin_update.html'
    model = adminlogin
    form_class = Adminform
    success_message='Data Saved'
    success_url = '/adminpage/'


def viewpost(request):
    if request.session.has_key('staff'):
        data = Job_Postings.objects.all()
        return render(request, 'viewpost.html', {'data': data})
    else:
        messages.error(request,"Session expired Please Login again")
        return render(request,"staff.html")
def deletepost(request):
    da=request.GET.get('id')
    Job_Postings.objects.filter(Job=da).delete()
    return redirect('viewpost')
def updatepost(request):
    da=request.GET.get("id")
    return render(request,'updatepost.html',{'data':Job_Postings.objects.filter(Job=da)})
def updatejob(request):
    data = Job_Postings.objects.all()
    job = request.POST.get('job')
    title = request.POST.get('name')
    qualification = request.POST.get('qualification')
    percentage = request.POST.get('percentage')
    Experience = request.POST.get('exp')
    Location = request.POST.get('location')
    Salary = request.POST.get('salary')
    Job_Postings.objects.filter(Job=job).update(Title=title,
                 Qualification=qualification,Percentage=percentage,
                 Experience=Experience,Location=Location,
                 Salary=Salary)
    return render(request,'viewpost.html',{"message":"Change Saved Successfully","data":data})
def delete_applicant(request):
    email=request.GET.get('j')
    Applicants.objects.filter(email=email).delete()
    return redirect('showApplicants')

def approve_applicant(request):
    app=request.GET.get('j')
    Applicants.objects.filter(email=app).update(status='Approved')
    return redirect('showApplicants')

def success_Stories(request):
    if request.session.has_key('staff'):
        story_title = request.POST.get("t1")
        Description = request.POST.get("t2")
        image = request.FILES['t3']
        success_stories(story_title=story_title, Description=Description, image=image).save()
        messages.success(request, "Story saved")
        return redirect('success')
    else:
        messages.error(request,"Session Expire Please Login Again")
        return render(request,"staff.html")

def postSaved(request):
    if request.session.has_key('staff'):
        job = request.POST.get('job')
        title = request.POST.get('name')
        qualification = request.POST.get('qualification')
        percentage = request.POST.get('percentage')
        Experience = request.POST.get('exp')
        LastDate = request.POST.get('lastdate')
        Location = request.POST.get('location')
        Salary = request.POST.get('salary')
        Job_Postings(Job=job, Title=title,
                     Qualification=qualification, Percentage=percentage,
                     Experience=Experience, Last_date=LastDate, Location=Location,
                     Salary=Salary).save()
        return render(request, "jobposting.html", {'message': 'Posted Successfully'})
    else:
        messages.error(request,"Session expired Please Login again")
        return render(request,"staff.html")

def agentRegister(request):
    Agent_Name = request.POST.get("name")
    Password = request.POST.get("password")
    Dob = request.POST.get("dateofbirth")
    email=request.POST.get('email')
    Contact_Number = request.POST.get("cno")
    Qualification = request.POST.get("quali")
    Address = request.POST.get("adress")
    image = request.FILES['image']
    CreateAgent(Agent_Name=Agent_Name,Email=email,Password=Password,Dob=Dob,Contact_Number=Contact_Number,Qualification=Qualification,
                Address=Address,image=image).save()
    return render(request,"createagent.html",{'message':'Created Successfully'})

def viewAgents(request):
    qs = CreateAgent.objects.all()
    return render(request,"viewallagents.html",{'data':qs})

def updateagent(request):
    qs = CreateAgent.objects.all()
    return render(request, "updateagent.html", {'data': qs})

class Editagent(SuccessMessageMixin,UpdateView):
    model = CreateAgent
    template_name = "editedagent.html"
    form_class = Agent
    success_message = 'Data Updated'
    success_url = '/editagent/'

def delete_agent(request):
    id=request.GET.get('id')
    CreateAgent.objects.filter(id=id).delete()
    return  redirect('editagent')

def viewJobs(request):
    job=request.GET.get('j')
    qs = Job_Postings.objects.filter(Job =job)
    if qs:
        return render(request,"viewjobs.html",{'data':qs})
    else:
        return render(request,'viewjobs.html')

def apply_job(request):
    job=request.GET.get('job')
    da = Job_Postings.objects.filter(Job=job)
    return render(request,'apply_jobs.html',{"data":da})
def suggest(request):
    name = request.POST.get("name")
    location = request.POST.get("location")
    suggession = request.POST.get('suggession')
    Tips(Name=name,Location=location,Suggession=suggession).save()
    messages.success(request,"Thank you for your suggestion")
    return render(request,"tips.html")

def viewApplicants(request):
    JOB_TITLE = request.POST.get("name")
    FN = request.POST.get("fn")
    LN = request.POST.get("g")
    Dob = request.POST.get("dob")
    Qualification = request.POST.get("quali")
    percentage = request.POST.get("percentage")
    Institute = request.POST.get("institute")
    Experience = request.POST.get("exp")
    Contact_Number = request.POST.get("cno")
    email=request.POST.get("email")
    try:
        if Qualification!='Select':
            if len(Contact_Number) == 10:
                print(percentage)
                Applicants(JOB_TITLE=JOB_TITLE, Name=FN, Gender=LN, Dob=Dob, Qualification=Qualification,
                           percentage=percentage, Institute=Institute, email=email, Experience=Experience,
                           Contact_Number=Contact_Number).save()
                return render(request, "findjobs.html", {'message': 'saved'})
            else:
                messages.error(request, 'enter correct data')
                da = Job_Postings.objects.filter(Job=JOB_TITLE)
                return render(request, 'apply_jobs.html', {"data": da})
        else:
            messages.error(request, 'Please Select Qulification')
            da = Job_Postings.objects.filter(Job=JOB_TITLE)
            return render(request, 'apply_jobs.html', {"data": da})
    except IntegrityError:
        messages.error(request,"Details already Saved")
        return render(request,"apply_jobs.html")

def showApplicants(request):
    if request.session.has_key('staff'):
        qs = Applicants.objects.all()
        return render(request, "showapplicants.html", {'data': qs})
    else:
        messages.error(request,"session expire")
        return render(request,"staff.html")

def case_details(request):
    if request.session.has_key('agent'):
        data = request.session['agent']
        case = Assign_Agent.objects.filter(agent_id=data['agent_id'])
        return render(request,"casedetails.html",{"case":case,"name":data['Agent_Name']})
    else:
        messages.error(request, "Session Expire")
        return render(request, 'agent_login.html')

def agent(request):
    email = request.POST.get("t1")
    Password = request.POST.get("t2")
    #print(email,Password,"hi")
    res = CreateAgent.objects.filter(Email=email,Password=Password)
    if res:
        res = CreateAgent.objects.filter(Email=email, Password=Password).values("Agent_Name","agent_id","image").distinct()
        request.session['agent'] = res[0]
        data=request.session['agent']
        request.session.set_expiry(0)
        if request.session.has_key("agent"):
            return render(request, "welcomeagent.html",{"data":data})
        else:
            messages.error(request, "Session expire")
            return render(request, 'agent_login.html')
    else:
        messages.error(request,"Wrong ID or Password") 

def agent_logout(request):
    try:
        if request.session.has_key("agent"):
            del request.session['agent']
            return render(request, 'agent_login.html')
        else:
            messages.error(request, 'session expire')
            return render(request, 'agent_login.html')
    except KeyError:
        messages.error(request, 'session expire')
        return render(request, 'agent_login.html')


def assign_Agent(request):
    id = request.POST.get("agent_id")
    case_id=request.POST.get("p1")
    if case_id!='Select':
         try:
           Assign_Agent(CaseCreation_Agent_id=case_id,agent_id=id).save()
           return render(request,"appoint_agent.html",{'message':'Assign Successfully'})
         except IntegrityError:
             messages.error(request, "Case is already taken or u have not selected the case ")
             return redirect('appoint_agent')


def showAgent(request):
    if request.session.has_key("user"):
        Agent_Name = request.POST.get('name')
        qs = CreateAgent.objects.filter(Agent_Name=Agent_Name)
        if qs:
            data = qs[0].agent_id
            d1 = CaseCreation.objects.all()
            return render(request, "appointcaseid.html", {'qs': data, 'qs1': d1})
        else:
            messages.success(request, "Please select the Agent")
            return redirect('appoint_agent')
    else:
        messages.error(request, 'session expire')
        return render(request, 'admin.html')


def getDetails(request):
    if request.session.has_key('agent'):
        data = request.session['agent']
        case = Assign_Agent.objects.filter(agent_id=data['agent_id'])
        case_id = request.POST.get("case_id")
        if case_id != "Select":
            qs = CaseCreation.objects.filter(case_id=case_id)
            if qs:
                return render(request, "agent_case.html", {'data': qs,"name":data['Agent_Name']})
            else:
                messages.error(request, 'Please Choose the case id')
                return render(request, "casedetails.html", {"case": case,"name":data['Agent_Name']})
        else:
            messages.error(request, 'Please Choose the case id')
            return render(request, "casedetails.html", {"case": case,"name":data['Agent_Name']})
    else:
        messages.error(request, "Session Expire")
        return render(request, 'agent_login.html')


def upDetails(request):
    qs = CaseDetails.objects.all()
    return render(request,"updateevidence.html",{"data":qs})

class UpEvidence(SuccessMessageMixin,UpdateView):
    model = CaseCreation
    template_name = "editevidence.html"
    fields = ('case_name','file','status')
    success_message = "Case Updated"
    success_url = '/case_details/'

def defencepage(request):
    dfrom=Defenceform()
    return render(request,"defence_login.html",{"form":dfrom})
def defence(request):
    df=Defenceform(request.POST)
    data=request.POST.copy()
    usera=data.get('username')
    pas=data.get('password')
    res=Defence_Login.objects.filter(username=usera,password=pas)
    if res and df.is_valid():
        details = Defence_Login.objects.filter(username=usera).values("id","username","password").distinct()
        request.session['user'] = details[0]
        request.session.set_expiry(0)
        if request.session.has_key('user'):
             return render(request, "welcomedefence.html")
        else:
            messages.error(request,"session expired")
            return render(request,"defence_login.html")
    else:
        messages.error(request,'Invalid User')
        return render(request,"defence_login.html",{"form":df})
def caselogout(request):
    try:
        if request.session.has_key('user'):
            request.session.flush()
            return render(request, 'defence_login.html',{"form":Defenceform()})
        else:
            messages.error(request, 'session expire')
            return render(request, 'defence_login.html',{"form":Defenceform()})
    except KeyError:
        messages.error(request, 'session expire')
        return render(request, 'defence_login.html',{"form":Defenceform()})

def casecreationpage(request):
    if request.session.has_key('user'):
        return render(request,"casecreation.html")
    else:
        messages.error(request, 'session expire')
        return render(request, 'defence_login.html', {"form": Defenceform()})
def create_Case(request):

        case_name = request.POST.get("case name")
        doc = request.POST.get("date")


        file = request.FILES['file']
        CaseCreation(case_name=case_name, file=file, doc=doc).save()
        messages.success(request, "Successfully Created The Case")
        return redirect('casecreation')

def agentmanage(request):
    if request.session.has_key('user'):
        return render(request,"agent_manage.html")
    else:
        messages.error(request, 'session expire')
        return render(request, 'admin.html')


def adminreport(request):
    if request.session.has_key('user'):
        data=Assign_Agent.objects.all().values('agent_id','CaseCreation_Agent_id',"CaseCreation_Agent__case_name","CaseCreation_Agent__status","CaseCreation_Agent__file").distinct()
        f=CaseCreation.objects.all()
        return render(request, "report_admin.html", {'data': data,"file":f})
    else:
        messages.error(request, 'session expire')
        return render(request, 'admin.html')


def defencereport(request):
    if request.session.has_key('user'):
        data=Assign_Agent.objects.all().values('agent_id','CaseCreation_Agent_id',"CaseCreation_Agent__case_name","CaseCreation_Agent__status").distinct()
        return render(request, "report_defence.html", {'data': data})
    else:
        messages.error(request, 'session expire')
        return render(request, 'defence_login.html')


def allStories(request):
    qs = success_stories.objects.all()
    return render(request,"allstories.html",{'data':qs})


def delete_story(request,story_id):
    if request.session.has_key('staff'):
        stroy = get_object_or_404(success_stories, pk=story_id)
        stroy.delete()
        return redirect('delete_success')
    else:
        messages.error(request,"SessionExpired Please Login Again")
        return render(request,"staff.html")
def st_page(request):
    if request.session.has_key('staff'):
        data=request.session['staff']
        return render(request, 'st_page.html',{"data":data})
    else:
        messages.error(request, "Session expire")
        return render(request, "staff.html")

def check_staff(request):
    em=request.POST.get('email')
    ps=request.POST.get("pass")
    res=Staff.objects.filter(Email=em,Password=ps).values('Email','Photo','Username','Status').distinct()
    if res:
        if res[0]['Status']=='Approved':
            request.session['staff'] = res[0]
            data=request.session['staff']
            request.session.set_expiry(0)
            if request.session.has_key('staff'):
                return render(request, 'st_page.html',{"data":data})
            else:
                messages.error(request, "Session expire")
                return render(request, "staff.html")
        else:
            messages.error(request,"Your account is not approved")
            return redirect('staff')
    else:
        messages.error(request,'Invalid Email id or password')
        return redirect('staff')

def staff_logout(request):
    try:
        if request.session.has_key("staff"):
            del request.session['staff']
            return render(request, "staff.html")
        else:
            messages.error(request, "Session expire")
            return render(request, "staff.html")
    except KeyError:
        messages.error(request, "Session expire")
        return render(request, "staff.html")

class St_regist(SuccessMessageMixin,CreateView):
        template_name = 'st_regist.html'
        model = Staff
        form_class = Staff_validation
        success_message = "Successfully Saved"
        success_url = "/st_regist/"


def approve_staff(request):
    if request.session.has_key('user'):
        id = request.GET.get("id")
        Staff.objects.filter(idno=id).update(Status='Approved')
        return redirect('approve_staff')
    else:
        messages.error(request, 'session expire')
        return render(request, 'admin.html')

def save_pass(request):
    email=request.POST.get('email')
    pas=request.POST.get('pas')
    c_pas=request.POST.get('c_pas')
    result=Staff.objects.filter(Email=email).values('Status','Password').distinct()
    print(result)
    if result:
        if result[0]["Status"] == 'Approved':
            if pas==c_pas:
                Staff.objects.filter(Email=email).update(Password=c_pas)
                messages.error(request, 'Password Updated')
                return render(request, 'staff.html')
            else:
                messages.error(request, "Password not match")
                return redirect('forget_pass')
        else:
            messages.error(request, "Your Email Id not Approved")
            return redirect('forget_pass')
    else:
        messages.error(request,"Email Id not found Please Register")
        return redirect('forget_pass')
