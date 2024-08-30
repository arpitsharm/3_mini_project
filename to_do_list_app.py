# fix the error of delete todo

def add_todo(write):
    with open("todo.txt", "a+") as fw:
        fw.write(f"{write}\n")


# fix the error of delete todo
# def delete_todo(delete):
#     with open("todo.txt", "a") as fd:
#         fd.replace(delete, '')

def show_all_todo():
    with open("todo.txt", "r") as fsa:
        read = fsa.read()

    print(read)

print("Welcome to todo application")
print("1.Add Todo")
print("2.Delete Todo")
print("3.Show All Todo")

choice = int(input("Enter your choice :- "))

if choice == 1:
    write_inp = input("Enter Todo Name :- ")
    add_todo(write_inp)

elif choice == 2:
    del_inp = input("Enter Delete Todo Name :- ")
    # delete_todo(del_inp)

elif choice == 3:
    show_all_todo()