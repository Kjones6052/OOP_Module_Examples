import calorie_tracker as ct
import exercise_tracker as et

def main():
    while True:
        choice = input("Enter '1' to add food, '2' to log exercise, or '3' to show totals: ")
        if choice == "1":
            food = input("Enter food items: ")
            calories = int(input("Enter calories: "))
            ct.add_food_calories(food, calories)
        elif choice == "2":
            exercise = input("Enter exercise: ")
            duration = int(input("Enter duration in minutes: "))
            et.log_exercise(exercise, duration)
        elif choice == "3":
            print(f"Total Calories: {ct.get_total_calories()}")
            print(f"Total Exercise Time: {et.get_total_exercise_time} minutes.")
        else:
            break

if __name__ == "__main__":
    main()