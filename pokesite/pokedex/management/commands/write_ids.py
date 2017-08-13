from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import get_object_or_404
from pokedex.models import * 

class Command(BaseCommand):

    print PokemonType.objects.all()



    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("written!"))
