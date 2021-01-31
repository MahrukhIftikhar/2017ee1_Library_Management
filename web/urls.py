
from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    
    path('index1.html',views.index, name = 'home1'),
    path('',views.index, name = 'home'),
    path('index.html',views.indexView, name = 'home'),
    path('dashboard.html',views.contact, name ="dashboard"),
    path('register.html',views.register,name = "register"),
    path('login.html',views.login,name = "login"),
    path('loginad.html',views.login1,name = "login1"),
    path('loginst.html',views.login2,name = "login2"),
    path('userlogin.html',views.loginuser,name = "loginu"),
    path('view.html',views.view,name="view"),
    path('books.html',views.booksView,name = "book_url"),
    path('booknad.html',views.bookView,name = "book"),
    path('staff.html',views.staffView,name = "staff_url"),
    path('user.html',views.userView,name = "user_url"),
    path('suser.html',views.usersView,name = "users"),
    path('sbook.html',views.sbookView,name = "sbook"),
    path('loan.html',views.loanView,name = "loan_url"),
    path('publisher.html',views.pubView,name = "pub_url"),
    path('service.html',views.serView,name = "ser_url"),
    path('about.html',views.abView,name = "ab_url"),
    path('contact.html',views.coView,name = "co_url"),
    path('edit/<int:ISNB>',views.ebView),
    path('update/<int:ISNB>',views.updatebook),
    path('delete/<int:ISNB>',views.dbView),
    path('edit/<int:SSN>/',views.esView),
    path('delete/<int:SSN>/',views.dsView),
    path('update/<int:SSN>/',views.updatestaff),
    path('edit/<int:SSN>/<int:ISNB>',views.elView),
    path('delete/<int:SSN>/<int:ISNB>',views.dlView),
    path('update/<int:SSN>/<int:ISNB>',views.updateloan),
    path('edit/<int:ID>//',views.epView),
    path('delete/<int:ID>//',views.dpView),
    path('update/<int:ID>//',views.updatepub),
    path('edit/<int:SSN>/&',views.euView),
    path('delete/<int:SSN>/&',views.duView),
    path('update/<int:SSN>/&',views.updateuser),
    path('adduser.html',views.useradd,name="adduser_url"),
    path('addbook.html',views.bookadd,name="addbook_url"),
    path('addloan.html',views.loanadd,name="addloan_url"),
    path('lendbook.html',views.lend,name="uloan_url"),
    path('slend.html',views.slend,name="sloan_url"),
    path('addstaff.html',views.staffadd,name="addstaff_url"),
    path('addpub.html',views.pubadd,name="addpub_url"),
    path('hi/',views.emailsend,name="email"),
]
