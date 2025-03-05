from django.urls import path
from .views import upload_pdf, pdf_list, pdf_view, delete_pdf

urlpatterns = [
    path("", pdf_list, name="home"),  # Set PDF list as the default homepage
    path("upload/", upload_pdf, name="upload_pdf"),
    path("pdfs/", pdf_list, name="pdf_list"),
    path("pdf/<int:pdf_id>/", pdf_view, name="pdf_view"),
    path("pdf/delete/<int:pdf_id>/", delete_pdf, name="delete_pdf"),
]
