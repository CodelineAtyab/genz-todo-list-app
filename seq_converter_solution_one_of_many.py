def convert_seq_to_numbers(inc_seq: str):
    """
    Converts a sequence of characters to a list of numbers, eliminating z, which is a continuation character.
    :param inc_seq: A sequence of characters in the form of a string.
    :return: A list of integers.
    """
    result_number_list = []
    z_zone = False
    z_zone_sum = 0
    for char in inc_seq:
        offset_val = 97 if char != "_" else 96  # Offset based on ASCII mapping. To start from 0 in case of 'a'.
        number_repr = ord(char) - offset_val + 1    # Since our representation is 1 for 'a' so we add 1.

        # Set z zone if any z is encountered and calculate sum until we get a non-z character
        if char == "z":
            z_zone = True
            z_zone_sum += number_repr
        else:
            z_zone = False

        if not z_zone:
            # If we are out of the z zone, then put the current non z char value in sum and skip to the next char
            if z_zone_sum > 0:
                z_zone_sum += number_repr
                result_number_list.append(z_zone_sum)
                z_zone_sum = 0

            # This is the normal case where there is no z around.
            else:
                result_number_list.append(number_repr)

    return result_number_list


def process_seq_and_generate_result(list_of_num_in_seq: list[int]):
    """
    Processes a list of numbers based on steps and sum included in those steps.
    :param list_of_num_in_seq: Incoming list of integers that needs to be compressed.
    :return: List of compressed integers based on steps.
    """
    result_package_list = []
    is_a_step = True  # First number is always a step.
    step_count_remaining = 0  # Set the count as soon as the number is encountered.
    curr_package_sum = 0  # Until step_count_remaining is not 0, keep adding the numbers in this cache.

    for curr_num in list_of_num_in_seq:
        if is_a_step:
            step_count_remaining = curr_num
            is_a_step = False
        elif step_count_remaining > 0:
            curr_package_sum += curr_num
            step_count_remaining -= 1

            if step_count_remaining == 0:  # Before exiting the iteration, append the result and reset the cycle.
                result_package_list.append(curr_package_sum)
                curr_package_sum = 0
                is_a_step = True

    return result_package_list


if __name__ == "__main__":
    input_seq = "za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"
    seq_converted_to_numeric_list = convert_seq_to_numbers(input_seq)
    print(seq_converted_to_numeric_list)
    print(process_seq_and_generate_result(seq_converted_to_numeric_list))
