from django.apps import AppConfig


class CrockerometerConfig(AppConfig):
    name = 'crockerometer'

    def ready(self):
      import crockerometer.signals
