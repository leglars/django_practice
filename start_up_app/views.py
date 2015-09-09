from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
from start_up_app.models import Book
from django.core.mail import send_mail


def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('timeview/current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render_to_response("timeview/hours_ahead.html", locals())

def display_meta(request):
    values = request.META.items()
    path = request.path
    # print(type(values))
    return render_to_response("display_meta.html", locals())

# def search_form(request):
#     return render_to_response("search_form.html")

def search(request):
    errors = []
    if "query" in request.GET:
        query = request.GET["query"]
        if not query:
            errors.append("Enter a search term.")
        elif len(query):
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__icontains = query)
    return render_to_response("search.html", locals())


def contact(request):
    errors = []
    if request.method == "post":
        if not request.POST.get("subject", ""):
            errors.append("Enter a subject.")
        if not request.POST.get("message", ""):
            errors.append("Enter a message.")
        if request.POST.get("email") and "@" not in request.POST["email"]:
            errors.append("Enter a valid e-mail address.")
        if not errors:
            send_mail(
                request.POST["subject"],
                request.POST["message"],
                request.POST.get("email", "noreply@example.com"),
                ["siteowner@example.com"],
            )
            return HttpResponseRedirect("/contact/thanks/")
    return render_to_response("contact_form.html", locals())