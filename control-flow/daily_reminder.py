# Daily Reminder Program

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop just to show control flow (ensures valid priority)
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Use match-case to handle different priorities
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Modify message if task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Print the final reminder
print("\nReminder:", reminder)
