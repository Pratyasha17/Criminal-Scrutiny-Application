from django.conf.urls.static import static
from app_cybernatics_protetor import views
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from app_cybernatics_protetor.models import CreateAgent, Staff
from cybernatics_protetor import settings
from app_cybernatics_protetor.models import success_stories , Tips, Job_Postings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="home.html"),name='home'),
    #home index stories
    path('stories/',TemplateView.as_view(template_name='Stories.html')),
    path('story1/',TemplateView.as_view(template_name='story1.html')),
    path('story2/', TemplateView.as_view(template_name='story2.html')),
    path('all_stories/',views.allStories),
    #find jobs
    path('find_jobs/',ListView.as_view(template_name="findjobs.html",model=Job_Postings),name='find_jobs'),
    path('viewjobs/',views.viewJobs,name='viewjobs'),
    path('apply_jobs/',views.apply_job,name='apply_job'),
    path('applicant/',views.viewApplicants,name="applicant"),
    path('applyclerkjobs/',ListView.as_view(template_name="apply_clerkjobs.html",model=Job_Postings)),
    path('clerk_applicant/',views.viewApplicants),
    #tips n suggestions
    path('tips/',TemplateView.as_view(template_name="tips.html")),
    path('suggest/',views.suggest),
    path('showtips/',ListView.as_view(template_name='showtips.html',model=Tips)),
    path('about/',TemplateView.as_view(template_name="aboutus.html")),
    #admin path #
    path('adminlogin/',TemplateView.as_view(template_name="admin.html")),
    path('welcomeadmin/',views.adminLogin,name='welcomeadmin'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('update_data<int:pk>/',views.Admin_update.as_view(),name="update_data"),
    path('viewpost/',views.viewpost,name='viewpost'),
    path('deletepost/',views.deletepost,name='deletepost'),
    path('updatepost/',views.updatepost,name='updatepost'),
    path('updatejob/',views.updatejob,name='updatejob'),
    path('delete_applicant/',views.delete_applicant,name='delete_applicant'),
    path('approve_applicant/',views.approve_applicant,name='approve_applicant'),
    # admin side index #
    path('sucees/',TemplateView.as_view(template_name="successtories.html"),name='success'),
    path('delete_success/',ListView.as_view(template_name="delete_stories.html",model=success_stories),name='delete_success'),
    path('<int:story_id>/',views.delete_story,name='delete_story'),
    path('succestories/',views.success_Stories),

    #job postings#
    path('job/',TemplateView.as_view(template_name="jobposting.html")),
    path('postsaved/',views.postSaved),
    #viewapplicants
    path('viewapplicants/',views.showApplicants,name='showApplicants'),
    #appoin agent
    path('app_agent/',ListView.as_view(template_name="appoint_agent.html",model=CreateAgent),name="appoint_agent"),
    path("assign_agent/",views.showAgent,name='assign_agent'),
    path('savecasedetails/',views.assign_Agent),
    #agent_manage
    path('agentmanage/',views.agentmanage),
    #create agent
    path('createagent/',TemplateView.as_view(template_name="createagent.html")),
    path('agentregister/',views.agentRegister),
    #view all agent
    path('viewallagents/',views.viewAgents),
    #edit agent
    path('editagent/',views.updateagent,name='editagent'),
    path('update<int:pk>/',views.Editagent.as_view(),name="update"),
    path('delete_agent/', views.delete_agent,name='delete_agent'),
    #reports
    path('reports_admin/',views.adminreport),
    path('reports_defence/',views.defencereport),

    #admin logout
    path('admin_logout/',views.admin_logout),
    #agent login
    path('agent_login/',TemplateView.as_view(template_name="agent_login.html"),name='agent_login'),
    path('agentsign/',views.agent,name="agent"),
    #case details
    path('case_details/',views.case_details,name="case_details"),
    path('agentcase/',views.getDetails),
    #Update Evidences
    path('update_evidence/',views.upDetails),
    path('upevidence<int:pk>/',views.UpEvidence.as_view(),name='upevidence'),
    #agent_logout/
    path('agent_logout/',views.agent_logout),
    #defence of minstry
    path('ministry/',views.defencepage,name='case'),
    path('welcomedefence/',views.defence,name='welcomedefence'),
    #case creation
    path('case_creation/',views.casecreationpage,name='casecreation'),
    path('create_case/',views.create_Case),
    #defence_logout/
    path('defence_logout/',views.caselogout,name="defence_logout"),
    #staff details/
    path("staff/",TemplateView.as_view(template_name='staff.html'),name='staff'),
    path("check_staff/",views.check_staff,name='check_staff'),
    path('st_regist/',views.St_regist.as_view(),name='st_regist'),
    path('staff_logout/',views.staff_logout),
    path('approve_staff/',ListView.as_view(template_name="approve_staff.html",model=Staff),name='approve_staff'),
    path('approve/',views.approve_staff,name='approve'),
    path("forget_pass/",TemplateView.as_view(template_name='forget_pass.html'),name='forget_pass'),
    path("save_pass/",views.save_pass,name='save_pass'),
    path('st_page/',views.st_page),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)