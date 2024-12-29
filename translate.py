import translator
import sys

with open(sys.argv[2], "r") as f:
    content = f.read()

if sys.argv[1] == "bf_to_at":
    print(translator.bf_to_at(content))
elif sys.argv[1] == "at_to_bf":
    print(translator.at_to_bf(content))