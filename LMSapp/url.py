from django.contrib import admin
from django.urls import path
from LMSapp import views

app_name = "LMSapp"


urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.u1login,name="u1login"),
    path('delete',views.delete,name="delete"), #taken for the 2ndu for deteltion of students
    path("active/<int:student_id>/<str:action>/", views.active, name="active"), #taken for the 2ndu for deactivating the users in here
    path('admin1/<int:id>',views.admin1,name="admin1"), #taken for the 2ndu for login to admin page
    # path('adminedit/<int:p>',views.adminedit,name="adminedit"), #taken for the 2ndu for login to admin page
    path('adminparent',views.adminparent,name="adminparent"),# taken for 2ndu only for showing parents
    # path('adminstaff',views.adminstaff,name="adminstaff"),   # only for showing class
    path('adminstudent',views.adminstudent,name="adminstudent"), #taken for the 2ndu for showing the student
    path('adminparent1/<int:id>',views.adminparent1,name="adminparent1"), #taking for the 2ndu all the details about parents
    path('adminparent1create',views.adminparent1create,name="adminparent1create"), #taking for 2ndu for the creation of parents
    # path('adminparentedit/<str:p>/<str:m>',views.adminparentedit,name="adminparentedit"), #editing the parents
    # path('adminstaff1/<str:p>',views.adminstaff1,name="adminstaff1"),  #taking all the details about staff
    # path('adminstaffedit/<str:p>/<str:m>',views.adminstaffedit,name="adminstaffedit"), # editing the dtaffs
    # path('adminstudentcreate',views.adminstudent,name="adminstudent"), #taking all the details about student
    # path('adminstudentedit/<str:p>/<str:m>', views.adminstudentedit,name="adminstudentedit"),  # editing the students
    # path('createuser', views.createuser,name="createuser"),
    # path('staffstudent',views.staffstudent,name="staffstudent"), # showing the class associated with the each class for staff
    # path('staffclass/<str:p>',views.staffclass,name="staffclass"), # showing the subjects associated with the each class for staff
    path('class_detail/<str:p>',views.class_detail,name="class_detail"),
    path('class_detail_parent/<str:p>',views.class_detail_parent,name="class_detail_parent"),
    path('adminstudentcreate',views.adminstudentcreate,name="adminstudentcreate"),

]
