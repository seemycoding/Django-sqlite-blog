from django import forms
from django.core.validators import validate_email

class registrationForm(forms.Form):
    firstName=forms.CharField(label="First Name",max_length=50)
    email=forms.EmailField(label="Email",max_length=50,required=True)
    password=forms.CharField(label="Password",widget=forms.PasswordInput,required=True,min_length=6)
    confirmPassword=forms.CharField(label="Confirm Password",widget=forms.PasswordInput,required=True,min_length=6)






   # def clean_email(self):
    #    data=self.cleaned_data['email']
     #   validData=validate_email(data)
      #  if not validData:
       #     raise forms.ValidationError("Email typed is not correct")
       # return data
            


class loginForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,required=True)
    password=forms.CharField(label="Password",widget=forms.PasswordInput,required=True,min_length=6)
    



