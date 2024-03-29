from django.contrib.auth.decorators import login_required

from .. import models
from django.shortcuts import render

#@login_required(login_url='common:login')
def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "pybo/upload-file.html", context = {
        "files": documents
    })