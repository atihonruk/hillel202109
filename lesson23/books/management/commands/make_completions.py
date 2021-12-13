from django.core.management import BaseCommand

from books.autocomplete import model_completions
from books.models import Book

DEBUG = True


class Command(BaseCommand):
    help = 'Make completions'
    
    def handle(self, *args, **kwargs):
        completions = model_completions(Book, 'title')
        self.stdout.write(f'{len(completions)} competions added')
        if DEBUG:
            for c in completions:
                self.stdout.write(c)
