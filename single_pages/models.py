from django.db import models

# Create your models here.
# 09-24

class Post(models.Model):
    # # DB col을 생성하는데, model -> title
    # title = models.CharField(max_length=30)
    #
    # # DB col을 생성하는데, model -> content
    # content = models.TextField()
    #
    # # DB col을 생성하는데, model -> 시간
    # # 현재시간을 새로 작성할때 바로 넣기
    # create_at = models.DateTimeField(auto_now_add=True)
    #
    # # 수정시간을 업데이트 했을때, 수정 현재시각으로 교체
    # update_at = models.DateTimeField(auto_now=True)
    #
    # #이미지 필드 추가
    # head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'