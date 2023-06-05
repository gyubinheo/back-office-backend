## OKPOS 백오피스 - 백엔드 코딩테스트

### 프로젝트 소개
[Django REST framework](https://www.django-rest-framework.org/) 를 사용하여 상품(Product)을 추가 / 조회 / 수정 / 삭제하는 API 를 만듭니다.<br>
중첩구조의 데이터를 한 번의 API호출로 처리하는 것이 가장 중요하며, 이 때 [drf-writable-nested](https://github.com/beda-software/drf-writable-nested) 라이브러리를 사용하도록 합니다.

### Stacks
| Python | Django |  Django REST framework   |
| :----: | :----: | :----------------------: |
|  3.8   | 2.2.24 |          3.12            |

### API Docs
https://documenter.getpostman.com/view/18286715/2s93sW9bf3

### Installation
```
git clone https://github.com/gyubinheo/back-office-backend
cd back-office-backend
```

### Local
```python
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# localhost:8000/admin
# localhost:8000/doc
# localhost:8000/shop
```

### Docker
```python
docker-compose up --build

# localhost/admin
# localhost/doc
# localhost/shop
```

### Test
```python
# Local에서 실행 가능
pytest
```
