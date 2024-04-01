class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def sayFirstName(self):
        print('мое имя', self.first_name)
       
    def sayLastName(self):
        print('моя фамилия', self.last_name)

    def sayFirstLastName(self):
        print('меня зовут', self.first_name, self.last_name)