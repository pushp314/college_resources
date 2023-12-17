# resources/forms.py
from django import forms
from .models import Resource, Note, Ebook, Link, Video, Image, Document

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'uploader', 'resource_type']

class UpdateResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description']

class DeleteResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = []  # No fields are needed for delete operation


#----------------------------------------------------------------#


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['author', 'publication_year', 'file']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['file']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_file']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']




class UploadForm(forms.Form):
    resource_type = forms.ChoiceField(choices=[
        ('note', 'Note'),
        ('ebook', 'Ebook'),
        ('link', 'Link'),
        ('video', 'Video'),
        ('image', 'Image'),
        ('document', 'Document'),
    ])
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    # Fields specific to each resource type
    content = forms.CharField(required=False, widget=forms.Textarea, label='Content')  # For Note
    author = forms.CharField(required=False, max_length=100, label='Author')  # For Ebook
    publication_year = forms.IntegerField(required=False, label='Publication Year')  # For Ebook
    url = forms.URLField(required=False, label='URL')  # For Link
    file = forms.FileField(required=False, label='File')  # For Video and Document
    image_file = forms.ImageField(required=False, label='Image File')  # For Image


