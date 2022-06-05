from django import forms
from django.forms import ModelForm

from pybo.models import Question, Answer, Comment


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content','mainphoto']

        labels = {
            'subject': '제목',
            'content': '내용',
            'mainphoto' : '사진'
        }



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }