#!/usr/bin/env python

'''
test_emojify_python_script.py

# Description
Test emojify_python_script.py for basic functionality

# Usage
python test_emojify_python_script.py

# License
Copyright (c) 2018, Chris Rands.
Redistribution and use of this code, with or without modification, are permitted,
provided that the the above copyright notice is included.
'''

import unittest
import sys
from emojify_python_script import emojify_string

__author__ = 'Chris Rands'
__copyright__ = 'Copyright (c) 2018, Chris Rands'

INPUT1 = "print('hello world')\n"
OUTPUT1 = 'from collections import OrderedDict\nexec("".join(map(chr,[int("".join(str(OrderedDict([(\':)\', 0),\n             (\':D\', 1),\n             (\':P\', 2),\n             (\':S\', 3),\n             (\':(\', 4),\n             (\'=)\', 5),\n             (\'=/\', 6),\n             (\':/\', 7),\n             (\':{\', 8),\n             (\';)\', 9)])[i]) for i in x.split())) for x in\n":D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  :D :) \\\n:(  :D :) :D  :D :) :{  :D :) :{  :D :D :D  :S :P  :D :D ;)  :D :D :D \\\n :D :D :(  :D :) :{  :D :) :)  :S ;)  :( :D  :D :)"\n.split("  ")])))\n'

INPUT2 = "print('hello world')\ndef add(n1,n2):\n    return n1 + n2\nprint('4 + 4 = {}'.format(add(4,4)))\n"
OUTPUT2 = 'from collections import OrderedDict\nexec("".join(map(chr,[int("".join(str(OrderedDict([(\':)\', 0),\n             (\':D\', 1),\n             (\':P\', 2),\n             (\':S\', 3),\n             (\':(\', 4),\n             (\'=)\', 5),\n             (\'=/\', 6),\n             (\':/\', 7),\n             (\':{\', 8),\n             (\';)\', 9)])[i]) for i in x.split())) for x in\n":D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  :D :) \\\n:(  :D :) :D  :D :) :{  :D :) :{  :D :D :D  :S :P  :D :D ;)  :D :D :D \\\n :D :D :(  :D :) :{  :D :) :)  :S ;)  :( :D  :D :)  :D :) :)  :D :) :D\\\n  :D :) :P  :S :P  ;) :/  :D :) :)  :D :) :)  :( :)  :D :D :)  :( ;)  \\\n:( :(  :D :D :)  =) :)  :( :D  =) :{  :D :)  :S :P  :S :P  :S :P  :S :\\\nP  :D :D :(  :D :) :D  :D :D =/  :D :D :/  :D :D :(  :D :D :)  :S :P  \\\n:D :D :)  :( ;)  :S :P  :( :S  :S :P  :D :D :)  =) :)  :D :)  :D :D :P\\\n  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  =) :P  :S :P  \\\n:( :S  :S :P  =) :P  :S :P  =/ :D  :S :P  :D :P :S  :D :P =)  :S ;)  :\\\n( =/  :D :) :P  :D :D :D  :D :D :(  :D :) ;)  ;) :/  :D :D =/  :( :)  \\\n;) :/  :D :) :)  :D :) :)  :( :)  =) :P  :( :(  =) :P  :( :D  :( :D  :\\\n( :D  :D :)"\n.split("  ")])))\n'


class TestFunctions(unittest.TestCase):
    """Unit tests"""
    # TODO: expand testing

    def test_emojify_string1(self):
        """First test"""
        self.assertEqual(emojify_string(INPUT1), OUTPUT1)

    def test_emojify_string2(self):
        """Second test"""
        self.assertEqual(emojify_string(INPUT2), OUTPUT2)


def main():
    """Run unit tests"""
    if sys.version_info.major != 3:
        print('Error: unit tests for Python 3 only, exiting')
        raise SystemExit
    unittest.main()


if __name__ == '__main__':
    main()
