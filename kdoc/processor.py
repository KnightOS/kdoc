from .asmscanner import ASMScanner

class Processor(object):
    files = []

    functions = []
    lookup_table = {}

    def add(self, file):
        self.files.append(open(file))

    def process(self):
        for f in self.files:
            s = ASMScanner(f)
            s.process()

            self.functions.extend(s.functions)
            self.lookup_table.update(s.lookup_table)
