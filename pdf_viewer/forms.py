from django import forms
from .models import UploadedPDF

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedPDF
        fields = ["title", "pdf_file", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pdf_file"].widget.attrs.update({"multiple": True})  # Allow multiple file selection



        # widgets = {
        #     "title": forms.TextInput(attrs={"placeholder": "Enter title"}),
        #     "pdf_file": forms.ClearableFileInput(attrs={"accept": ".pdf"}),
        # }
