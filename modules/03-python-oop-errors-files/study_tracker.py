"""Script version of the Module 03 mini-project: the study tracker.

It loads sample_log.csv from disk, refuses rows it cannot trust, prints a
report, saves a JSON summary, and fits a baseline model shaped exactly like a
scikit-learn one. Run it from a terminal -- from any folder, not just this one:

    python study_tracker.py

Module 01's study_report.py handled one learner with one loop, Module 02's
study_stats.py handled many learners with functions and containers, and this
handles a real file with objects. Module 03 adds the three things study_stats.py
did not have: persistence (a CSV in, a JSON out), validation (a named exception
for a row we refuse, instead of a crash), and objects (each piece of data
carrying the behaviour that belongs with it).
"""

import csv
import json
import statistics
from pathlib import Path

GOAL_MINUTES = 30
MAX_REASONABLE_MINUTES = 1440  # a day is 1440 minutes; more than that is a typo
REPORT_WIDTH = 52

# Every path starts from the folder holding THIS file, never from the folder you
# happen to be standing in when you launch Python. That one habit is why the
# script gives the same answer from the repo root as it does from here.
DATA_DIR = Path(__file__).parent
SANDBOX_DIR = DATA_DIR / "sandbox"
SAMPLE_LOG_PATH = DATA_DIR / "sample_log.csv"


# --------------------------------------------------------------------------
# Errors: one small family, so a caller can catch all of them or just one.
# --------------------------------------------------------------------------

class StudyLogError(Exception):
    """Base class for every failure this program raises on purpose."""


class InvalidEntryError(StudyLogError, ValueError):
    """A study row we refuse to accept.

    It inherits from ValueError as well, which is a kindness to callers: code
    that already says `except ValueError` keeps working, and code that knows
    this project can say `except InvalidEntryError` and be exact.
    """


class NotFittedError(StudyLogError):
    """Raised when a model is asked for an answer before fit() taught it one."""


# --------------------------------------------------------------------------
# Objects: data with the behaviour that belongs to it.
# --------------------------------------------------------------------------

class StudyEntry:
    """One study session: who studied, when, for how long, and on what.

    All the checking happens in __init__, which buys something valuable: an
    entry that exists is an entry every later line can trust without asking.
    """

    def __init__(self, name, date, minutes, topic):
        """Store one session, raising InvalidEntryError if it makes no sense."""
        clean_name = "" if name is None else str(name).strip()
        if clean_name == "":
            raise InvalidEntryError(f"name is blank or missing, got {name!r}")

        # bool is a subclass of int in Python, so True would otherwise pass as 1.
        if isinstance(minutes, bool) or not isinstance(minutes, int):
            raise InvalidEntryError(
                f"minutes must be a whole number, got {minutes!r}")
        if minutes < 0:
            raise InvalidEntryError(f"minutes cannot be negative, got {minutes!r}")
        if minutes > MAX_REASONABLE_MINUTES:
            raise InvalidEntryError(
                f"minutes above {MAX_REASONABLE_MINUTES} is not believable, "
                f"got {minutes!r}")

        self.name = clean_name
        self.date = "" if date is None else str(date).strip()
        self.minutes = minutes
        self.topic = "" if topic is None else str(topic).strip()

    def hours(self):
        """Return this session's length in hours."""
        return self.minutes / 60

    def met_goal(self, goal=GOAL_MINUTES):
        """Return True when this session reached the daily goal."""
        return self.minutes >= goal

    def __repr__(self):
        """What the terminal shows. Print every field, or debugging is guesswork."""
        return (f"StudyEntry(name={self.name!r}, date={self.date!r}, "
                f"minutes={self.minutes!r}, topic={self.topic!r})")


class StudyLog:
    """A collection of StudyEntry objects, plus the sums we ask of them.

    A log HAS a list; it is not a kind of list. That is composition, and it is
    the right choice here because a log does not want sort(), pop() and slicing
    handed to callers -- it wants add(), names() and summary().
    """

    def __init__(self, entries=None):
        """Start an empty log, or one already holding the given entries."""
        # The list is built here, once per log. A list written up in the class
        # body would be one list shared by every log ever made -- the aliasing
        # bug from Module 02, wearing a class.
        self.entries = []
        if entries is not None:
            for entry in entries:
                self.add(entry)

    def add(self, entry):
        """Append one StudyEntry, refusing anything that is not one."""
        if not isinstance(entry, StudyEntry):
            raise InvalidEntryError(
                f"a StudyLog holds StudyEntry objects, got {entry!r}")
        self.entries.append(entry)

    def names(self):
        """Return every learner name once, sorted."""
        return sorted({entry.name for entry in self.entries})

    def for_name(self, name):
        """Return one learner's entries, in the order they were added."""
        return [entry for entry in self.entries if entry.name == name]

    def total_minutes(self, name=None):
        """Return total minutes for one learner, or everybody when name is None."""
        chosen = self.entries if name is None else self.for_name(name)
        return sum(entry.minutes for entry in chosen)

    def summary(self):
        """Return {name: {sessions, total, average, best, days_at_goal}}."""
        report = {}
        for name in self.names():
            sessions = self.for_name(name)
            minutes = [entry.minutes for entry in sessions]
            report[name] = {
                "sessions": len(sessions),
                "total": sum(minutes),
                "average": sum(minutes) / len(minutes),
                "best": max(minutes),
                # One object asking another object its own question, rather
                # than reaching in for .minutes and comparing out here.
                "days_at_goal": len([e for e in sessions if e.met_goal()]),
            }
        return report

    def __len__(self):
        """Let len(log) work: Python calls this method for the len() builtin."""
        return len(self.entries)

    def __repr__(self):
        """A one-line shape summary -- enough to tell two logs apart."""
        return f"StudyLog({len(self.entries)} entries, {len(self.names())} learners)"


class MeanMinutesModel:
    """A baseline that predicts one number: the typical minutes of a session.

    This is the shape of every model in the rest of the course. __init__ stores
    the choices you made, fit stores what the data taught (mean_, with the
    trailing underscore that says "learned, not chosen"), and fit returns self
    so that Model().fit(entries).predict() is one legal line.
    """

    def __init__(self, strategy="mean"):
        """Store the hyperparameter. Nothing has been learned yet."""
        self.strategy = strategy
        # mean_ is deliberately not created here. Until fit runs there is no
        # honest answer to give, which is what lets predict() say so.

    def fit(self, entries):
        """Learn mean_ from entries, then return self so calls can be chained."""
        minutes = [entry.minutes for entry in entries]
        if not minutes:
            raise InvalidEntryError("cannot fit on zero entries")

        if self.strategy == "mean":
            self.mean_ = sum(minutes) / len(minutes)
        elif self.strategy == "median":
            self.mean_ = statistics.median(minutes)
        else:
            raise StudyLogError(
                f"unknown strategy {self.strategy!r}; use 'mean' or 'median'")
        return self

    def predict(self):
        """Return the predicted minutes for any session. fit() must have run."""
        self._require_fitted("predict()")
        return self.mean_

    def score(self, entries):
        """Return the mean absolute error over entries. Lower is better."""
        self._require_fitted("score()")
        minutes = [entry.minutes for entry in entries]
        if not minutes:
            raise InvalidEntryError("cannot score on zero entries")
        return sum(abs(m - self.mean_) for m in minutes) / len(minutes)

    def _require_fitted(self, what):
        """Raise NotFittedError if fit() has not run. A leading _ means internal."""
        if not hasattr(self, "mean_"):
            raise NotFittedError(f"call fit(entries) before {what}")

    def __repr__(self):
        """Show the choices only, exactly as scikit-learn's own models do."""
        return f"MeanMinutesModel(strategy={self.strategy!r})"


# --------------------------------------------------------------------------
# Calculations: pure functions. No printing, no files, nothing changed.
# --------------------------------------------------------------------------

def parse_minutes(text):
    """Return text converted to a whole number of minutes.

    Everything a CSV gives you is a string, so the conversion has to happen
    somewhere. Doing it here means a bad field becomes InvalidEntryError -- the
    one exception the loader knows how to skip.
    """
    try:
        return int(str(text).strip())
    except (TypeError, ValueError) as error:
        # `from error` keeps the original ValueError attached as the cause, so
        # the traceback shows both what we refused and why int() gave up.
        raise InvalidEntryError(
            f"minutes must be a whole number, got {text!r}") from error


def class_totals(log):
    """Return (learner_count, total_minutes, sessions_at_goal) for a whole log."""
    summary = log.summary()
    return (
        len(summary),
        sum(figures["total"] for figures in summary.values()),
        sum(figures["days_at_goal"] for figures in summary.values()),
    )


# --------------------------------------------------------------------------
# Side effects: reading files, writing files, printing. Kept apart from above.
# --------------------------------------------------------------------------

def load_log(path):
    """Read a CSV of study sessions and return a StudyLog.

    A bad row is reported by its line number and skipped, so one typo cannot
    cost you the other seven rows. A missing file is still fatal, but the
    message names the full path that was actually searched.
    """
    csv_path = Path(path)
    log = StudyLog()
    try:
        # newline="" hands line-ending handling to the csv module, the only
        # thing here that knows a quoted field may legally contain a newline.
        with open(csv_path, "r", encoding="utf-8", newline="") as source:
            reader = csv.DictReader(source)
            # start=2: line 1 of the file is the header, so these numbers match
            # the line numbers an editor shows the learner.
            for line_number, row in enumerate(reader, start=2):
                try:
                    entry = StudyEntry(
                        row.get("name"),
                        row.get("date"),
                        parse_minutes(row.get("minutes")),
                        row.get("topic"),
                    )
                except InvalidEntryError as error:
                    print(f"skipping row {line_number}: {error}")
                    continue
                log.add(entry)
    except FileNotFoundError as error:
        # Re-raise with the resolved path, because "sample_log.csv not found"
        # never tells you WHERE Python looked. `from error` keeps the original.
        raise FileNotFoundError(f"no study log at {csv_path.resolve()}") from error
    return log


def save_summary(log, path):
    """Write log.summary() to path as indented JSON and return the Path used."""
    json_path = Path(path)
    # The folder may not exist on a fresh clone, and writing does not create it.
    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as target:
        json.dump(log.summary(), target, indent=2, sort_keys=True)
    return json_path


def print_report(log, goal=GOAL_MINUTES):
    """Display the log as a table. This is the only function here that prints."""
    print("STUDY TRACKER")
    print("=" * REPORT_WIDTH)
    if len(log) == 0:
        print("No usable entries in the log yet.")
        return

    summary = log.summary()
    ranked = sorted(summary, key=lambda name: summary[name]["total"], reverse=True)
    for name in ranked:
        figures = summary[name]
        print(f"{name:<6}{figures['sessions']:>3} sessions "
              f"{figures['total']:>5} min  avg {figures['average']:>5.1f}  "
              f"best {figures['best']:>3}  {figures['days_at_goal']} at goal")

    print("-" * REPORT_WIDTH)
    learners, minutes, at_goal = class_totals(log)
    print(f"{learners} learners, {minutes} minutes, "
          f"{at_goal} sessions at the {goal}-minute goal")


def main():
    """Run the whole tracker once: load, reject, save, fit, explain."""
    log = load_log(SAMPLE_LOG_PATH)
    print_report(log)
    print(f"Loaded {len(log)} entries from {SAMPLE_LOG_PATH.name}")

    print()
    print("Refusing one bad row on purpose (Part 3):")
    try:
        StudyEntry("maya", "2026-03-06", -5, "files")
    except InvalidEntryError as error:
        print(f"  rejected: {error}")
    print("  the object was never created, so no later line has to check for it.")

    print()
    print("Saving a JSON summary (Part 5):")
    summary_path = save_summary(log, SANDBOX_DIR / "summary.json")
    with open(summary_path, "r", encoding="utf-8") as saved:
        reloaded = json.load(saved)
    print(f"  wrote {summary_path.relative_to(DATA_DIR)}")
    print(f"  read it back: ravi's average is {reloaded['ravi']['average']}")

    print()
    print("Fitting the baseline model (Part 7):")
    model = MeanMinutesModel()
    print(f"  fit returned the same object: {model.fit(log.entries) is model}")
    print(f"  strategy = {model.strategy!r}  <- a hyperparameter: you chose it")
    print(f"  mean_    = {model.mean_}   <- a fitted attribute: the data taught it")
    print(f"  predict() = {model.predict()} minutes, for any session")
    print(f"  score()   = {model.score(log.entries)} minutes of average error")
    try:
        MeanMinutesModel().predict()
    except NotFittedError as error:
        print(f"  a fresh model, asked too early: {type(error).__name__}: {error}")
    print("  raising beats returning None: the message says what to do next.")


# Runs only when this file is executed directly. Importing it defines the names
# and prints nothing, which is exactly what Part 8 means by __name__.
if __name__ == "__main__":
    main()
