from django.utils.deprecation import MiddlewareMixin
from .models import Turn




class GetTurn(MiddlewareMixin):
    def process_request(self, request):

        turn_list= Turn.objects.order_by('id')
       
        request.turn_list = turn_list
        
        print(request.turn_list)
        return None