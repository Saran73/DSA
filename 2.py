stack = []
def push():
    if len(stack) == n:
        print("stack is full")
    else:
        element = input("enter the elements: ")
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("elements removed:",e)
        print(stack)

n = int(input())
while True:
    print("select the operation 1 push, 2 pop, 3 exit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    else:
        print("enter the correct expression!")

