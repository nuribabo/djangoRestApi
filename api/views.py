
from django.http.response import HttpResponse
from .models import Post
import json
from django.core import serializers as sl

# Create your views here.

def test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        try:
            Post(text = data.get('text','')).save()
            # text = Test.objects.get_
            return HttpResponse(json.dumps({'code':'true'})) 
        except:
            return HttpResponse(json.dumps({'code':'fail'}))
    else:
        qs = Post.objects.all()
        qs_json = sl.serialize('json', qs)

        return HttpResponse(qs_json, content_type='application/json')