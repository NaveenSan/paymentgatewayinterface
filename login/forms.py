from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=55)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ['username','password']


class donation(forms.Form):
    amount = forms.IntegerField()
    class Meta:
        fields = ['amount']