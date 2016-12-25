#!/usr/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'genpac==1.4.1','console_scripts','genpac'
__requires__ = 'genpac==1.4.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('genpac==1.4.1', 'console_scripts', 'genpac')()
    )
