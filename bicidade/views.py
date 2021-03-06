from django.http import HttpResponse,HttpResponseRedirect
from bicidade.models import * 
import json
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render_to_response

@csrf_exempt
def reverse_geocode(request):
  x=request.GET.get('x')
  y=request.GET.get('y')
  id=None
  for t in Way.objects.raw("SELECT bicidade.reverse_geocode(%s,%s) as id",[x,y]):
    id=t.id
    
  
  return HttpResponse(str(id))
@csrf_exempt
def route(request):
  x0=request.GET.get('x0')
  y0=request.GET.get('y0')
  x1=request.GET.get('x1')
  y1=request.GET.get('y1')
  alt=request.GET.get('alt')
  crit=request.GET.get('crit')
  cursor = connection.cursor()
  
  #print "altimetria"+str(alt)
  if alt==None:
    alt=0
  cursor.execute("SELECT bicidade.route(%s,%s,%s,%s,%s,%s)",[x0,y0,x1,y1,crit,alt])
  results = cursor.fetchall()
  response = HttpResponse(results[0])
  response["Access-Control-Allow-Origin"] = "*"  
  response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"  
  response["Access-Control-Max-Age"] = "1000"  
  response["Access-Control-Allow-Headers"] = "*" 
  
  return response
  
def home(request):
  return HttpResponseRedirect('/map')

