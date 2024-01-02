from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm) :
    class Meta :
        model = Question
        fields = [ 'subject', 'content' ]


class AnswerForm(forms.ModelForm) :
    class Meta :
        model = Answer
        fields = [ 'content' ]
        labels =  { 'content' : '답변내용' }