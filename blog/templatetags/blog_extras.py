from django import template
register = template.Library()
from django.contrib.auth import get_user_model
user_model = get_user_model()
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe


@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    return ""

  if author == current_user:
    return format_html("<strong> me </strong>")

  if author.first_name and author.last_name:
    # name = escape(f"{ author.first_name } { author.last_name }")
    name = f"{ author.first_name } { author.last_name }"

  else:
    # name = escape(f"{author.username}")
    name = f"{author.username}"

  if author.email:
    # email = escape(author.email)
    prefix = format_html("<a href='mailto:{}'>", author.email)
    sufix = format_html("</a>")
  else:
    prefix = ''
    sufix = ''

  # return mark_safe(f"{prefix}{name}{sufix}")
  return format_html('{}{}{}', prefix, name , sufix)