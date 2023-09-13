from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Boarder, Roomt, Maintenance, Bills

# Create your views here.

def emro_boarding_house (request):

    myboarders = Boarder.objects.all().values()
    template = loader.get_template('all_boarder.html')
    context = {
        'myboarders' : myboarders,
    }

    return HttpResponse(template.render(context,request))

def details (request, id):

    myboarders = Boarder.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myboarders' : myboarders,
    }

    return HttpResponse(template.render(context,request))

def main (request):

    template = loader.get_template('main.html')
    return HttpResponse(template.render())



def roomt (request):

    myroomt = Roomt.objects.all().values()
    template = loader.get_template('roomt.html')
    context = {
        'myroomt' : myroomt,
    }
    return HttpResponse(template.render(context,request))

def maintenance (request,id):

    roomid= get_object_or_404(Roomt, id=id)

    mymain = Maintenance.objects.filter(room_id=roomid)
    template = loader.get_template('maintenance.html')
    context = {

        'roomid':roomid,
        'mymain' : mymain,
        
    }
    return render(request, 'maintenance.html', context)
    ##return HttpResponse(template.render(context,request))


def bills (request,id=None):
  if id is not None:
    idboarder= get_object_or_404(Boarder, id=id)
    mybill = Bills.objects.filter(boarder_id=idboarder)
  else:
    mybill = Bills.objects.all()
  template = 'bills.html'
  context = {
        'idboarder':idboarder if id is not None else None,
        'mybill' : mybill,
  }
  return render(request, template, context)

    ##return HttpResponse(template.render(context,request))


def bills_details (request,id):

    idboarder= get_object_or_404(Boarder, id=id)

    mybills = Bills.objects.filter(boarder_id=idboarder)
    template = loader.get_template('bills_details.html')
    context = {

        'idboarder':idboarder,
        'mybills' : mybills,
        
    }
    return render(request, 'bills_details.html', context)
