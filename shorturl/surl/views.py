from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from .models import Link
#import pdb
#@jake:4/13/2016 The view in homepage
class LinkCreate(CreateView):
    model = Link
    fields = ["url"]

    def form_valid(self, form):
        prev = Link.objects.filter(url=form.instance.url)
        if prev:
        	return redirect("link_show", pk=prev[0].pk)
        return super(LinkCreate, self).form_valid(form)
 #@jake:4/13/2016 Detailed view after submission of url   
class LinkShow(DetailView):
	model = Link
#@jake:4/13/2016 Redirect to long url
class RedirectToLongURL(RedirectView):
	permanent=False
	def get_redirect_url(self, *args, **kwargs):
		short_url = kwargs["short_url"]
		return Link.expand(short_url)