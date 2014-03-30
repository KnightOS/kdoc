class Function(object):
    def __init__(self):
        self.name = None
        self.description = []
        self.sections = {}
        self.sections_order = []
        self.line = 0
        self.path = None

    def __repr__(self):
        return self.name

    def finish(self):
        self.description = ' '.join(self.description)
        for section, v in self.sections.items():
            if section not in ['Inputs', 'Outputs']:
                self.sections[section] = ' '.join(v)

    def flatten(self):
        return {
            'name': self.name,
            'description': self.description,
            'sections': self.sections,
            'line': self.line,
            'path': self.path
        }
