from django import forms 

         #models helps create entry in db in django

class LoginForm(forms.Form):
    username=forms.CharField(            #1st field in form is email field ye python m built in format h
        max_length=30,
        min_length=1,
        required=True,
        widget=forms.TextInput(        #kya kya input h email fild m
            attrs={
                "placeholder":"UserName",
                "class":"form-control"
            }
        )
    )
    password=forms.CharField(
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Password",
                "class":"form-control"
            }
        )
    )
    