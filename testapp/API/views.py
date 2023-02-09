from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.API.serializers import URLSerializer
from testapp.models import URL
from random import *
class Generate_Short_URL(APIView):
    def post(self,request):
        data = request.data
        serializer = URLSerializer(data=data)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        output = choice(alphabets) + choice(digits) + choice(alphabets) + choice(digits) + choice(alphabets) + choice(
            digits)
        if serializer.is_valid():
           url = serializer.data.get('url')
           new_object = URL(url=url , hidden_url=output)
           new_object.save()
           return Response({'shorten url:':'http://127.0.0.1:8000/'+output})

        else:
            return Response({'shorten url:':'Seomthing went wrong'})
