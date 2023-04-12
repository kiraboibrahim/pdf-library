from pathlib import Path
from django.core.exceptions import ValidationError


class PDFRequired:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, file):
        if Path(file.name).suffix.lower() != ".pdf":
            raise ValidationError("PDF file is required")
        # Decode the first 4 bytes of PDF file, If pdf file, first 4 bytes of file = %PDF
        with file.open("rb") as f:
            first_four_bytes = f.read(4)
            if first_four_bytes.decode("ascii", errors="ignore") != "%PDF":
                raise ValidationError("PDF file is required")
        return file


class NonMaliciousPDFRequired:

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, file):
        """TODO: Implement this to screen against malicious PDF, Scan for Javascript and OpenAction objects"""
        return file
