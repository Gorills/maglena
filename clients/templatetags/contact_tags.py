from django import template
from clients.forms import ContactForm

register = template.Library()


@register.inclusion_tag('clients/tags/form.html')
def contact_form():
    return {'contact_form': ContactForm()}