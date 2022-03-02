from pickletools import read_uint1
from unicodedata import category, name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.urls import reverse


# Create your models here.
# 글 카테고리 정의

class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그의 카테고리 분류를 입력하세요.(ex:일상)")
    
    def __str__(self):
        return self.name   #클래스 자신을 무엇으로 화면에 표시할지 여기서는 제목=name으로 보여줌


#블로그 글(제목, 작성일, 이미지, 글의 내용, 카테고리분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True) #이미지 빈값일 수 있으니 트루설정#settings에 media추가필요#urls에서 static 추가필요
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True) #자동으로 지금 시간 적용
    updateDate = models.DateTimeField(auto_now_add=True)
    #다양한 카테고리 선택(ex: 정보, 유머) 다 대 다 관계
    category = models.ManyToManyField(Category, help_text="글의 분류를 선택하세요")
    
    def __str__(self):
        return self.title
    
    #글의 번호가 1번 -> post/1/ 가 주소가 됨.
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
    
    def is_content_more300(self):
        return len(self.content) > 300
    
    def get_content_under300(self):
        return self.content[:300]