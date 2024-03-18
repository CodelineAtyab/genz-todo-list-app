import file_manager


file_manager.create_file_if_not_exist()

# for _ in range(2):
#     new_row = ",".join(["92011497", "Atyab", "Al-Ansab"])
#     store_row_in_file(new_row)

try:
    file_manager.remove_row_from_file(1)
except Exception as ex:
    pass

# for row in get_rows_from_file():
#     print(row)
