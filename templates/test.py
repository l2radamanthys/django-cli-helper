from rest_framework.test import APITestCase

from %app%.models.%nombre_plural% import %modelo%


class API%modelo%TestCase(ApiTestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/%modelo_url%')
        self.assertEqual(len(response.data['result']), 0)
