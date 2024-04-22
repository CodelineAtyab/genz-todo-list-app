from src.models.todolist import TodoList
from src.models.item import Item
import pickle

__PICKLE_FILE_PATH = "./data/store_list.pkl"

todo_list = TodoList()
todo_list.if_header_exists()


list_of_lines_in_file = []
# Open the file and read everything using readlines()
list_of_lines_in_file = TodoList.open_write_file()

for line in list_of_lines_in_file:
    description, status = line.split(",")
    todo_list.items.append(Item(description, status))

"""
    This function creates a pickle file from a list of todo items. 
    It's just a proof of concept.
"""
def create_pickle_file(todo_items, pickle_file):
    # Save todo_list to pickle file
    with open(pickle_file, 'wb') as f:
        pickle.dump(todo_list, f)

if __name__ == "__main__":

    # proof of concept for pickle
    create_pickle_file(todo_list.items, __PICKLE_FILE_PATH)
    
    print(todo_list.filter_items("pending"))
    todo_list.append_item(Item("Buy groceries", "pending"))
    todo_list.append_item(Item("Complete homework", "completed"))
    todo_list.append_item(Item("Complete homewoddddrk", "pending"))

