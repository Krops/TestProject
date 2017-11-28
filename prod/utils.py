from django.http import HttpResponse
import json
from django.db.models import DateField
import datetime
from io import StringIO
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from PIL import Image


def convert_context_to_json(context):
    u""" This method serialises a Django form and
    returns JSON object with its fields and errors
    """
    form = context.get('form')
    to_json = {}
    options = context.get('options', {})
    to_json.update(options=options)
    to_json.update(success=context.get('success', False))
    fields = {}
    for field_name, field in form.fields.items():
        if isinstance(field, DateField) \
                and isinstance(form[field_name].value(), datetime.date):
            fields[field_name] = form[field_name].value().strftime('%d.%m.%Y')
        else:
            fields[field_name] = \
                form[field_name].value() \
                and form[field_name].value() \
                or form[field_name].value()
    to_json.update(fields=fields)
    if form.errors:
        errors = {
            'non_field_errors': form.non_field_errors(),
        }
        fields = {}
        for field_name, text in form.errors.items():
            fields[field_name] = text
        errors.update(fields=fields)
        to_json.update(errors=errors)
    return json.dumps(to_json)


def render_to_json_response(context, **response_kwargs):
    data = json.dumps(context)
    response_kwargs['content_type'] = 'application/json'
    return HttpResponse(data, **response_kwargs)
