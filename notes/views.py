from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
