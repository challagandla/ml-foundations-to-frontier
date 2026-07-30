# Beginner-friendly script version of the Module 01 mini-project.

print("STUDY SESSION REPORT")
print("=" * 24)

learner_name = input("Learner name: ").strip()
if learner_name == "":
    learner_name = "Learner"

planned_days = int(input("Number of study days: "))

if planned_days <= 0:
    print("The number of study days must be greater than zero.")
else:
    total_minutes = 0
    days_at_goal = 0
    daily_goal = 30

    for day in range(1, planned_days + 1):
        minutes_today = int(input(f"Minutes studied on day {day}: "))

        while minutes_today < 0:
            print("Minutes cannot be negative. Try again.")
            minutes_today = int(input(f"Minutes studied on day {day}: "))

        total_minutes += minutes_today

        if minutes_today >= daily_goal:
            days_at_goal += 1

    average_minutes = total_minutes / planned_days

    if average_minutes >= 45:
        habit = "strong"
    elif average_minutes >= 20:
        habit = "building"
    else:
        habit = "start small"

    print()
    print(f"{learner_name}'s study report")
    print("-" * 24)
    print(f"Days studied: {planned_days}")
    print(f"Total: {total_minutes} minutes")
    print(f"Hours: {total_minutes / 60:.2f}")
    print(f"Daily average: {average_minutes:.1f} minutes")
    print(f"Days meeting the {daily_goal}-minute goal: {days_at_goal}")
    print(f"Habit: {habit}")
