from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Men
from .permissions import IsAdminOrReadOnly
from .serializers import MenSerializer


class MenAPIList(generics.ListCreateAPIView):  # get & post requests
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MenAPIUpdate(generics.RetrieveUpdateDestroyAPIView):  # put request
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated,)



class MenAPIDestroy(generics.RetrieveUpdateDestroyAPIView):  # delete request
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly,)
