from datetime import datetime  # <-- ADDED

def log(message):  # <-- ADDED
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # <-- ADDED
    with open("app.log", "a") as file:  # <-- ADDED
        file.write(f"[{time}] {message}\n")  # <-- ADDED
