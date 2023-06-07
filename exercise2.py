class Python():
    def __init__(self, string):
        self.string = string

    def get_string(self):
        self.string = input('Input msg here: ')
        print(self.string)

    def print_string(self):
        print(self.string.upper())

x = Python('hello world')
x.print_string()
x.get_string()
x.print_string()

y = Python('hello dude')
y.print_string()