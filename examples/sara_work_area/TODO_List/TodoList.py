import json
import os
import csv


from Item import Item


class TodoList:
    BASE_FILE_PATH = "./data/store_list.csv"

    def __init__(self):
        self.items = []

    def write_heading(self):
        self.open_write_file("Description,Status\n", 'w')  # writes heading of csv

    def if_header_exists(self):
        if not os.path.exists(self.BASE_FILE_PATH):  # checks if file exists
            self.write_heading()

    def add_items(self, description, status):
        """
        :param description: based on description, a check occurs to see if task already exists, if it does,
                            the task does not get added and "Task Already Exists" is returned
        :param status:
        :return: If task is not already in list i.e description doesn't match anything in data store, it will
                 then be sent to save_items function for saving.
        """

        read_list = self.open_write_file()

        if any(description.strip().lower() == task.split(",")[0].strip().lower() for task in read_list):
            print("Task Already in List")
        else:
            new_item = Item(description, status)
            self.items.append(new_item)
            self.save_items()
            print("List Saved")

    def save_items(self):
        """
        :return: takes data from add_items function, runs it through to_csv() for formatting, and saves to file.
        """

        data = "".join(item.to_csv() for item in self.items)
        self.open_write_file(data, "a")
        self.items.clear()

    def open_write_file(self, data="", state="r"):
        """
        contains all file related functions such as, Write, Read, Append to main file
        :param data: user inputted record
        :param state: a, r, or w
        :return: Data Saved Successfully!
        """
        with open(self.BASE_FILE_PATH, state) as list_file:
            if state in ["a", "w"]:
                list_file.write(data)
            elif state == "r":
                return [x.strip() for x in list_file.readlines()]

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

    # Another logic to implement the filter_items function using dict
    # def filter_items(self, status=""):
    #     items_list = self.open_write_file(state="r")
    #     filtered_dict = {}
    #     for item in items_list:
    #         description, item_status = item.split(',')
    #         description = description.strip()
    #         item_status = item_status.strip()
    #         if status == "completed" and "completed" in item_status:
    #             filtered_dict[description] = "completed"
    #         elif status == "pending" and "pending" in item_status:
    #             filtered_dict[description] = "pending"
    #         elif status == "":
    #             filtered_dict[description] = item_status
    #
    #     return json.dumps(filtered_dict)
