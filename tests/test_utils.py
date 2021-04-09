from dbci.utils import yaml2dict


def test_yaml2dict():
    assert yaml2dict("test-1.yaml") == {
        'name': 'tudat',
        'assets': [
            {'name': 'NASA-NAIF',
             'type': 'index',
             'url': 'https://naif.jpl.nasa.gov/pub/naif/'}
        ]
    }
