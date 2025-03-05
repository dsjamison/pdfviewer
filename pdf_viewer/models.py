from django.db import models

class UploadedPDF(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to="uploads/pdfs/")
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically set the title to the filename without extension
        if not self.title:
            self.title = self.pdf_file.name.split("/")[-1].split(".")[0]
        super().save(*args, **kwargs)



    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",") if tag]

    def __str__(self):
        return self.title
