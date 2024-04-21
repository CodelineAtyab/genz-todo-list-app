import os
import json

from models.item import Item


class TodoList:
    BASE_FILE_PATH = "../data/store_list.csv"

    def __init__(self):
        self.items = []

    @staticmethod
    def get_heading():
        return f"Description,Status\n"

    def write_heading(self):
        self.open_write_file(self.get_heading(), 'w')  # writes heading of csv

    def if_header_exists(self):
        if not os.path.exists(self.BASE_FILE_PATH):  # checks if file exists
            self.write_heading()

    def validate_item(self, item):
        """
        :param item: based on description, a check occurs to see if task already exists, if it does,
                            the task does not get added and "Task Already Exists" is returned
        """

        return any(item.description.strip().lower() == existing_item.description.strip().lower() for existing_item in
                   self.items)

    def append_item(self, item):
        if self.validate_item(item):
            print("Task Already in List")
        else:
            self.items.append(item)
            self.save_items()
            print("List Saved")

    def save_items(self):
        """
        :return: takes data from add_items function, runs it through to_csv() for formatting, and saves to file.
        """
        # data = self.get_heading()
        data = "".join(item.to_csv() for item in self.items)

        self.open_write_file(data, "w")

    @staticmethod
    def open_write_file(data="", state="r"):
        """
        contains all file related functions such as, Write, Read, Append to main file
        :param data: user inputted record
        :param state: a, r, or w
        :return: Data Saved Successfully!
        """
        try:
            with open(TodoList.BASE_FILE_PATH, state) as list_file:
                if state in ["a", "w"]:
                    list_file.write(data)
                elif state == "r":
                    return [x.strip() for x in list_file.readlines()]
        except Exception as ex:
            print("Error", ex)

    def filter_items(self, status=""):
        """
        A function to return items based on their status (pending/completed)
        :param status: pending, completed, or none
        :return: a filtered list of items in a json format
        """
        items_list = self.open_write_file(state="r")
        if status == "completed":
            filtered_list = [item.split(',')[0].strip() for item in items_list if "completed" in item]
        elif status == "pending":
            filtered_list = [item.split(',')[0].strip() for item in items_list if "pending" in item]
        else:
            filtered_list = [item.strip() for item in items_list]
        return json.dumps(filtered_list)
