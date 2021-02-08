import json

from django.core.management.base import BaseCommand

from weather.models import Location


class Command(BaseCommand):
    help = 'Load locations in JSON format'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options.get('filename')

        with open(filename) as json_file:
            data = json.load(json_file)
            locations = [
                Location(**{
                    'code': location['ID'],
                    'name': location['Name'],
                })
                for location in data
            ]
            objs = Location.objects.bulk_create(locations)
            total = len(objs)

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {filename} ({total} locations)'))
