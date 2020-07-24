from django.apps import AppConfig


class WakeSysConfig(AppConfig):
    name = 'wake_sys'

    def ready(self):
        import wake_sys.signals