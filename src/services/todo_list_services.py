from models.todolist import TodoList
from models.item import Item



todo_list = TodoList()
todo_list.if_header_exists()


list_of_lines_in_file = []
# Open the file and read everything using readlines()
list_of_lines_in_file = TodoList.open_write_file()

for line in list_of_lines_in_file:
    description, status = line.split(",")
    todo_list.items.append(Item(description, status))


if __name__ == "__main__":
    print(todo_list.filter_items("pending"))
    todo_list.append_item(Item("Buy groceries", "pending"))
    todo_list.append_item(Item("Complete homework", "completed"))
    todo_list.append_item(Item("Complete homewoddddrk", "pending"))



