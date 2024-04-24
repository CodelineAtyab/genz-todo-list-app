from TodoList import TodoList
from Item import Item


todo_list = TodoList()
todo_list.if_header_exists()


list_of_lines_in_file = []
# Open the file and read everything using readlines()
list_of_lines_in_file = TodoList.open_write_file()

for line in list_of_lines_in_file:
    description, status = line.split(",")
    todo_list.items.append(Item(description, status))


# todo_list.append_item(Item("Buy groceries", "pending"))
# todo_list.append_item(Item("Complete homework", "in progress"))
# todo_list.append_item(Item("Complete homewoddddrk", "in progrggess"))



