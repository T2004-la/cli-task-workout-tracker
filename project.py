import csv

from datetime import datetime

import sys

from tabulate import tabulate





def main():

    print("\n=== 🏋️  CLI Task & Workout Tracker  📖 ===")

    print("1. Log a new activity")

    print("2. View activity summary")

    print("3. Exit")



    choice = input("Select an option (1-3): ").strip()



    if choice == "1":

        task = input("Activity/Task name: ")

        duration_input = input("Duration in minutes: ")

        date_input = input("Date (YYYY-MM-DD) [Leave empty for today]: ")





        if not date_input.strip():

            date_input = datetime.today().strftime("%Y-%m-%d")



        if not validate_date(date_input):

            sys.exit("❌ Error: Invalid date format. Must be YYYY-MM-DD.")



        try:

            duration = parse_duration(duration_input)

        except ValueError as e:

            sys.exit(f"❌ Error: {e}")



        entry = format_log_entry(task, duration, date_input)





        save_to_csv("tracker.csv", entry)

        print("✅ Activity logged successfully!")



    elif choice == "2":

        summary = get_summary("tracker.csv")

        print("\n" + summary)



    elif choice == "3":

        sys.exit("Goodbye!")

    else:

        sys.exit("❌ Invalid option selected.")





def validate_date(date_str):


    try:

        datetime.strptime(date_str.strip(), "%Y-%m-%d")

        return True

    except ValueError:

        return False





def parse_duration(duration_str):


    try:

        val = int(duration_str.strip())

        if val <= 0:

            raise ValueError("Duration must be a positive integer.")

        return val

    except ValueError:

        raise ValueError("Duration must be a valid positive integer.")





def format_log_entry(task, duration, date_str):


    cleaned_task = task.strip().title()

    if not cleaned_task:

        cleaned_task = "Untitled Activity"



    return {

        "date": date_str.strip(),

        "task": cleaned_task,

        "duration_min": duration,

    }





def save_to_csv(filename, data_dict):


    fieldnames = ["date", "task", "duration_min"]

    file_exists = True

    try:

        with open(filename, "r"):

            pass

    except FileNotFoundError:

        file_exists = False



    with open(filename, "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:

            writer.writeheader()

        writer.writerow(data_dict)





def get_summary(filename):


    try:

        with open(filename, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            rows = list(reader)

            if not rows:

                return "No records found."

            return tabulate(rows, headers="keys", tablefmt="grid")

    except FileNotFoundError:

        return "No records found. Start by logging an activity!"





if __name__ == "__main__":

    main() 

