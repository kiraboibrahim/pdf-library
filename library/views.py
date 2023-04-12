from functools import cached_property

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book
from .mixins import BookUploaderRequiredMixin
from .forms import BookUploadForm


class BookListView(ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"


class BookUpdateView(LoginRequiredMixin, BookUploaderRequiredMixin, UpdateView):
    model = Book
    pk_url_kwarg = "book_id"

    @cached_property
    def get_object(self, queryset=None):
        return super().get_object(queryset)


class BookDeleteView(LoginRequiredMixin, BookUploaderRequiredMixin, DeleteView):
    model = Book

    @cached_property
    def get_object(self, queryset=None):
        return super().get_object(queryset)


class DMCAViolationReportView(SingleObjectMixin, View):
    pk_url_kwarg = "book_id"
    model = Book

    def get(self, request, *args, **kwargs):
        """TODO: Log DRMA notice in database and notify the user that uploaded the book"""
        pass


class BookCategoryListView(ListView):
    model = Book
    template_name = "library/book_category_list.html"
    context_object_name = "book_categories"


class UploadBookView(LoginRequiredMixin, CreateView):
    form_class = BookUploadForm
