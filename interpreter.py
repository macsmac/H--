from lexer import Lexer

from tags.printtag import PrintTag

class Interpreter():
	tags = {
		"print": PrintTag
	}

	def __init__(self, source):
		lexer = Lexer()
		lexer.feed(source)
		self.tree = lexer.tree

	def runTag(self, tag):
		name = str.lower(tag[0])

		if self.tags[name]:
			self.tags[name](tag)
		else:
			raise Error("Unknown tag")

	def run(self):
		for tag in self.tree[2]:
			self.runTag(tag)