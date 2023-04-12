from django.contrib.auth.mixins import UserPassesTestMixin


class BookUploaderRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().is_uploader(self.request.user)

