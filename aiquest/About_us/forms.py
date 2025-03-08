from django import forms
from django.core import validators 

class TeachersRegistration(forms.Form):
    first_name = forms.CharField(label="Enter Your First Name", label_suffix=' ')
    last_name = forms.CharField(initial='StudyMart', disabled=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)
    
    def clean(self):
        clean_data =  super().clean()
        rightpassword = self.cleaned_data["password"]
        wrongpassword = self.cleaned_data["repassword"]
        
        if rightpassword != wrongpassword:
            raise forms.ValidationError('Passwored not mach')
            
        
        
    


        
        