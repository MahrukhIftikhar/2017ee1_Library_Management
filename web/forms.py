from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from web.models import BookDetails,StaffDetails,LoanDetails,UserDetails,PubDetails
from django import forms

class RegisterForm(UserCreationForm):
    SSN = forms.CharField(max_length = 100)
    L_name = forms.CharField(max_length = 100)
    Address = forms.CharField(max_length = 100)
    email = forms.EmailField()
    catagery = forms.CharField(max_length = 100)
    phone_no = forms.CharField(max_length = 100)
    class Meta:
        model = User
        fields = ["SSN","username","L_name","Address","email","password1","password2","catagery","phone_no"]

class bookForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = ['ISNB','price','noofcopies','title','edition','author', 'pbid', 'status', 'catagery']
class staffForm(forms.ModelForm):
    class Meta:
        model = StaffDetails
        fields = ['SSN','F_name','L_name','Address','salary','specified_task']
class loanForm(forms.ModelForm):
    class Meta:
        model = LoanDetails
        fields = ['SSN','ISNB','issue_date','return_date','fine']
class pubForm(forms.ModelForm):
    class Meta:
        model = PubDetails
        fields = ['ID','Name','pub_year']
class userForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['SSN','F_name','L_name','Address','email_id','password', 'catagery', 'phone_no']        
      
   