SYMBOL = "@"
class Interpreter:
    def __init__(self):
        self.tape = {}
        self.ptr = 0
    
    def clean_instruction(self, instruction):
        return ''.join(char for char in instruction if char in [SYMBOL, ' ', '\n', '\t'])

    def count_symbol(self, instruction):
        return sum(1 for char in instruction if char == SYMBOL)
    
    def get_cell(self, ptr):
        return self.tape.get(ptr, 0)
    def set_cell(self, ptr, value):
        if value < 256:
            self.tape[ptr] = value
        else:
            self.tape[ptr] = 0
        if value < 0:
            self.tape[ptr] = 255

    def find_matching_loops(self, instructions):
        loop_starts = []
        loop_map = {}
        
        for i, inst in enumerate(instructions):
            count = self.count_symbol(inst)
            if count == 7:  # [
                loop_starts.append(i)
            elif count == 8:  # ]
                if not loop_starts:
                    raise SyntaxError("Unmatched closing loop")
                start = loop_starts.pop()
                loop_map[start] = i
                loop_map[i] = start
        
        if loop_starts:
            raise SyntaxError("Unmatched opening loop")
        return loop_map

    def execute(self, code):
        clean_code = self.clean_instruction(code)
        instructions = clean_code.split()
        loop_map = self.find_matching_loops(instructions)
        
        i = 0
        while i < len(instructions):
            count = self.count_symbol(instructions[i])
            match count:
                case 1:
                    self.ptr += 1
                case 2:
                    if self.ptr > 0:
                        self.ptr -= 1
                case 3:
                    self.set_cell(self.ptr, self.get_cell(self.ptr) + 1)
                case 4:
                    self.set_cell(self.ptr, self.get_cell(self.ptr) - 1)
                case 5:
                    print(chr(self.get_cell(self.ptr)), end='')
                case 6:
                    self.set_cell(self.ptr, int(input()))
                case 7: 
                    if self.get_cell(self.ptr) == 0:
                        i = loop_map[i] 
                case 8:
                    if self.get_cell(self.ptr) != 0:
                        i = loop_map[i] 
            i += 1