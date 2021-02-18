

## Drf

Django 안에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리


## Serializer

파이썬 형식의 코드를 다른 네트워크 환경과 통신을 위해
코드를 직렬화 해야할 때, DRF에서 그것을 담당하는 Serializer 클래스이다.

DRF에서 제공하는 Serializer는 queryset, model instance 등의 복잡한 데이터를 
JSON, XML 등의 컨텐트 타입으로 쉽게 변환 가능한 python datatype으로 변환한다.


01 - Serialization은 ORM과 non-ORM 데이터 소스를 모두 지원한다.
02 - serializers는 모델을 전달하고, 그 모델들을 json 객체로 변환한다.
03 - 클라이언트로부터 백엔드에게 데이터를 전달하기도 한다.
04 - 코드를 검증하는 것도 자동으로 할 수 있다.
05 - 코드를 정리해서 security issues를 해결하기도 한다.


참고link: https://bmh8993.github.io/python/django/drf-01/


