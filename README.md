# Klasifikasi for Python

Official [Klasifikasi](https://klasifikasi.com/) API Client Library

## Requirement

Python 3.7 or later

## Installation

`pip install klasifikasi-py`

## Quick start

You will need valid `clientId` & `clientSecret` of your model. You can get those
from credential section at your model page, which is both unique per model

```python
from klasifikasi import Klasifikasi

klasifikasi_instance = Klasifikasi(creds=[
  {
    'client_id': 'client_id',
    'client_secret': 'client_secret'
  }
])
```

You can pass multiple `clientId` & `clientSecret` too

```python
from klasifikasi import Klasifikasi

klasifikasi_instance = Klasifikasi(creds=[
  {
    'client_id': 'client_id_1',
    'client_secret': 'client_secret_1'
  },
  {
    'client_id': 'client_id_2',
    'client_secret': 'client_secret_2'
  }
])
```

## Classify

You need your model `publicId` to start classifying. You can get those from your
model page, or you get get it from here :

```python
models = klasifikasi_instance.get_models()
for publicId in models:
  print(publicId)
```

Classifying example :

```python
result = klasifikasi_instance.classify('publicId', 'query')
```

## Logs

You can get your classifying logs based on your model `publicId`

```python
logs = klasifikasi_instance.classify('publicId', {
  'started_at': '1 December 2020',
  'ended_at': '2 December 2020',
  'skip': 0
  'take': 10
})
```

`ended_at` & `started_at` parameter is mandatory, the rest is optional

## Error

All the function above will throw an Exception if something bad happen. Always
run each function inside `try` & `except` block
