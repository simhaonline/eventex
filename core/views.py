from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request, template=None):
    return render_to_response(template, context_instance=RequestContext(request))
