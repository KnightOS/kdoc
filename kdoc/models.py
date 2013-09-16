class Function(object):
    def __init__(self):
        self.name = None
        self.description = [] 
        self.sections = {}

    def __repr__(self):
        return self.name
