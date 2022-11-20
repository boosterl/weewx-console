# Copyright 2022 Bram Oosterlynck

from setup import ExtensionInstaller

def loader():
    return ConsoleInstaller()

class ConsoleInstaller(ExtensionInstaller):
    def __init__(self):
        super(ConsoleInstaller, self).__init__(
            version="0.2",
            name='console',
            description='A console-friendly layout.',
            author="Bram Oosterlynck",
            author_email="bram.oosterlynck@gmail.com",
            config={
                'StdReport': {
                    'console': {
                        'skin':'console',
                        'HTML_ROOT':'console'}}},
            files=[('skins/console',
                    ['skins/console/current.tmpl',
                     'skins/console/week.tmpl',
                     'skins/console/skin.conf'])
                   ]
            )
