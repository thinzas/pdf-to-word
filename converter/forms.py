from django import forms

class UploadPDFForm(forms.Form):
    pdf_file =  forms.FileField(label="select a PDF file")