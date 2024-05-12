class Conversion:

    def __init__(self):
        pass

    def letter_value(self, letter: str):
        return ord(letter) - ord('a') + 1

    def char_value(self, input_list):
        for char in input_list:
            if char == '_':
                return 0
            else:
                return self.letter_value(char)

    def get_merged_list(self, input_string):
        merged_list = []
        merged_value = 0
        for digit in input_string:
            if digit == 26:
                merged_value += 26
            else:
                merged_list.append(digit + merged_value)
                merged_value = 0
        return merged_list

    def converted_string(self, input_string):
        char_list = [self.char_value(input_string[i]) for i in range(len(input_string))]
        result_list = []
        merged_list = self.get_merged_list(char_list)
        while merged_list:
            counter = merged_list.pop(0)
            result_list.append(sum(merged_list[0:counter]))
            merged_list = merged_list[counter:]
        return f"Result list: {result_list}"


# user_string = Conversion()
# print(user_string.converted_string("abcdabcdab"))


# def converted_string(self, input_string):
#     char_list = list(input_string)
#     result_list = []
#     while char_list:
#         encode_by = 0
#         while char_list[0] == 'z':
#             char_list.pop(0)
#             encode_by += 26
#         encode_by += char_value(char_list[0])
#         char_list.pop(0)
#         total, index = 0, 0
#         for _ in range(encode_by):
#             if char_list[index] != 'z':
#                 value = char_value(char_list[index])
#                 total += value
#             else:
#                 while char_list[index] == 'z':
#                     total += 26
#                     index += 1
#                 total += char_value(char_list[index])
#             index += 1
#         result_list.append(total)
#         char_list = char_list[index:]
#
#     return f"Result list: {result_list}"
