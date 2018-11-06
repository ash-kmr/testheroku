from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def test(request):
	r = requests.post('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=', request.POST)
	print(r.json())
	return JsonResponse({'foo':'bar'})

