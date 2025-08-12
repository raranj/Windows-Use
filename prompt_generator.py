import random

users = ["bastres"]
browsers = ["Microsoft Edge", "Google Chrome", "Mozilla Firefox"]
locations = ["Kyiv", "London", "New York", "Berlin", "Warsaw"]
messaging_apps = ["Microsoft Teams", "Discord", "Slack"]
storage = ["OneDrive", "Dropbox"]
sites = ["cnn.com", "weather.com", "linkedin.com", "sharepoint.com"]
# domains = ["company.com", "outlook.com", "zoom.us", "teams.microsoft.com"]
files = ["Document 5.pdf", "another_one.pdf"]

tasks = [
    lambda: f"Open {random.choice(messaging_apps)} and send a message to {random.choice(users)}.",
    # lambda: f"Send a work email to {random.choice(users)}@kiplingsecure.ai.",
    lambda: f"Open {random.choice(browsers)} and check the weather in {random.choice(locations)}.",
    # lambda: f"Use Outlook Web Access to check inbox and reply to recent messages.",
    lambda: f"Return the content of {random.choice(files)}",
    # lambda: f"Sync OneDrive files with cloud account.","
    lambda: f"Start a Zoom meeting, click on meeting information, then description, and return the meeting id and passcode." 
]

def generate_user_prompt():
    return random.choice(tasks)()