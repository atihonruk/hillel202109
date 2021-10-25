from django.db import models

# CREATE_BOOKS = '''
# create table if not exists books (
#   id integer primary key,
#   title CHAR(256),
#   isbn CHAR(256),
#   published DATE
# );


class Book(models.Model):
    title = models.CharField(max_length=256)
    isbn = models.CharField(max_length=256)
    published = models.DateField()

# CREATE_AUTHORS = '''
# create table if not exists authors (
#   id integer primary key,
#   name CHAR(100),
#   email CHAR(256)
# );
# '''

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    

# CREATE_BOOKS_AUTHORS = '''
# create table if not exists book_authors (
#   id integer primary key,
#   author_id integer,
#   book_id integer,
#   FOREIGN KEY(author_id) REFERENCES authors(id),
#   FOREIGN KEY(book_id) REFERENCES books(id)
# );



class ImmunizationLegalEntities(models.Model):
    legal_entity_id = models.TextField(blank=True, null=True)
    legal_entity_name = models.TextField(blank=True, null=True)
    legal_entity_edrpou = models.TextField(blank=True, null=True)
    care_type = models.TextField(blank=True, null=True)
    property_type = models.TextField(blank=True, null=True)
    legal_entity_email = models.TextField(blank=True, null=True)
    legal_entity_phone = models.TextField(blank=True, null=True)
    legal_entity_owner_name = models.TextField(blank=True, null=True)
    registration_area = models.TextField(blank=True, null=True)
    registration_settlement = models.TextField(blank=True, null=True)
    registration_addresses = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lng = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'immunization_legal_entities'
