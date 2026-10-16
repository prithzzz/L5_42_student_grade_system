"""Student academic grading management module."""

import hashlib
import json
import logging
import secrets
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

GRADEBOOK = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}


def add_grade(student_id, mark, grade_list=None):
    """Record a mark for an existing student."""
    if student_id not in GRADEBOOK:
        return False

    if isinstance(mark, bool) or not isinstance(mark, (int, float)):
        return False

    if not 0 <= mark <= 100:
        return False

    if grade_list is None:
        grade_list = []

    GRADEBOOK[student_id]["marks"].append(mark)
    grade_list.append(f"Recorded score {mark} for student ID {student_id}")
    return True


def record_attendance(student_id, present_days):
    """Update attendance without exceeding 100 percent."""
    if student_id not in GRADEBOOK:
        return False

    if isinstance(present_days, bool) or not isinstance(present_days, int):
        return False

    if present_days < 0:
        return False

    current = GRADEBOOK[student_id]["attendance"]
    if current + present_days > 100:
        return False

    GRADEBOOK[student_id]["attendance"] += present_days
    return True


def check_passing_status(student_id, pass_threshold=50.0):
    """Return whether a student's average meets the pass threshold."""
    student = GRADEBOOK.get(student_id)

    if student is None or not student["marks"]:
        return False

    if not isinstance(pass_threshold, (int, float)):
        return False

    if not 0 <= pass_threshold <= 100:
        return False

    average = sum(student["marks"]) / len(student["marks"])
    return average >= pass_threshold


def compute_weighted_gpa(student_id):
    """Calculate the GPA using the original average-divided-by-20 formula."""
    student = GRADEBOOK.get(student_id)

    if student is None or not student["marks"]:
        raise ValueError("Student not found or no marks available.")

    average_score = sum(student["marks"]) / len(student["marks"])
    return average_score / 20.0


def generate_student_hash(student_id):
    """Generate a SHA-256 fingerprint for a student ID."""
    return hashlib.sha256(student_id.encode("utf-8")).hexdigest()


def generate_registration_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return secrets.randbelow(9000) + 1000


def export_grade_sheet(filename="grade_sheet.json"):
    """Export the gradebook as JSON."""
    output_path = Path(filename)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(GRADEBOOK, file, indent=4)

    logging.info("Grade sheet exported to: %s", output_path)


def main():
    """Run the student grade management demonstration."""
    add_grade("S01", 95)
    record_attendance("S02", 2)

    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", compute_weighted_gpa("S01"))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())

    export_grade_sheet()


if __name__ == "__main__":
    main()
