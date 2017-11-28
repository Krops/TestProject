from django.forms import CharField, ModelForm
from prod.models import Comment, Vote


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['form_message']

    form_message = CharField(max_length=300, required=True)
