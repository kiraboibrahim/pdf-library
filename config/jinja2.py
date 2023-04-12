import jinja2
from django.templatetags.static import static
from django.urls import reverse
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_form
from library.forms import BookUploadForm


class Environment:

    def __call__(self, **options):
        env = jinja2.Environment(**options)
        request = env.globals.get("request")
        env.globals.update({
            "static": static,
            "url": reverse,
            "crispy": as_crispy_form,
            "book_upload_form": BookUploadForm(),
        })
        return env


environment = Environment()
