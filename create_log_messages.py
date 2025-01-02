import random
import datetime

# Categories of log messages
categories = ["User Actions", "System Events", "Error Messages"]

# Sample data for message generation
users = [f"user_{i}" for i in range(1, 101)]
reports = [f"report_{i}" for i in range(1, 51)]
formats = ["PDF", "Excel", "CSV"]
errors = ["Database timeout", "Unauthorized action", "Email delivery failure", "Data not found", "Permission denied", "Invalid input"]
actions = [
    "logged in", "logged out", "generated a report", "exported a report", "scheduled an email", 
    "deleted a report", "updated account settings", "changed password", "viewed dashboard"
]
events = [
    "Data sync completed", "Report generated", "Email sent", "Scheduled task executed", 
    "Cache cleared", "System backup completed", "Maintenance window started", "API request processed"
]
systems = ["CRM", "Database", "Reporting Engine", "Email Server", "Cache Service"]

# Generate a random timestamp
def random_timestamp():
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

# Generate log messages
def generate_log_messages(count):
    messages = []
    for _ in range(count):
        category = random.choice(categories)
        timestamp = random_timestamp()
        if category == "User Actions":
            user = random.choice(users)
            action = random.choice(actions)
            report = random.choice(reports)
            format = random.choice(formats)
            messages.append(f"[{timestamp}] INFO: {user} {action} (Report: {report}, Format: {format}).")
        elif category == "System Events":
            event = random.choice(events)
            system = random.choice(systems)
            messages.append(f"[{timestamp}] INFO: {event} on {system}.")
        elif category == "Error Messages":
            user = random.choice(users)
            error = random.choice(errors)
            report = random.choice(reports)
            messages.append(f"[{timestamp}] ERROR: {user} encountered an error: {error} (Report: {report}).")
    return messages

# Generate 1000 log messages
log_messages = generate_log_messages(1000)

# Write to a file
with open("log_messages.txt", "w") as file:
    file.write("\n".join(log_messages))

print("Log messages generated and saved to 'log_messages.txt'.")
