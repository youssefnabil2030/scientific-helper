import csv
import random
import time

# Function to load experiments from a CSV file
def load_experiments(filename):
    experiments = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            experiments.append({
                "name": row["name"],
                "materials": row["materials"].split(","),
                "instructions": row["instructions"].split(";")
            })
    return experiments

# Function to get a random experiment
def get_random_experiment(experiments):
    return random.choice(experiments)

# Function to list materials for an experiment
def list_materials(experiment):
    return experiment["materials"]

# Function to display instructions for an experiment
def display_instructions(experiment):
    for step in experiment["instructions"]:
        print(step)

# Function to start a timer for timed steps
def start_timer(duration):
    print(f"Timer started for {duration} seconds.")
    time.sleep(duration)
    print("Time's up!")

# Function to save a favorite experiment
def save_favorite(experiment, filename="favorites.txt"):
    with open(filename, "a") as file:
        file.write(f"{experiment['name']}\n")

# Function to load favorite experiments
def load_favorites(filename="favorites.txt"):
    favorites = []
    with open(filename, "r") as file:
        favorites = [line.strip() for line in file]
    return favorites

# Main function to run the program
def main():
    experiments = load_experiments("experiments.csv")
    print("Welcome to the Science Experiment Helper!")

    while True:
        print("\nOptions:")
        print("1. Get a random experiment")
        print("2. List materials for an experiment")
        print("3. Display instructions for an experiment")
        print("4. Start a timer")
        print("5. Save a favorite experiment")
        print("6. View favorite experiments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            experiment = get_random_experiment(experiments)
            print(f"Experiment: {experiment['name']}")
        elif choice == "2":
            name = input("Enter the experiment name: ")
            experiment = next((e for e in experiments if e["name"] == name), None)
            if experiment:
                print("Materials:", ", ".join(list_materials(experiment)))
            else:
                print("Experiment not found.")
        elif choice == "3":
            name = input("Enter the experiment name: ")
            experiment = next((e for e in experiments if e["name"] == name), None)
            if experiment:
                display_instructions(experiment)
            else:
                print("Experiment not found.")
        elif choice == "4":
            duration = int(input("Enter timer duration in seconds: "))
            start_timer(duration)
        elif choice == "5":
            name = input("Enter the experiment name to save as favorite: ")
            experiment = next((e for e in experiments if e["name"] == name), None)
            if experiment:
                save_favorite(experiment)
                print("Experiment saved as favorite.")
            else:
                print("Experiment not found.")
        elif choice == "6":
            favorites = load_favorites()
            print("Favorite Experiments:")
            for fav in favorites:
                print(fav)
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
