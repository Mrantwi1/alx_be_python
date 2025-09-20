# Daily Reminder Program

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle priorities
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority"

# Add time sensitivity message
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = f"Note: {message}. Consider completing it when you have free time."

# ✅ Print customized reminder
print(f"Reminder: {message}")

