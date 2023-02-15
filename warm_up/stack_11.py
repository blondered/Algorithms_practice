from sys import stdin

class Stack(list):
    length = 0
    def not_empty(self):
        if self.length == 0:
            print("error")
            return False
        return True
    def proceed_command(self, full_command):
        read_args = full_command.split()
        command = read_args[0]
        if command == "exit":
            print("bye")
            exit(0)
        elif command == "push":
            print("ok")
            self.length += 1
            self.append(int(read_args[1]))
        elif command == "back":
            if self.not_empty():
                print(self[-1])
        elif command == "pop":
            if self.not_empty():
                print(self.pop())
                self.length -= 1
        elif command == "size":
            print(self.length)
        elif command == "clear":
            print("ok")
            self.length = 0
            self.clear()


def main():
    stack = Stack()
    while True:
        stack.proceed_command(stdin.readline())


if __name__ == "__main__":
    main()
