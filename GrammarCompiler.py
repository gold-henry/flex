import string

import Error

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

LEXEME = 'LEXEME'
EXPANDS = 'EXPANDS'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
OR = 'OR'
INTERPRET = 'INTERPRET'
SYMBOL = 'SYMBOL'


class Token:
    def __init__(self, type, val=None):
        self.type = type
        self.val = val

    def __repr__(self):
        if self.val:
            return f'{self.type}:{self.val}'
        else:
            return self.type


class Lexer:
    def __init__(self, fn):
        self.fn = fn
        self.text = open(fn).read()
        self.idx = -1
        self.current_char = ''
        self.tokens = []

    def advance(self):
        self.idx += 1
        self.current_char = self.text[self.idx]

    def next_line(self):
        while(self.current_char != '\n'):
            self.advance()

    def lex(self):
        self.advance()
        while self.idx < len(self.text) - 1:

            if (self.current_char == '#'):
                self.next_line()

            if self.current_char == '(':
                self.tokens.append(Token(LPAREN))

            if self.current_char == ')':
                self.tokens.append(Token(RPAREN))

            if self.current_char == '|':
                self.tokens.append(Token(OR))

            if self.current_char == "'":
                sym = ''
                self.advance()
                while self.current_char != "'":
                    sym += self.current_char
                    self.advance()
                self.tokens.append(Token(SYMBOL, sym))

            if self.current_char == "{":
                sym = ''
                self.advance()
                while self.current_char != "}":
                    sym += self.current_char
                    self.advance()
                self.tokens.append(Token(INTERPRET, sym))

            if self.current_char == ":":
                self.advance()
                while self.current_char != "=":
                    self.advance()
                self.tokens.append(Token(EXPANDS))

            if self.current_char in LETTERS_DIGITS:
                name = ''
                while self.current_char in LETTERS_DIGITS:
                    name += self.current_char
                    self.advance()
                self.tokens.append(Token(LEXEME, name))

            self.advance()

        return self.tokens, None


class Pattern:
    def __init__(self):
        self.tokens = []


class Lexem:
    def __init__(self):
        self.patterns = []
        self.interpret = None


class Grammar:
    def __init__(self):
        self.lexems = []


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.idx = -1
        self.grammar = None

    def advance(self):
        self.idx += 1
        self.current_token = self.tokens[self.idx]

    def parseLexem(self):
        pass


"""
    def parseGrammar(self):
        grammar = Grammar()
        self.advance()
        # loop through all tokens
        while self.idx < len(self.tokens) - 1:
            self.grammar self.parseLexem()
"""
