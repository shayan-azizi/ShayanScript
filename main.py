# Error | SUSY CLASS! :))
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
        
    def as_string (self):
        responce = f"{self.error_name}: {self.details}"
        return responce

class IllegalCharError(Error):
    
    def __init__(self, details):
        super.__init__("Illegal Character", details)
        



# Tokens

digits = '0123456789'

TT_INT = "TT_INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAEREN"


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
        
    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"
    
# Lexer

class Lexer:
    def __init__(self, text):
        
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance (self):
        
        self.pos += 1
        self.current_char = self.text [pos] if self.pos < len(self.text) else None
        
    def make_token (self):
        
        tokens = []
        
        while self.current_char != None:
            
            if self.current_char in ' \t':
                self.advance()
                
            elif self.current_char in digits:
                tokens.append(self.make_number())
            
            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
                
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
                
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()

            elif self.current_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()

            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
                
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()
                
            else:
                char = self.current_char
                self.advance()
                
                return [], IllegalCharError("'" + char + "'")
            
        return tokens, None
    
    def make_number ():
        num_str = ""
        dot_counter = 0
        
        while self.current_char and self.current_char in digits + '.':
            if self.current_char == ".":
                if dot_counter == 1: 
                    break
                dot_counter += 1
                num_str += '.'
            else:
                num_str += self.current_char
        
        if dot_counter == 0:
            return Token(TT_INT, int(num_str)) 
        
        else:
            return Token(TT_FLOAT, float(num_str))
        
        
    