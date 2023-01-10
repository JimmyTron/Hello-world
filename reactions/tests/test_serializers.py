from django.test import TestCase
from reactions.models import Stori
from reactions.serializers import StoriSerializer

# Create your tests here.
class StoriSerializerTestCase(TestCase):
    def test_stori_serializer(self):
        stori_serializer = StoriSerializer(
            data={"title": "Stories Of Time", 
                "stori": "The mighty sinbad story", 
                "description": "A fiction tale", 
                "created_by": 1, 
                "category": "Fiction",
                "status": 0,}
            )
        self.assertEqual(str(stori_serializer.is_valid()),"True")