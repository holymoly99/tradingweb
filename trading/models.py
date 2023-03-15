from django.db import models

class Write(models.Model):
    subject = models.CharField(max_length=200) # 글 제목
    images = models.ImageField(blank=True, upload_to='images')
    category = models.TextField(default="") # 카테고리
    price = models.IntegerField(default=0) # 가격
    tmethod = models.TextField(default="") # 거래 방식
    content = models.TextField() # 글 내용
    create_date = models.DateTimeField() # 글 작성일

    def __str__(self):
        return self.subject


class Answer(models.Model):
    write = models.ForeignKey(Write, on_delete=models.CASCADE) # 댓글 작성할 글
    content = models.TextField() # 댓글 내용
    create_date = models.DateTimeField() # 댓글 작성