from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, **kwargs):
        self._user = user
        super(AskForm, self).__init__(self.base_fields)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def __init__(self, user, **kwargs):
        self._user = user
        super(AnswerForm, self).__init__(**kwargs)

    def clean_question(self):
        question = self.cleaned_data['question']
        try:
            self.question = Question.objects.get(question)
            return question
        except:
            raise forms.ValidationError('Question not found')

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
