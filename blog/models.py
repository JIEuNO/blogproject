from django.db import models

# Create your models here.
# 모르는 거는 "django model" 이라고 검색해보자
class Blog(models.Model): # Blog 라는 이름의 객체 틀을 만들겠다 !
    title=models.CharField(max_length=200) # title 이름으로 최대 200글자의 데어터를 받겠다 !
    pub_date=models.DateTimeField('date published') # pub_date 라는 이름으로 시간 날짜 데이터를 받겠다 !
    body=models.TextField()

    def __str__(self):
        return self.title