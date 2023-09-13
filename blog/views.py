from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Contact
from .forms import ContactForm


# from .forms import CommentForm
# from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def ContactView(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Create and save the Contact object
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        return redirect(PostList)
