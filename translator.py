def bf_to_at(bf_code):
    translation = {
        '>': '@',
        '<': '@@',
        '+': '@@@',
        '-': '@@@@',
        '.': '@@@@@',
        ',': '@@@@@@',
        '[': '@@@@@@@',
        ']': '@@@@@@@@'
    }

    result = []
    for char in bf_code:
        if char in translation:
            result.append(translation[char])

    return ' '.join(result)

def at_to_bf(at_code):
    translation = {
        1: '>',
        2: '<',
        3: '+',
        4: '-',
        5: '.',
        6: ',',
        7: '[',
        8: ']'
    }

    clean_code = ''.join(c for c in at_code if c in ['@', ' ', '\n', '\t'])
    instructions = clean_code.split()
    result = []

    for inst in instructions:
        count = sum(1 for c in inst if c == '@')
        if count in translation:
            result.append(translation[count])

    return ''.join(result)