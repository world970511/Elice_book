# csv->db 를 위한 파일
# manage.py 경로에 db_uploader.py
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from books.models import BookInfo # django.setup() 이후에 임포트해야 오류가 나지 않음

CSV_PATH_PRODUCTS='./elice_book.csv'
path='./media/book_img'
dic={}
for i in os.listdir(path):dic[os.path.splitext(i)[0]]=i

with open(CSV_PATH_PRODUCTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        for row in data_reader:
                img=dic[row[0]] if row[0] in dic else None
                BookInfo.objects.create(
                        image='book_img/'+img,
                        book_name = row[1],
                        publisher = row[2],
                        author = row[3],
                        publication_date = row[4],
                        pages = row[5],
                        isbn = row[6],
                        description = row[7],
                        link = row[8],
                        hold=1,
                 )







