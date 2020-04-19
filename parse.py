from ast import *


replacements = {
    "()": "p",
    "{}": "P",
    "[]": "n",
    "<>": "t"
}

brackets = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

nilads = {
    "p": lambda: 1,
    "P": Pop,
    "n": Height,
    "t": Toggle
}

monads = {
    "()": Push,
    "[]": Negate,
    "{}": Loop,
    "<>": Suppress
}

def parse(program):
    # lmao
    for trigger, repl in replacements.items():
        program = program.replace(repl, "").replace(trigger, repl)

    parse_stack = [Program()]
    for char in program:
        if char in nilads:
            parse_stack[-1].expr.append(nilads[char]())
        elif char in brackets:
            monad = monads.get(char + brackets[char])
            if monad:
                parse_stack.append(monad())
        elif char in brackets.values():
            t = parse_stack.pop()
            parse_stack[-1].expr.append(t)

    return parse_stack[0]
