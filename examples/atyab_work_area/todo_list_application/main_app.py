import file_manager

data = []

def main():
  app_running = True
  while app_running:
    print("(1) Save a reminder.")
    print("(2) View all reminders.")
    print("(3) Search for a specific reminders.")
    print("(4) Exit.")

    user_input = input("Please select one of the options: ")
    
    if user_input and user_input.isdigit():
      selected_choice = int(user_input)

      reminder_input = ""
      if selected_choice == 1:
        reminder_input = input("Please specify, what to add: ")
        data.append(reminder_input)
        file_manager.store_reminder(reminder_input)
      elif selected_choice == 2:
        for index, reminder in enumerate(file_manager.read_reminders()):
          print(f"{index + 1} <--> {reminder}")
      elif selected_choice == 3:
        pass
      elif selected_choice == 4:
        app_running = False

if __name__ == "__main__":
  main()