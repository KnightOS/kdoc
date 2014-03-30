from kdoc.asmscanner import ASMScanner

class Processor(object):
    files = []

    functions = []
    lookup_table = {}
    category_table = {}

    def add(self, file):
        self.files.append(open(file))

    def process(self):
        for f in self.files:
            s = ASMScanner(f)
            s.process()

            self.functions.extend(s.functions)
            self.lookup_table.update(s.lookup_table)
            self.category_table.update(s.category_table)

    def flatten(self):
        return dict([
            (name, {f.name: f.flatten() for f in function_list})
            for name, function_list in self.category_table.items()
        ])
