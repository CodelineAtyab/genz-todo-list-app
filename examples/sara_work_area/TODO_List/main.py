from TodoList import TodoList


def main():
    running = True
    todo_list = TodoList()
    todo_list.if_header_exists()
    while running:
        print("(1) Add to list")
        print("(2) Load To Do List")
        print("(3) Filter items (completed/pending)")
        print("(4) Exit")

        choice = int(input("Enter desired operation: "))

        if choice == 1:
            description = input("Enter Task Description: ")
            status = input("Enter status of Task (completed or pending): ")

            todo_list.add_items(description, status)

        if choice == 2:
            load_list = todo_list.open_write_file()
            print(load_list)

        if choice == 3:
            load_list = todo_list.filter_items("pending")
            print(load_list)

        if choice == 4:
            running = False
            print("App Closing...")


if __name__ == "__main__":
    main()