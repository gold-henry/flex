class Error:
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return "Error: " + self.msg


class GrammarSymbolError(Error):
    def __init__(self, msg):
        super().__init__(msg)

    def __repr__(self):
        return "Grammar Symbol Error: " + self.msg


class GrammarParseError(Error):
    def __init__(self, msg):
        super().__init__(msg)

    def __repr__(self):
        return "Grammar Parsing Error: " + self.msg
