from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from .serializers import CleanersInfoSerializer
from .models import CleanersInfo


class ByOneCleanerPagination(LimitOffsetPagination):
    default_limit = 1

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.count,
            'results': data
        })

class CleanersInfoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = CleanersInfo.objects.all()
    serializer_class = CleanersInfoSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('id', 'city', 'isworking')

    def create(self, request, format=None, *args, **kwargs):
        serializer = CleanersInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = CleanersInfo.objects.all()

        city = self.request.query_params.get('city')
        if city is not None:
            queryset = queryset.filter(city=city) | queryset.filter(city='')

        get_group = self.request.query_params.get('get_group')
        if get_group is not None:
            get_group = int(get_group)
            queryset = queryset.order_by('-rating')[:get_group]

        return queryset

class ByOneCleanerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CleanersInfo.objects.all().order_by('-rating')
    serializer_class = CleanersInfoSerializer
    pagination_class = ByOneCleanerPagination

    def get_queryset(self):
        queryset = CleanersInfo.objects.all().order_by('-rating')

        city = self.request.query_params.get('city')
        if city is not None:
            queryset = queryset.filter(city=city) | queryset.filter(city='')

        return queryset


# class CleanersList(APIView):
#     """
#     List all cleaners, or create a new cleaner.
#     """
#     def get(self, request, format=None):
#         cleaners = CleanersInfo.objects.all()
#         serializer = CleanersInfoSerializer(cleaners, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CleanersInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.set_id()
#             serializer.save()
#             return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class CleanerDetail(APIView):
#     """
#     Retrieve, update or delete a cleaner.
#     """
#     def get_object(self, pk):
#         try:
#             return CleanersInfo.objects.get(pk=pk)
#         except CleanersInfo.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         cleaner = self.get_object(pk)
#         serializer = CleanersInfoSerializer(cleaner)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         cleaner = self.get_object(pk)
#         serializer = CleanersInfoSerializer(cleaner, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         cleaner = self.get_object(pk)
#         cleaner.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

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
