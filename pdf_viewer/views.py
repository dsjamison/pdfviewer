from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadedPDF
from .forms import PDFUploadForm
from django.core.paginator import Paginator
from django.db.models import Q

def upload_pdf(request):
    if request.method == "POST":
        # form = PDFUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        files = request.FILES.getlist("pdf_file")  # Get multiple files
        for file in files:
            UploadedPDF.objects.create(title=file.name, pdf_file=file)
        return JsonResponse({"message": "Files uploaded successfully"}, status=200)
    #         return redirect("pdf_list")
    # else:
    # form = PDFUploadForm()
    # return render(request, "pdf_viewer/upload_pdf.html", {"form": form})
    return render(request, "pdf_viewer/upload_pdf.html", )

def pdf_list(request):
    query = request.GET.get("q", "")
    tag_filter = request.GET.get("tag", "")
    pdfs = UploadedPDF.objects.all().order_by("title") #("-uploaded_at")

    if query:
        pdfs = UploadedPDF.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))

    if tag_filter:
        pdfs = pdfs.filter(tags__icontains=tag_filter)

    paginator = Paginator(pdfs, 5)  # Show 5 PDFs per page
    page_number = request.GET.get("page")
    pdfs_page = paginator.get_page(page_number)

    tags = set(tag for pdf in UploadedPDF.objects.all() for tag in pdf.tag_list())

    return render(request, "pdf_viewer/pdf_list.html", {"pdfs": pdfs_page, "query": query, "tags": sorted(tags), "tag_filter": tag_filter})

def pdf_view(request, pdf_id):
    pdf = get_object_or_404(UploadedPDF, id=pdf_id)
    return render(request, "pdf_viewer/pdf_viewer.html", {"pdf": pdf})

def delete_pdf(request, pdf_id):
    pdf = get_object_or_404(UploadedPDF, id=pdf_id)
    if request.method == "POST":
        pdf.delete()
        return redirect("pdf_list")

    return render(request, "pdf_viewer/delete_confirm.html", {"pdf": pdf})
