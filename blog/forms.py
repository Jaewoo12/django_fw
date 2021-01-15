from django import forms
from .models import Post,Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)

class PostModelform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)

# title 입력필드의 길이 체크 <3
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('Title은 3글자 이상 입력해주세요')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget=forms.Textarea)

