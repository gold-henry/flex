class flex:
    def __init__(self, grammar):
        self.grammar = grammar

    def parseAST(self):
        pass

    def interpret(self):
        pass

    def run(self, text):
        self.parseAST(text)

        self.interpret()