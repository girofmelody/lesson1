import pytest
import requests

base_url = "https://ru.yougile.com/api-v2/projects/"

api_key = "iZ9lYsQiCQYV2rgesRquxBoEP-+HAuRPgDW3WMfEy6u+QhB7XTmHWkZc85BJSWLR"

headers = {
  "Authorization": f"Bearer {api_key}",
 "Content-Type": "application/json",
}

@pytest.fixture
def create_test_project():
  payload = {
    "title": "Test Project"
  }
  response = requests.post(f"{base_url}", json=payload, headers=headers)
  response.raise_for_status()
  project_id = response.json().get("id")
  yield project_id

def test_create_project_positive():
  payload = {
    "title": "New Project"
  }

  response = requests.post(f"{base_url}", json=payload, headers=headers)
  print("Статус:", response.status_code)
  print("Ответ:", response.text)
  assert response.status_code == 201, \
    f"Ожидался статус 201, получен {response.status_code}"

  data = response.json()
  assert "id" in data, "Ответ не содержит id"

def test_update_project_positive(create_test_project):
  project_id = create_test_project
  new_title = "Updated Project Title"

  update_response = requests.put(
    f"{base_url}{project_id}",
    json={"title": new_title},
    headers=headers
  )

  print("Update статус:", update_response.status_code)
  print("Update ответ:", update_response.text)

  assert update_response.status_code == 200, \
    f"Обновление не удалось, статус {update_response.status_code}"

  get_response = requests.get(f"{base_url}{project_id}", headers=headers)
  print("Get после обновления статус:", get_response.status_code)
  print("Get после обновления ответ:", get_response.text)

  assert get_response.status_code == 200
  data = get_response.json()

  assert data["id"] == project_id
  assert data["title"] == new_title

def test_get_project_positive(create_test_project):
  project_id = create_test_project

  response = requests.get(f"{base_url}{project_id}", headers=headers)

  print("Get статус:", response.status_code)
  print("Get ответ:", response.text)

  assert response.status_code == 200, \
    f"Не удалось получить проект, статус {response.status_code}"

  data = response.json()
  assert data["id"] == project_id
  assert "title" in data

def test_get_nonexistent_project():
  fake_id = "nonexistent-id-12345"

  response = requests.get(f"{base_url}{fake_id}", headers=headers)

  print("Get несуществующего проекта статус:", response.status_code)

  assert response.status_code == 404

def test_update_nonexistent_project():

  fake_id = "nonexistent-id-12345"

  response = requests.put(
    f"{base_url}{fake_id}",
    json={"title": "Should Fail"},
    headers=headers
  )

  assert response.status_code == 404

def test_create_project_with_invalid_type():
  invalid_payload = "This is not a valid JSON object"

  response = requests.post(f"{base_url}", data=invalid_payload, headers={"Content-Type": "application/json"})

  print("Ответ при передаче некорректного типа данных:", response.status_code)
  print("Ответ текста:", response.text)

  assert response.status_code in [400, 415], \
    f"Ожидался статус 400 или 415, получен {response.status_code}"