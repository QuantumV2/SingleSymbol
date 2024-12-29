import interpreter
import sys

with open(sys.argv[1], "r") as f:
    content = f.read()

interp = interpreter.Interpreter()
interp.execute(content)