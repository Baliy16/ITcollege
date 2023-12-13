from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("1 task\README.md", "a") as readme_file:
    readme_file.write(f"\n\n VII: {current_date}\n")
