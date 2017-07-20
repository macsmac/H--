import sys
from interpreter import Interpreter

interpreter = Interpreter(open(sys.argv[1], "r").read())
interpreter.run()