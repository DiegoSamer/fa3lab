import fastlab
from fastapi.testclient import TestClient

client = TestClient(fastlab)
def test1():
 assert fastlab.sum_two_args(2,2) == 4


def test_make_image_no_files():
 # Создайте данные для формы
 data = {"angle": 45, "resp": "recaptcha_response"}

 # Отправьте запрос
 response = client.post("/image_form", data=data)

 # Проверьте ответ
 assert response.status_code == 400