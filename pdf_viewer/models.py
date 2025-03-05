from django.db import models

class UploadedPDF(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to="uploads/pdfs/")
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")

    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",") if tag]

    def __str__(self):
        return self.title
