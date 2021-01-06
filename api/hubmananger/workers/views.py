from rest_framework import viewsets , generics
from users.models import Worker
from .serializers import WorkerSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsHubMananger



class WorkerViewSet(generics.ListCreateAPIView , IsHubMananger ):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = ( IsAuthenticated , IsHubMananger )

class WorkerDetailViewSet(generics.RetrieveUpdateDestroyAPIView , IsHubMananger):

    serializer_class = WorkerSerializer
    permission_classes = (IsAuthenticated, IsHubMananger )
    lookup_field = "id"

    def get_queryset(self):
        return Worker.objects.all()
    
