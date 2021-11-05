from django.db import models
from django.conf import settings

# CREATE_BOOKS = '''
# create table if not exists books (
#   id integer primary key,
#   title CHAR(256),
#   isbn CHAR(256),
#   published DATE
# );


class Book(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=256)
    isbn = models.CharField(max_length=256)
    published = models.DateField(help_text='Published date')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    prev_edition = models.ForeignKey('Book',
                                     on_delete=models.CASCADE,
                                     blank=True, null=True)
    authors = models.ManyToManyField('Author')
    

# CREATE_AUTHORS = '''
# create table if not exists authors (
#   id integer primary key,
#   name CHAR(100),
#   email CHAR(256)
# );
# '''


class Author(models.Model):
    MALE, FEMALE, NOT_SPECIFIED = range(3)
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOT_SPECIFIED, 'Not specified'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL,
    #                            on_delete=models.CASCADE)


    
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

# C - create
# R - retrieve
# U - update
# D - delete

# class User(AbstractUser):
#    phone = models.CharField()
#    gender = models.CharField(choices=...)
