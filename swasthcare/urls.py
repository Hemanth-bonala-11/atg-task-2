from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.home,name="home"),
    path('about',views.about,name='about'),
    path('doctor_login',views.doctor_login,name='doctor_login'),
    path('patient_login',views.patient_login,name='patient_login'),
    path('contact',views.contact,name="contact"),
    path('success_contact',views.success_contact,name="message_sent"),
    path('doctor_signup',views.doctor_signup,name="doctor_signup"),
    path('patient_signup',views.patient_signup,name="patient_signup"),
    path('login_doctor',views.doctor_login_after_signup,name="doctor_signup_completed"),
    path('patient_dashboard',views.patient_dashboard,name="dashboard"),
    path('doctor_dashboard',views.doctor_dashboard,name="doctor_dashboard"),
    path('login_patient',views.patient_login_after_signup,name="patient_signup_completed"),
    path('loggedout',views.logged_out,name="logout"),
    path('address',views.address,name="address"),
    path('blog_save',views.save_blogs,name="save"),
    path('your_published_blogs',views.see_your_blogs,name='blogs'),
    path('saved_as_draft',views.save_draft,name='draft'),
    path('blog_page/<str:uniqueid>',views.blog_page,name="blog_page"),
    path('blogs',views.all_blogs,name="all_blogs")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)