#  ________________  .___.____       
#  \_   _____/  _  \ |   |    |      
#   |    __)/  /_\  \|   |    |      
#   |     \/    |    \   |    |___   
#   \___  /\____|__  /___|_______ \  
#       \/         \/            \/  



##########################################
#Tokens
##########################################

TT_INT      = 'TT_INT'
TT_FLOAT    = 'TT_FLOAT'
TT_MINUS    = 'TT_MINUS'
TT_MUL      = 'TT_MUL'
TT_DIV      = 'TT_DIV'
TT_LPAREN   = 'TT_LPAREN'
TT_RPAREN   = 'TT_RPAREN'

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'



##########################################
#Lexer
##########################################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.char != None:
            if self.current_char in '\t':
                self.advance()
            elif 

        return tokens