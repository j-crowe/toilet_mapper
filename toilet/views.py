# Create your views here.
from models import Toilet
from review.models import Review
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template

def single_toilet_view(req, pk):
    t = Toilet.objects.get(pk=pk)
    if req.user.is_authenticated() == False:
        reviewed = False
    else:
        reviewed = True if len(Review.objects.filter(toilet=t).filter(user=req.user)) > 0 else False
    c = Context({ "t": t, 'has_reviewed' : reviewed, 'is_mod' : req.user.groups.filter(name='Mod') })
    return render(req, "single_toilet_view.html", c)


