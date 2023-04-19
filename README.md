
# Environment
- Python: Python 3.10.4
  - pyenv
- Package Manager: poetry
- 
python version: 3.10.4

## pyenv setup
TBD

## poetry setup
TBD

## Setup Local Server
* cd prd & python manage.py makemigrations & python manage.py migrate
* cd prd & python manage.py runserver

# Misc
Update PublicCardInfo
from django.contrib.auth.models import User
from card.szs import PublicCardInfoSerializer
from card.models import PublicCardInfo
user = User.objects.get(id=1)
card = PublicCardInfoSerializer(data={ "url": "http://example.co", "name": "chatgpt", "creator": 1, "link": [{ "url": "http://linkin.com/user"}]})

Put by CURL
curl -u cjcool:mathdep1281 -X PUT http://127.0.0.1:8000/card/public_card_update/3 -d 'url=http://example10.co&id=3&name=wtf&creator=2'
curl -u cjcool:mathdep1281 -H "Content-Type: application/json" -X PUT http://127.0.0.1:8000/card/public_card_update/3 -d '{"url": "http://example10.co", "name": "wtf", "creator":2}'
curl -u cjcool:mathdep1281 -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/card/public_card_create -d '{"url": "http://example10.co", "name": "wtf", "creator":2}'

"""
using HTTP POST method will not trigger an update in a Django ModelViewSet.

HTTP POST is used to create a new resource at the server. In the context of a Django ModelViewSet, a POST request is typically used to create a new instance of the model.

To update an existing instance of the model using a Django ModelViewSet, you would typically use the HTTP PUT or PATCH method.

HTTP PUT is used to replace the entire resource with a new one, while HTTP PATCH is used to update the resource with a partial set of new data.

When a PUT or PATCH request is sent to the viewset, it will trigger the update method of the viewset. In the update method, the existing instance of the model can be updated with the new data provided in the request.

So, to summarize, if you want to update an existing instance of the model using a Django ModelViewSet, you should use HTTP PUT or PATCH methods, and not the HTTP POST method.
"""