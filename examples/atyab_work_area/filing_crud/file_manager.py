import os

_STORAGE_FILE_PATH = "./data_store.csv"


def _open_file_and_operate_on_data(new_line_content="", mode_of_operation="r"):
    """
    :param new_line_content: In case its is_a_write_operation then put this string in the file
    :param mode_of_operation: Can be "w", "a" and "r"
    :return: Empty list in case of a "r" operation and a populated list in case of a "w" and "a" operation
    """
    is_a_write_operation = True if mode_of_operation in ["w", "a"] else False
    lines_in_file = []
    with open(_STORAGE_FILE_PATH, mode_of_operation) as data_store_file:
        if is_a_write_operation:
            data_store_file.write(new_line_content + "\n")
        else:
            lines_in_file = [line.strip() for line in data_store_file.readlines()]

    return lines_in_file


def write_initial_header(header_content="contact_no,name,address"):
    _open_file_and_operate_on_data(header_content, mode_of_operation="w")


def create_file_if_not_exist():
    if not os.path.exists(_STORAGE_FILE_PATH):
        write_initial_header()
        print("[INFO] Created file successfully!")


def store_row_in_file(new_line_content):
    """
    Adds a record at the end of the file.
    """
    _open_file_and_operate_on_data(new_line_content, "a")
    print("[INFO] Added a row successfully!")


def remove_row_from_file(line_no=None):
    """
    Removes a specific line based on a line number.
    :param line_no: The integer line number of the actual file.
    :return: An updated list of strings. Each string represents a line.
    """
    all_lines_in_file = get_rows_from_file()
    del all_lines_in_file[line_no-1]

    write_initial_header()  # Reset the file and just write the header first
    for line in all_lines_in_file:
        _open_file_and_operate_on_data(new_line_content=line, mode_of_operation="a")


def update_row_in_file(line_no, new_line_content):
    """
    Updates a specific line. Replace the given line with the existing one.
    :param line_no: The integer line number of the actual file.
    :param new_line_content: The string to replace the existing line with.
    :return: A updated list of strings. Each string represents a line.
    """
    pass


def get_rows_from_file(line_no=None):
    """
    Get specific row if line_no is given, otherwise get all the lines.
    :param line_no: The integer line number of the actual file.
    :return: A list of strings. Each string represents a line.
    """
    return _open_file_and_operate_on_data()[1:]


