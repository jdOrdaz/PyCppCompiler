# Token class allow for tuples organization
class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
