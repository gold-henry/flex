import GrammarCompiler
import Flex

GL = GrammarCompiler.Lexer('./grammar.txt')
tokens, err = GL.lex()
if err:
    print(err)
    quit()

print(tokens)

flex = Flex.flex(grammar)

while True:
    text = input('flex > ')
    result, error = flex.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)
