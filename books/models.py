from django.db import models
from django.conf import settings
# Create your models here.

class BookInfo(models.Model):
    # 도서정보
    image = models.ImageField(upload_to='book_img/',blank=True, null=True)
    book_name = models.CharField("도서명", max_length=200)
    publisher = models.CharField("출판사", max_length=100)
    author = models.CharField("저자", max_length=100)
    publication_date = models.CharField("출판일", max_length=10, blank=True)
    pages=models.CharField("페이지 수",max_length=10000)
    isbn = models.CharField("ISBN", max_length=25, unique=True)
    description=models.CharField("소개",max_length=10000)
    link = models.URLField("원본링크", blank=True)

    #추가 정보
    hold = models.IntegerField("보유권수", blank=True)
    rent_info = models.OneToOneField('RentInfo',on_delete=models.CASCADE,blank= True,null=True,related_name='bookInfo')

    class Meta:
        db_table='book_info'
        ordering = ['-pk']

    def __str__(self):
        return self.book_name

    def rent_book(self,user):
            rent_info=self.rentinfo_set.create(user=user,return_status=False)
            self.rent_info=rent_info
            self.hold -= 1
            self.save()

    def return_book(self):
        self.rent_info.return_status = True
        self.rent_info.save()
        self.rent_info=None
        self.hold += 1
        self.save()

#대여기록
class RentInfo(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='대출회원')
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='대출도서')
    return_status = models.BooleanField("반납여부")

    def __str__(self):
        return "{}-{}".format(self.user, self.book)