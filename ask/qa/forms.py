from django.forms import forms

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, **kwargs):
        self._user = user
        super(AskForm, self).__init__(**kwargs)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.TextField(widget=forms.Textarea)
    question = forms.CharFeld()

    def clean_question(self):
        question = self.cleaned_data['question']
        try:
            question = Question.objects.get(question)
            return question
        except:
            raise forms.ValidationError

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
