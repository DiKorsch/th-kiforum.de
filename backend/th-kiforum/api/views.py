from django.http import JsonResponse
from rest_framework import viewsets
from markdown_it import MarkdownIt

from api.models import Demonstrator
from api.models import Content
from api.serializers import DemonstratorSerializer



class DemonstratorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Demonstrator.objects.all()
    serializer_class = DemonstratorSerializer


def get_content(request, content_name):
    try:
        content = Content.objects.get(name=content_name)
        md = MarkdownIt('commonmark', {'breaks':True,'html':True})
        html = md.render(content.content)
        return JsonResponse({'name': content.name, 'content': content.content, "html": html})
    except Content.DoesNotExist:
        return JsonResponse({'error': 'Content not found'}, status=404)
