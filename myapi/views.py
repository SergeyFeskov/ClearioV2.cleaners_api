from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CleanersInfoSerializer
from .models import CleanersInfo

class CleanersList(APIView):
    """
    List all cleaners, or create a new cleaner.
    """
    def get(self, request, format=None):
        cleaners = CleanersInfo.objects.all()
        serializer = CleanersInfoSerializer(cleaners, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CleanersInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.set_id()
            serializer.save()
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CleanerDetail(APIView):
    """
    Retrieve, update or delete a cleaner.
    """
    def get_object(self, pk):
        try:
            return CleanersInfo.objects.get(pk=pk)
        except CleanersInfo.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        cleaner = self.get_object(pk)
        serializer = CleanersInfoSerializer(cleaner)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cleaner = self.get_object(pk)
        serializer = CleanersInfoSerializer(cleaner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cleaner = self.get_object(pk)
        cleaner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CleanersInfoViewSet(viewsets.ModelViewSet):
#     queryset = CleanersInfo.objects.all().order_by('id')
#     serializer_class = CleanersInfoSerializer

# class CleanerInfoCreateViewSet(APIView):
#     def post(self, request):
#         cleaner_info = CleanerInfoCreateSerializer(data=request.data)
#         if cleaner_info.is_valid():
#             # cleaner_info.set_id()
#             cleaner_info.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(cleaner_info.errors, status=status.HTTP_400_BAD_REQUEST)
