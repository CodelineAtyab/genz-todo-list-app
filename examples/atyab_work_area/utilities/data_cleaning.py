FILE_TO_CLEAN = "./data/nlp_training_data.csv"
RESULT_FILE = "./data/cleaned_nlp_training_data.csv"


with open(RESULT_FILE, "w", encoding="utf8") as result_file:
    with open(FILE_TO_CLEAN, "r", encoding="utf8") as data_file:
        for line in data_file:
            try:
                decoded_str = line.strip()
                curr_row_values = decoded_str.split(",")
                if len(curr_row_values) > 1 and curr_row_values[0].strip() and curr_row_values[1].strip():
                    result_file.write(f"{curr_row_values[0]},\"{curr_row_values[1]}\"" + "\n")
            except Exception:
                pass

