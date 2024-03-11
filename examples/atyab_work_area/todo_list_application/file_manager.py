REMINDER_FILE_PATH = "./data/stored_reminders.txt"

def store_reminder(incoming_reminder):
  with open(REMINDER_FILE_PATH, "a") as reminder_file:
          reminder_file.write(incoming_reminder + "\n")

def read_reminders():
     with open(REMINDER_FILE_PATH, "r") as reminder_file:
          return [line.strip() for line in reminder_file.readlines()]
