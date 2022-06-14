class TestFullListApi:
    def test_root_status(self, test_client):
        response = test_client.get('/api/posts')
        assert response.status_code == 200, "Статус код ответа api full_list_api_page не 200"

    def test_type_of_root_content(self, test_client):
        response = test_client.get('/api/posts')
        assert type(response.json) == list, "Тип данных ответа api full_list_api_page не list"

    def test_keys_of_root_content(self, test_client, test_keys_should_be):
        response = test_client.get('/api/posts')
        assert set(response.json[0].keys()) == test_keys_should_be, "Ключи ответа api full_list_api_page не совпадают"


class TestCurrentPostApi:
    def test_root_status(self, test_client):
        response = test_client.get('/api/posts/1')
        assert response.status_code == 200, "Статус код ответа api current_post_api_page не 200"

    def test_type_of_root_content(self, test_client):
        response = test_client.get('/api/posts/1')
        assert type(response.json) == dict, "Тип данных ответа api current_post_api_page не dict"

    def test_keys_of_root_content(self, test_client, test_keys_should_be):
        response = test_client.get('/api/posts/1')
        assert set(response.json.keys()) == test_keys_should_be, "Ключи ответа api current_post_api_page не совпадают"

    def test_values_of_root_content(self, test_client):
        response = test_client.get('/api/posts/1')
        assert response.json['pk'] == 1, "Значение ответа  по ключу pk в api current_post_api_page не совпадает"
