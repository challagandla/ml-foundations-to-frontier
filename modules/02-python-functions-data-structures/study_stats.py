"""Script version of the Module 02 mini-project: the study-log analyzer.

Every calculation below is a small pure function: it reads its arguments and
returns a value. Only print_report() and collect_log() touch the outside world.
Run it from a terminal inside this folder:

    python study_stats.py

Module 01's study_report.py handled one learner with one loop. This handles
many learners with functions and containers -- the whole point of Module 02.
"""

DEFAULT_GOAL = 30
REPORT_WIDTH = 46


# --------------------------------------------------------------------------
# Calculations: pure functions. No printing, no input, no globals changed.
# --------------------------------------------------------------------------

def average_minutes(minutes):
    """Return the mean of a list of daily minutes, or 0.0 for an empty list."""
    if not minutes:
        return 0.0
    return sum(minutes) / len(minutes)


def classify(average):
    """Return 'strong', 'building', or 'start small' for an average."""
    if average >= 45:
        return "strong"
    if average >= 20:
        return "building"
    return "start small"


def days_at_goal(minutes, goal=DEFAULT_GOAL):
    """Return how many days met or exceeded the goal."""
    return len([m for m in minutes if m >= goal])


def best_day(minutes):
    """Return the largest single day's minutes, or 0 for an empty list."""
    if not minutes:
        return 0
    return max(minutes)


def summarize(minutes, goal=DEFAULT_GOAL):
    """Return one learner's figures as a dict."""
    average = average_minutes(minutes)
    return {
        "days": len(minutes),
        "total": sum(minutes),
        "average": average,
        "habit": classify(average),
        "at_goal": days_at_goal(minutes, goal),
        "best": best_day(minutes),
    }


def build_report(log, goal=DEFAULT_GOAL):
    """Return {name: summary} for every learner in the log."""
    return {name: summarize(minutes, goal) for name, minutes in log.items()}


def top_learner(report):
    """Return (name, total_minutes) for the learner with the most minutes.

    Returns ("nobody", 0) for an empty report, so callers never crash.
    """
    if not report:
        return "nobody", 0
    best_name = max(report, key=lambda name: report[name]["total"])
    return best_name, report[best_name]["total"]


def needs_encouragement(report):
    """Return the set of names whose habit is 'start small'."""
    return {name for name, summary in report.items() if summary["habit"] == "start small"}


# --------------------------------------------------------------------------
# Side effects: displaying and collecting. Kept apart from the calculations.
# --------------------------------------------------------------------------

def print_report(report, goal=DEFAULT_GOAL):
    """Display the report. This is the only function here that prints."""
    print()
    print("STUDY LOG REPORT")
    print("=" * REPORT_WIDTH)

    if not report:
        print("No learners in the log yet.")
        return

    ranked = sorted(report, key=lambda name: report[name]["total"], reverse=True)
    for name in ranked:
        s = report[name]
        print(f"{name:<8}{s['days']:>3} days  {s['total']:>4} min  "
              f"avg {s['average']:>5.1f}  {s['habit']}")

    print("-" * REPORT_WIDTH)
    best_name, best_total = top_learner(report)
    print(f"Top learner: {best_name} with {best_total} minutes")
    total_all = sum(s["total"] for s in report.values())
    print(f"Class total: {total_all} minutes across {len(report)} learners")
    print(f"Days meeting the {goal}-minute goal: "
          f"{sum(s['at_goal'] for s in report.values())}")

    encourage = needs_encouragement(report)
    if encourage:
        print(f"Check in with: {', '.join(sorted(encourage))}")


def ask_whole_number(prompt, minimum=0):
    """Ask until the answer is a whole number of at least `minimum`."""
    while True:
        answer = input(prompt).strip()
        if answer.lstrip("-").isdigit() and int(answer) >= minimum:
            return int(answer)
        print(f"Please type a whole number of {minimum} or more.")


def collect_log():
    """Ask the user for learners and their daily minutes; return the log dict."""
    log = {}
    learner_count = ask_whole_number("How many learners? ", minimum=1)

    for _ in range(learner_count):
        name = input("Learner name: ").strip()
        if name == "":
            name = f"learner{len(log) + 1}"

        day_count = ask_whole_number(f"How many days for {name}? ", minimum=0)
        minutes = []
        for day in range(1, day_count + 1):
            minutes.append(ask_whole_number(f"  Minutes on day {day}: ", minimum=0))

        log[name] = minutes

    return log


SAMPLE_LOG = {
    "maya": [30, 45, 20, 60],
    "sam": [60, 60],
    "ren": [10, 15, 5],
}


def main():
    """Show the sample report, then optionally build one from user input."""
    print("Sample log built into this script:")
    print_report(build_report(SAMPLE_LOG))

    print()
    answer = input("Enter your own learners instead? (y/n) ").strip().lower()
    if answer.startswith("y"):
        print_report(build_report(collect_log()))
    else:
        print("Keeping the sample. Edit SAMPLE_LOG in this file and run it again.")


# Runs only when this file is executed directly, not when it is imported.
# Module 03 covers importing; for now, read it as "start here".
if __name__ == "__main__":
    main()
