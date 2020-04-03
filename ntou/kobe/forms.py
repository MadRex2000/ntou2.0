from django import forms
from .models import KobePost, registrationReviewer

class deleteForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deleteToken'].widget.attrs.update({'class': 'form-control form-control-lg'})

    deleteToken = forms.CharField(label = 'Token')

class postForm(forms.ModelForm):

    class Meta:
        model = KobePost
        fields = '__all__'
        exclude = {'check', 'checkPosted', 'ipAddress', 'token', 'postId'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nickname'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['content'].widget.attrs.update({'class': 'form-control form-control-lg'})

class registerForm(forms.ModelForm):

    class Meta:
        model = registrationReviewer
        fields = '__all__'
        exclude = {'registerIpAddress',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['reviewerNickName'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['mail'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['telegramId'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['department'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['grade'].widget.attrs.update({'class': 'form-control form-control-lg'})
