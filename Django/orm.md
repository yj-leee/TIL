
# 01. Annotate

작성한 코드 
```python

            properties = Property.objects.\
                prefetch_related('propertyimage_set',
                                 'bookmark_set',
                                 'review_set',
                                 'type').\
                annotate(review_count=Count('review')).\
                filter(query, **conditions).order_by(sort_set[sort])
```

annotate는property의 'review' 라는 필드를 생성하고 review 개수를 count한 값을 넣어준다.


# 02. Aggregate
Django에서 쿼리셋의 특정 필드를 모두 더할 때 사용한다.
한 컬럼의 전체의 합이나 평균, 개수를 계산한다고 보면 된다.
aggretate 로 생성한 값이 딕셔너리 형태로 출력되기 때문에 아래처럼 작성되었다.

작성한 코드
```python
def validate_review_set(property):

    if property.review_set.exists():
        rate = {}
        rate['propertyCleanliness']   = property.review_set.aggregate(cleanliness=Avg('cleanliness'))['cleanliness']
        rate['propertyCommunication'] = property.review_set.aggregate(communication=Avg('communication'))['communication']
        rate['propertyCheckIn']       = property.review_set.aggregate(check_in=Avg('check_in'))['check_in']
        rate['propertyAccuracy']      = property.review_set.aggregate(accuracy=Avg('accuracy'))['accuracy']
        rate['propertyLocation']      = property.review_set.aggregate(location=Avg('location'))['location']
        rate['propertyAffordability'] = property.review_set.aggregate(affordability=Avg('affordability'))['affordability']


        rate['propertyRate'] = (rate['propertyCleanliness'] +\
                               rate['propertyCommunication'] +\
                               rate['propertyCheckIn'] +\
                               rate['propertyAccuracy'] +\
                               rate['propertyLocation'] +\
                               rate['propertyAffordability'])/6
        return rate
    return False
```
