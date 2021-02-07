import json
from io import StringIO

from django.core.management import call_command


def test_command_output(db, tmp_path, locations_data):
    filename = tmp_path / "load_locations_data.json"
    with open(filename, 'w') as file_obj:
        json.dump(locations_data, file_obj)

    out = StringIO()
    call_command('load_locations', filename, stdout=out)
    expected = f'Successfully imported {filename} ({len(locations_data)} locations)\n'

    assert expected == out.getvalue()
