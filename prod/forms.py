from django.forms import CharField, ModelForm, BooleanField
from django.forms import TextInput, CheckboxInput, ModelChoiceField
from prod.models import Comment, Vote


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

    message = CharField(max_length=300, required=True)
