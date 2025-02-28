
from . serializers import TodoSerializer, UserSerializer, RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from . models import *

class TodoView(APIView):
    #read
    def get (self, request):
        try:
            todo= Todo.objects.all()
            serializers= TodoSerializer(todo, many= True)
            return Response(serializers.data, status= status.HTTP_200_OK)

        except Exception as e:
            return Response({'error', str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      #create  
    def post (self, request):
        try:
            serializers= TodoSerializer(data= request.data)
            if serializers.is_valid():
                serializers.save
                return Response(serializers.data, status= status.HTTP_201_CREATED)
            return Response({'Message':'Error in data'}, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error',str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #update
    def put (self, request, *args, **kwargs):
        todo_id= kwargs.get ('id')
        try:
            todo= Todo.objects.get(id=todo_id)
            serializer= TodoSerializer (instance= todo, data= request.data, partial= True)
            if serializer.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response({'message': 'error in data'}, status= status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response ({'error', str(e)}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        #delete
        def delete(self, request, *args, **kwargs):
            todo_id= kwargs.get('id')
            try:
                todo= Todo.objects.get(id=todo_id)
                todo.delete()
                return Response({'success':'item deleted'}, status=status.HTTP_204_NO_CONTENT)

            except Exception as e:
                return Response({'error', str(e)}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

                    
        
