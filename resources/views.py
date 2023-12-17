from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Resource, Note, Ebook, Link, Video, Image, Document, ResourceType
from .forms import ResourceForm, UpdateResourceForm, DeleteResourceForm
from django.http import FileResponse
from django.views import View
from .forms import NoteForm, EbookForm, LinkForm, VideoForm, ImageForm, DocumentForm

class ResourceListView(ListView):
    model = Resource
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'
    ordering = ['-upload_date']

class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'resources/resource_detail.html'
    context_object_name = 'resource'

# Note views
class NoteListView(ListView):
    model = Note
    template_name = 'resources/note_list.html'
    context_object_name = 'notes'
    ordering = ['-upload_date']
    

class NoteDetailView(DetailView):
    model = Note
    template_name = 'resources/note_detail.html'
    context_object_name = 'note'

# Ebook views
class EbookListView(ListView):
    model = Ebook
    template_name = 'resources/ebook_list.html'
    context_object_name = 'ebooks'
    ordering = ['-upload_date']

class EbookDetailView(DetailView):
    model = Ebook
    template_name = 'resources/ebook_detail.html'
    context_object_name = 'ebook'

# Link views
class LinkListView(ListView):
    model = Link
    template_name = 'resources/link_list.html'
    context_object_name = 'links'
    ordering = ['-upload_date']

class LinkDetailView(DetailView):
    model = Link
    template_name = 'resources/link_detail.html'
    context_object_name = 'link'

# Video views
class VideoListView(ListView):
    model = Video
    template_name = 'resources/video_list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']

class VideoDetailView(DetailView):
    model = Video
    template_name = 'resources/video_detail.html'
    context_object_name = 'video'

# Image views
class ImageListView(ListView):
    model = Image
    template_name = 'resources/image_list.html'
    context_object_name = 'images'
    ordering = ['-upload_date']
    

class ImageDetailView(DetailView):
    model = Image
    template_name = 'resources/image_detail.html'
    context_object_name = 'image'

# Document views
class DocumentListView(ListView):
    model = Document
    template_name = 'resources/document_list.html'
    context_object_name = 'documents'
    ordering = ['-upload_date']

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'resources/document_detail.html'
    context_object_name = 'document'


def home_view(request):
    context = {
        'welcome_message': 'Welcome to the College Resources Platform!',
    }
    return render(request, 'base.html', context)

def resource_type_list(request):
    resource_types = ResourceType.objects.all()
    return render(request, 'resource_type_list.html', {'resource_types': resource_types})

def resource_type_detail(request, resource_type_id):
    resource_type = get_object_or_404(ResourceType, pk=resource_type_id)
    resources_of_type = Resource.objects.filter(resource_type=resource_type)
    return render(request, 'resource_type_detail.html', {'resource_type': resource_type, 'resources_of_type': resources_of_type})


def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()

    return render(request, 'create_resource.html', {'form': form})



def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})


def update_resource(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == 'POST':
        form = UpdateResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = UpdateResourceForm(instance=resource)

    return render(request, 'update_resource.html', {'form': form, 'resource': resource})


def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == 'POST':
        form = DeleteResourceForm(request.POST, instance=resource)
        if form.is_valid():
            resource.delete()
            return redirect('resource_list')
    else:
        form = DeleteResourceForm(instance=resource)

    return render(request, 'delete_resource.html', {'form': form, 'resource': resource})

#Upload Resource
def upload_resource(request, resource_type_id):
    resource_type = ResourceType.objects.get(id=resource_type_id)

    if request.method == 'POST':
        form = get_resource_form(request.POST, request.FILES, resource_type)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploader = request.user
            resource.resource_type = resource_type
            resource.save()
            return redirect('resource_list')  # Replace with your actual URL
    else:
        form = get_resource_form(resource_type=resource_type)

    return render(request, 'upload_resource.html', {'form': form, 'resource_type': resource_type})

def get_resource_form(data=None, files=None, resource_type=None):
    if resource_type:
        if resource_type.name == 'Note':
            return NoteForm(data, files)
        elif resource_type.name == 'Ebook':
            return EbookForm(data, files)
        elif resource_type.name == 'Link':
            return LinkForm(data, files)
        elif resource_type.name == 'Video':
            return VideoForm(data, files)
        elif resource_type.name == 'Image':
            return ImageForm(data, files)
        elif resource_type.name == 'Document':
            return DocumentForm(data, files)
    return ResourceForm(data, files)



# resources/views.py


def upload_page(request):
    resource_types = ResourceType.objects.all()
    return render(request, 'resources/upload_page.html', {'resource_types': resource_types})




def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resource_list')  # or wherever you want to redirect after a successful upload
    else:
        form = ImageForm()
    
    return render(request, 'resources/upload_page.html', {'form': form})




# resources/views.py
from .forms import UploadForm

def upload_page(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            resource_type = form.cleaned_data['resource_type']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            if resource_type == 'note':
                content = form.cleaned_data['content']
                note = Note.objects.create(title=title, description=description, content=content, uploader=request.user)
                note.save()
            elif resource_type == 'ebook':
                author = form.cleaned_data['author']
                publication_year = form.cleaned_data['publication_year']
                file = form.cleaned_data['file']
                ebook = Ebook.objects.create(title=title, description=description, author=author,
                                             publication_year=publication_year, file=file, uploader=request.user)
                ebook.save()
            elif resource_type == 'link':
                url = form.cleaned_data['url']
                link = Link.objects.create(title=title, description=description, url=url, uploader=request.user)
                link.save()
            elif resource_type == 'video':
                file = form.cleaned_data['file']
                video = Video.objects.create(title=title, description=description, file=file, uploader=request.user)
                video.save()
            elif resource_type == 'image':
                image_file = form.cleaned_data['image_file']
                image = Image.objects.create(title=title, description=description, image_file=image_file, uploader=request.user)
                image.save()
            elif resource_type == 'document':
                file = form.cleaned_data['file']
                document = Document.objects.create(title=title, description=description, file=file, uploader=request.user)
                document.save()

            return redirect('resource_list')  # or wherever you want to redirect after a successful upload
    else:
        form = UploadForm()

    return render(request, 'resources/upload_page.html', {'form': form})


# ###############################################

# resources/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

class SignUpView(View):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to home or another page upon successful signup
        return render(request, self.template_name, {'form': form})



# resources/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

class SignInView(View):
    template_name = 'registration/signin.html'
    authenticated_template_name = 'registration/already_authenticated.html'  # New template for authenticated users
    form_class = AuthenticationForm

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.authenticated_template_name)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return render(request, self.authenticated_template_name)
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')  # Redirect to home or another page upon successful login
        return render(request, self.template_name, {'form': form})




# resources/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View
from django.contrib import messages

class SignOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('home')  # Redirect to home or another page upon successful logout



# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def UserDashboardView(request):
    user = request.user
    context = {
        'full_name': user.full_name,
        'date_of_birth': user.date_of_birth,
        'college': user.college,
        'age': user.age,
        'mobile_number': user.mobile_number,
        'email': user.email,
    }
    return render(request, 'user_dashboard.html', context)


