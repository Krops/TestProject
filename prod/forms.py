from django.forms import CharField, ModelForm, BooleanField
from django.forms import TextInput, CheckboxInput
from prod.models import Comment, Vote


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
    message = CharField(max_length=300, required=True)
