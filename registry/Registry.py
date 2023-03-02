from Shorts_py.clerk.commands.Command import Command


class Console:

    def __init__(self):
        self.__commands = [
            Command().p,
            Command().s
        ]


    def communicate(self):

        while True:
            print('Введите команду')
            command = input()
            if command == 'exit':
                break
            for item in self.__commands:
                if command == item.__name__:
                    item()
                    break
            else:
                print('Несуществующая команда')






Console().communicate()
