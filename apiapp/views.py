from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import user
from .serializers import ItemSerializer

# Create your views here.






def attackareal(request):

    return render(request, "attack_template.html")


class UserView(APIView):

    def get(self, request):
        items = user.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
  

class RemoveUser(APIView):

    def get(self, request, id):
        items = user.objects.get(id=id)
        if items:
            items.delete()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)




class FetchUser(APIView):

    def get(self, request, id):
        userinfor = user.objects.get(id=id)

        serializedata = ItemSerializer(userinfor)

        return Response(serializedata.data, status= status.HTTP_200_OK)




