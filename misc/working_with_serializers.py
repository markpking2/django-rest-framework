# Django shell example of working with serializers

import io
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

# translate model instance to Python native datatypes
serializer = SnippetSerializer(snippet)
print(serializer.data)

# render data into JSON
content = JSONRenderer().render(serializer.data)
content

# deserialization, parse stream into Python datatypes
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
# restore datatypes into fully populated object instance
serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
print(serializer.validated_data)
serializer.save()

# We can also serialize querysets instead of model instances. To do so we simply add a many=True flag to the serializer arguments
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
print(serializer.data)
