import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic_site.test_settings")
django.setup()


test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['basic_site'])
    sys.exit(bool(failures))
