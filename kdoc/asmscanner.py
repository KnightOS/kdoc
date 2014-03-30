from plex import *

from .models import Function

ENUMERATED_SECTIONS = ['Inputs', 'Outputs']

class ASMScanner(Scanner):
    f = None
    current_section = None
    current_field = None

    functions = []
    lookup_table = {}
    category_table = {}

    line = 0

    def current_level(self):
        return self.indentation_stack[-1]

    def newline(self, text):
        self.begin('code')
        self.line += 1

        return 'newline'

    def indent(self, text):
        current_level = self.current_level()
        new_level = len(text) - 2 # len(";;") == 2

        if new_level > current_level:
            self.indent_to(new_level)
        else:
            self.dedent_to(new_level)

        if current_level == 0 and new_level == 1:
            self.f = Function()

        #if current_level == 1 and new_level == 0:

        if new_level == 1:
            if not self.f.name:
                self.begin("name")
            else:
                self.begin("section")
        else:
            if not self.current_section:
                self.begin("description")
            else:
                if self.current_section in ENUMERATED_SECTIONS:
                    self.begin('field_name')
                else:
                    self.begin("section_text")


    def indent_to(self, new_level):
        self.indentation_stack.append(new_level)
        self.produce("INDENT", "")

    def dedent_to(self, new_level):
        while new_level < self.current_level():
            self.indentation_stack.pop()
            self.produce("DEDENT", "")

    def eof(self):
        if self.f.name:
            self.f.finish()
            self.functions.append(self.f)
            self.lookup_table[self.f.name] = self.f.category
            if self.f.category not in self.category_table:
                self.category_table[self.f.category] = [self.f]
            else:
                self.category_table[self.f.category].append(self.f)

        self.current_section = None
        self.f = Function()
        self.dedent_to(0)

    def doc_end(self, _):
        self.eof()

    # Actual parsing

    def function_name(self, text):
        self.f.name = text.strip()
        self.f.line = self.line + 1
        self.f.path = self.path

    def category_name(self, text):
        self.f.category = text

    def section_name(self, text):
        self.current_section = text
        self.f.sections_order.append(text)
        self.f.sections[text] = [] if text not in ENUMERATED_SECTIONS else {}

    def description_line(self, text):
        self.f.description.append(text)

    def section_text(self, text):
        self.f.sections[self.current_section].append(text)

    def field_name(self, text):
        self.current_field = text
        self.begin('field_value')

    def field_value(self, text):
        self.f.sections[self.current_section][self.current_field] = text[2:]
        self.current_field = None

    lexicon = Lexicon([
        State('code', [
            (Str(";;") + Rep(Str(" ")), indent),
            (Str("\n"), newline),
            (AnyBut(";"), doc_end),
            (AnyChar, TEXT)
        ]),
        State('name', [
            (Rep(AnyBut("[")), function_name),
            (Str("["), Begin("category")),
        ]),
        State('category', [
            (Rep(AnyBut("]")), category_name),
            (Str("]"), Begin(""))
        ]),
        State('section', [
            (Rep(AnyBut(":")), section_name),
            (Str(":"), Begin(""))
        ]),
        State('description', [
            (Rep(AnyBut("\n")), description_line),
            (Str("\n"), newline)
        ]),
        State('section_text', [
            (Rep(AnyBut("\n")), section_text),
            (Str("\n"), newline)
        ]),
        State('field_name', [
            (Rep(AnyBut(":")), field_name),
        ]),
        State('field_value', [
            (Rep(AnyBut("\n")), field_value),
            (Str("\n"), newline)
        ]),
        (Str("\n") | Eof, newline),
        (AnyChar, TEXT)
    ])

    def process(self):
        t = self.read()
        while t[0] != None:
            t = self.read()

    def __init__(self, file):
        Scanner.__init__(self, self.lexicon, file)
        self.f = Function()
        self.path = file.name
        self.functions = []
        self.lookup_table = {}
        self.indentation_stack = [0]
        self.begin('code')
