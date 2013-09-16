#!/usr/bin/env python
from kdoc import Processor

import sys
import pprint

if __name__ == '__main__':
    p = Processor()
    for f in sys.argv[1:]:
        p.add(f)

    p.process()

    f_count = len(p.functions)
    if f_count:
        pp = pprint.PrettyPrinter(indent=4)
        print "There are %d functions." % f_count
        print "---"

        for f in p.functions:
            print "Name:", f.name
            print "Category:", f.category
            print "Description:", ''.join(f.description)
            print "Sections:"

            pp.pprint(f.sections)

            print "---"

        print "The lookup table is:"
        pp.pprint(p.lookup_table)
