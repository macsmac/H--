from html.parser import HTMLParser

class Lexer(HTMLParser):
    tree = ["root", "", [], ""]
    blocks = []
    current = tree

    def handle_starttag(self, tag, attrs):
        self.current[2].append([tag, attrs, [], ""])
        self.blocks.append(self.current)
        self.current = self.current[2][-1]

    def handle_endtag(self, tag):
        self.current = self.blocks.pop()

    def handle_data(self, data):
        self.current[3] = data