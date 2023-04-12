import jinja2
from django.templatetags.static import static
from django.urls import reverse
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_form


class Environment:

    def __call__(self, **options):
        env = jinja2.Environment(**options)
        env.globals.update({
            "static": static,
            "url": reverse,
            "crispy": as_crispy_form,
        })
        return env


environment = Environment()
