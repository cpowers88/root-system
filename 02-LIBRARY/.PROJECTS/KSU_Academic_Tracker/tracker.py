import argparse
from email import parser
import sqlite3
from datetime import date, timedelta


DB_NAME = "academic.db"


def connect_db():
    """Connect to the SQLite database file."""
    return sqlite3.connect(DB_NAME)


def create_tables(connection):
    """Create the four tracker tables if they do not already exist."""
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            code TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            professor TEXT,
            credit_hours INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            assignment_id INTEGER PRIMARY KEY,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL,
            grade REAL,
            notes_file TEXT,
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tests (
            test_id INTEGER PRIMARY KEY,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            test_date TEXT NOT NULL,
            chapters_covered TEXT,
            study_status TEXT,
            notes_file TEXT,
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            reading_id INTEGER PRIMARY KEY,
            course_id INTEGER NOT NULL,
            chapter TEXT NOT NULL,
            pages TEXT,
            due_date TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            notes_file TEXT,
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    """)

    connection.commit()


def seed_courses(connection):
    """Enter the five Fall 2026 courses once."""
    cursor = connection.cursor()

    courses = [
        ("PHYS2211", "Physics I", "", 4),
        ("CSE1321", "Python + Lab", "", 4),
        ("ECON1000", "Engineering Contemporary Economic Issues", "", 3),
        ("TCOM2010", "Technical Writing", "", 3),
        ("ENGR1000", "Intro to Engineering", "", 1),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO courses (code, name, professor, credit_hours)
        VALUES (?, ?, ?, ?)
    """, courses)

    connection.commit()


def show_week(connection):
    """Show assignments/readings/tests due in the next 7 days."""
    cursor = connection.cursor()

    today = date.today()
    week_end = today + timedelta(days=7)

    print(f"\nKSU Tracker — Next 7 Days")
    print(f"{today} through {week_end}")
    print("-" * 50)

    # Assignments
    cursor.execute("""
        SELECT courses.code, assignments.name, assignments.due_date, assignments.status, assignments.notes_file
        FROM assignments
        JOIN courses ON assignments.course_id = courses.course_id
        WHERE assignments.due_date BETWEEN ? AND ?
        ORDER BY assignments.due_date
    """, (today.isoformat(), week_end.isoformat()))

    assignments = cursor.fetchall()

    print("\nAssignments:")
    if assignments:
        for course, name, due_date, status, notes_file in assignments:
            print(f"- {due_date} | {course} | {name} | {status} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    # Readings
    cursor.execute("""
        SELECT courses.code, readings.chapter, readings.pages, readings.due_date, readings.completed, readings.notes_file
        FROM readings
        JOIN courses ON readings.course_id = courses.course_id
        WHERE readings.due_date BETWEEN ? AND ?
        ORDER BY readings.due_date
    """, (today.isoformat(), week_end.isoformat()))

    readings = cursor.fetchall()

    print("\nReadings:")
    if readings:
        for course, chapter, pages, due_date, completed, notes_file in readings:
            status = "complete" if completed else "not complete"
            print(f"- {due_date} | {course} | {chapter} | pages {pages or 'n/a'} | {status} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    # Tests
    cursor.execute("""
        SELECT courses.code, tests.name, tests.test_date, tests.chapters_covered, tests.study_status, tests.notes_file
        FROM tests
        JOIN courses ON tests.course_id = courses.course_id
        WHERE tests.test_date BETWEEN ? AND ?
        ORDER BY tests.test_date
    """, (today.isoformat(), week_end.isoformat()))

    tests = cursor.fetchall()

    print("\nTests:")
    if tests:
        for course, name, test_date, chapters, study_status, notes_file in tests:
            print(f"- {test_date} | {course} | {name} | {chapters or 'chapters TBD'} | {study_status or 'not started'} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    print()

def show_courses(connection):
    """Show all courses stored in the tracker."""
    cursor = connection.cursor()

    cursor.execute("""
        SELECT code, name, professor, credit_hours
        FROM courses
        ORDER BY code
    """)

    courses = cursor.fetchall()

    print("\nKSU Courses")
    print("-" * 50)

    if courses:
        for code, name, professor, credit_hours in courses:
            professor_display = professor if professor else "professor TBD"
            print(f"- {code} | {name} | {credit_hours} credits | {professor_display}")
    else:
        print("- No courses found")

    print()

def show_tests(connection):
    """Show all upcoming tests with study status and notes path."""
    cursor = connection.cursor()

    today = date.today().isoformat()

    cursor.execute("""
        SELECT courses.code, tests.name, tests.test_date,
               tests.chapters_covered, tests.study_status, tests.notes_file
        FROM tests
        JOIN courses ON tests.course_id = courses.course_id
        WHERE tests.test_date >= ?
        ORDER BY tests.test_date
    """, (today,))

    tests = cursor.fetchall()

    print("\nUpcoming Tests")
    print("-" * 50)

    if tests:
        for course, name, test_date, chapters, study_status, notes_file in tests:
            print(
                f"- {test_date} | {course} | {name} | "
                f"{chapters or 'chapters TBD'} | "
                f"{study_status or 'not started'} | "
                f"{notes_file or 'no notes file'}"
            )
    else:
        print("- None")

    print()

def show_today(connection):
    """Show assignments, readings, and tests due today."""
    cursor = connection.cursor()

    today = date.today().isoformat()

    print(f"\nKSU Tracker — Today: {today}")
    print("-" * 50)

    # Assignments due today
    cursor.execute("""
        SELECT courses.code, assignments.name, assignments.status, assignments.notes_file
        FROM assignments
        JOIN courses ON assignments.course_id = courses.course_id
        WHERE assignments.due_date = ?
        ORDER BY courses.code
    """, (today,))

    assignments = cursor.fetchall()

    print("\nAssignments:")
    if assignments:
        for course, name, status, notes_file in assignments:
            print(f"- {course} | {name} | {status} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    # Readings due today
    cursor.execute("""
        SELECT courses.code, readings.chapter, readings.pages, readings.completed, readings.notes_file
        FROM readings
        JOIN courses ON readings.course_id = courses.course_id
        WHERE readings.due_date = ?
        ORDER BY courses.code
    """, (today,))

    readings = cursor.fetchall()

    print("\nReadings:")
    if readings:
        for course, chapter, pages, completed, notes_file in readings:
            status = "complete" if completed else "not complete"
            print(f"- {course} | {chapter} | pages {pages or 'n/a'} | {status} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    # Tests today
    cursor.execute("""
        SELECT courses.code, tests.name, tests.chapters_covered, tests.study_status, tests.notes_file
        FROM tests
        JOIN courses ON tests.course_id = courses.course_id
        WHERE tests.test_date = ?
        ORDER BY courses.code
    """, (today,))

    tests = cursor.fetchall()

    print("\nTests:")
    if tests:
        for course, name, chapters, study_status, notes_file in tests:
            print(f"- {course} | {name} | {chapters or 'chapters TBD'} | {study_status or 'not started'} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    print()

def show_course(connection, course_code):
    """Show assignments, readings, and tests for one course."""
    cursor = connection.cursor()

    course_code = course_code.upper()

    cursor.execute("""
        SELECT course_id, code, name
        FROM courses
        WHERE code = ?
    """, (course_code,))

    course = cursor.fetchone()

    if course is None:
        print(f"\nCourse not found: {course_code}")
        print("Try one of: PHYS2211, CSE1321, ECON1000, TCOM2010, ENGR1000\n")
        return

    course_id, code, course_name = course

    print(f"\n{code} — {course_name}")
    print("-" * 50)

    # Assignments
    cursor.execute("""
        SELECT name, due_date, status, grade, notes_file
        FROM assignments
        WHERE course_id = ?
        ORDER BY due_date
    """, (course_id,))

    assignments = cursor.fetchall()

    print("\nAssignments:")
    if assignments:
        for name, due_date, status, grade, notes_file in assignments:
            grade_display = grade if grade is not None else "no grade"
            print(f"- {due_date} | {name} | {status} | {grade_display} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    # Readings
    cursor.execute("""
        SELECT chapter, pages, due_date, completed, notes_file
        FROM readings
        WHERE course_id = ?
        ORDER BY due_date
    """, (course_id,))

    readings = cursor.fetchall()

    print("\nReadings:")
    if readings:
        for chapter, pages, due_date, completed, notes_file in readings:
            status = "complete" if completed else "not complete"
            print(f"- {due_date} | {chapter} | pages {pages or 'n/a'} | {status} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    # Tests
    cursor.execute("""
        SELECT tests.name, tests.test_date, tests.chapters_covered,
               tests.study_status, tests.notes_file
        FROM tests
        JOIN courses ON tests.course_id = courses.course_id
        WHERE courses.code = ?
        ORDER BY tests.test_date
    """, (course_code,))

    tests = cursor.fetchall()

    print("\nTests:")
    if tests:
        for name, test_date, chapters, study_status, notes_file in tests:
            print(f"- {test_date} | {name} | {chapters or 'chapters TBD'} | {study_status or 'not started'} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    print()

def show_overdue(connection):
    """Show assignments and readings that are past due and unfinished."""
    cursor = connection.cursor()

    today = date.today().isoformat()

    print(f"\nKSU Tracker — Overdue Items before {today}")
    print("-" * 50)

    # Overdue assignments
    cursor.execute("""
        SELECT courses.code, assignments.name, assignments.due_date,
               assignments.status, assignments.notes_file
        FROM assignments
        JOIN courses ON assignments.course_id = courses.course_id
        WHERE assignments.due_date < ?
          AND assignments.status != 'submitted'
          AND assignments.status != 'graded'
        ORDER BY assignments.due_date
    """, (today,))

    assignments = cursor.fetchall()

    print("\nAssignments:")
    if assignments:
        for course, name, due_date, status, notes_file in assignments:
            print(f"- {due_date} | {course} | {name} | {status} | {notes_file or 'no notes file'}")
    else:
        print("- None")

    # Overdue readings
    cursor.execute("""
        SELECT courses.code, readings.chapter, readings.pages,
               readings.due_date, readings.completed, readings.notes_file
        FROM readings
        JOIN courses ON readings.course_id = courses.course_id
        WHERE readings.due_date < ?
          AND readings.completed = 0
        ORDER BY readings.due_date
    """, (today,))

    readings = cursor.fetchall()

    print("\nReadings:")
    if readings:
        for course, chapter, pages, due_date, completed, notes_file in readings:
            print(f"- {due_date} | {course} | {chapter} | pages {pages or 'n/a'} | not complete | {notes_file or 'no notes file'}")
    else:
        print("- None")

    print()

def get_course_id(connection, course_code):
    """Return the course_id for a course code, or None if not found."""
    cursor = connection.cursor()
    course_code = course_code.upper()

    cursor.execute("""
        SELECT course_id
        FROM courses
        WHERE code = ?
    """, (course_code,))

    row = cursor.fetchone()
    return row[0] if row else None

def add_test(connection):
    """Interactively add a test."""
    cursor = connection.cursor()

    print("\nAdd Test")
    print("-" * 50)

    course_code = input("Course code, example PHYS2211: ").strip().upper()
    course_id = get_course_id(connection, course_code)

    if course_id is None:
        print(f"Course not found: {course_code}")
        return

    name = input("Test name, example Exam 1: ").strip()
    test_date = input("Test date YYYY-MM-DD: ").strip()
    chapters = input("Chapters covered, example CH 1-3: ").strip()
    study_status = input("Study status, example not started / in progress / ready: ").strip()
    notes_file = input("Notes file path, or leave blank: ").strip()

    cursor.execute("""
        INSERT INTO tests (
            course_id,
            name,
            test_date,
            chapters_covered,
            study_status,
            notes_file
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        course_id,
        name,
        test_date,
        chapters,
        study_status,
        notes_file
    ))

    connection.commit()
    print("Test added.\n")

def add_assignment(connection):
    """Interactively add an assignment."""
    cursor = connection.cursor()

    print("\nAdd Assignment")
    print("-" * 50)

    course_code = input("Course code, example TCOM2010: ").strip().upper()
    course_id = get_course_id(connection, course_code)

    if course_id is None:
        print(f"Course not found: {course_code}")
        return

    name = input("Assignment name: ").strip()
    due_date = input("Due date YYYY-MM-DD: ").strip()
    status = input("Status, example pending / submitted / graded: ").strip()
    notes_file = input("Notes file path, or leave blank: ").strip()

    cursor.execute("""
        INSERT INTO assignments (
            course_id,
            name,
            due_date,
            status,
            grade,
            notes_file
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        course_id,
        name,
        due_date,
        status,
        None,
        notes_file
    ))

    connection.commit()
    print("Assignment added.\n")

def add_reading(connection):
    """Interactively add a reading."""
    cursor = connection.cursor()

    print("\nAdd Reading")
    print("-" * 50)

    course_code = input("Course code, example PHYS2211: ").strip().upper()
    course_id = get_course_id(connection, course_code)

    if course_id is None:
        print(f"Course not found: {course_code}")
        return

    chapter = input("Chapter, example CH 1: ").strip()
    pages = input("Pages, example 1-25: ").strip()
    due_date = input("Due date YYYY-MM-DD: ").strip()
    completed_input = input("Completed? y/n: ").strip().lower()
    completed = 1 if completed_input == "y" else 0
    notes_file = input("Notes file path, or leave blank: ").strip()

    cursor.execute("""
        INSERT INTO readings (
            course_id,
            chapter,
            pages,
            due_date,
            completed,
            notes_file
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        course_id,
        chapter,
        pages,
        due_date,
        completed,
        notes_file
    ))

    connection.commit()
    print("Reading added.\n")

def main():
    parser = argparse.ArgumentParser(description="KSU Academic Tracker")
    parser.add_argument("--week", action="store_true", help="Show everything due in the next 7 days")
    parser.add_argument("--courses", action="store_true", help="Show all courses")
    parser.add_argument("--tests", action="store_true", help="Show all upcoming tests")
    parser.add_argument("--today", action="store_true", help="Show everything due today")
    parser.add_argument("--overdue", action="store_true", help="Show overdue unfinished work")
    parser.add_argument("--course", type=str, help="Show everything for one course code")
    parser.add_argument("--add-test", action="store_true", help="Add a test interactively")
    parser.add_argument("--add-assignment", action="store_true", help="Add an assignment interactively")
    parser.add_argument("--add-reading", action="store_true", help="Add a reading interactively")

    args = parser.parse_args()

    connection = connect_db()
    create_tables(connection)
    seed_courses(connection)

    if args.week:
        show_week(connection)
    elif args.courses:
        show_courses(connection)
    elif args.tests:
        show_tests(connection)
    elif args.today:
        show_today(connection)
    elif args.course:
        show_course(connection, args.course)
    elif args.overdue:
        show_overdue(connection)
    elif args.add_test:
        add_test(connection)
    elif args.add_assignment:
        add_assignment(connection)
    elif args.add_reading:
        add_reading(connection)
    else:
        print("KSU Academic Tracker is set up.")
        print("Try: python tracker.py --week")
        print("Try: python tracker.py --courses")
        print("Try: python tracker.py --tests")
        print("Try: python tracker.py --today")
        print("Try: python tracker.py --course PHYS2211")
        print("Try: python tracker.py --overdue")
        print("Try: python tracker.py --add-test")
        print("Try: python tracker.py --add-assignment")
        print("Try: python tracker.py --add-reading")
        
    connection.close()

if __name__ == "__main__":
    main()