from django import forms
from .models import KobePost

class postForm(forms.ModelForm):

    class Meta:
        model = KobePost
        fields = '__all__'
        exclude = {'check', 'checkPosted', 'ipAddress', 'token', 'postId'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nickname'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['content'].widget.attrs.update({'class': 'form-control form-control-lg'})
