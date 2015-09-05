from core import settings
from helpers.modules.NotificationModule import NotificationModule

import os


class Module(NotificationModule):
    def is_available(self):
        return os.system('notify-send --help > /dev/null') == 0

    def send(self, msg):
        os.system('notify-send "%s" "%s" &' % (settings.NAME, msg))