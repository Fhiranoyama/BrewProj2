from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from .models import Brewiten
import requests

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class Brewshopping(View):
    def get(self, request):
        nome = request.GET.get('nome', '')
        site = f'https://api.openbrewerydb.org/v1/breweries?by_name={nome}'
        print(nome)
        req = requests.get(site)
        list_of_jsons = req.json()        
        response = HttpResponse()
        response.write("<table border= '2'>")
        response.write("<tr><th>brewery_name</th><th>city</th><th>type_brews</th></tr>")
        for Brew in list_of_jsons:
            #print (Brew)
            response.write(f"<tr><td>{Brew['name']}</td><td>{Brew['city']}</td><td>{Brew['brewery_type']}</td></tr>")
        response.write("</table>")
        return response
    
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        brew_name = data.get('brew_name')
        Price = data.get('Price')
        type_brews = data.get('type_brews')

        produco_data = {
            'brew_name': brew_name,
            'Price': Price,
            'type_brews': type_brews,
        }

        Brewiten = Brewiten.objects.create(**produco_data)

        data = {
            "message": f"Brew_name: {Brewiten.id}"
        }
        return JsonResponse(data, status=201)
    
@method_decorator(csrf_exempt, name='dispatch')
class updel(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = Brewiten.objects.get(id=item_id)
        item.type_brews= data['type']
        item.save()

        data = {
            'message': f'Item {item_id} has been updated'
        }

        return JsonResponse(data)


    def delete(self, request, item_id):
        item = Brewiten.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Item {item_id} Brew has been removed!'
        }

        return JsonResponse(data)
    