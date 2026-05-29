import random

# -------------------------------
# University Timetable Generator
# -------------------------------

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
slots = [
    "9:00-10:00",
    "10:00-11:00",
    "11:00-12:00",
    "1:00-2:00",
    "2:00-3:00"
]

subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Computer Science",
    "English"
]

teachers = {
    "Mathematics": "Dr. Rao",
    "Physics": "Dr. Sharma",
    "Chemistry": "Dr. Priya",
    "Computer Science": "Dr. Kiran",
    "English": "Dr. Meena"
}

rooms = ["Room-101", "Room-102", "Lab-1", "Lab-2"]

# Store timetable
timetable = {}

# Generate timetable
for day in days:
    timetable[day] = []

    used_subjects = []

    for slot in slots:
        available_subjects = [s for s in subjects if s not in used_subjects]

        if not available_subjects:
            used_subjects = []
            available_subjects = subjects

        subject = random.choice(available_subjects)
        teacher = teachers[subject]
        room = random.choice(rooms)

        timetable[day].append({
            "slot": slot,
            "subject": subject,
            "teacher": teacher,
            "room": room
        })

        used_subjects.append(subject)

# Display timetable
print("\n========== UNIVERSITY TIMETABLE ==========\n")

for day in days:
    print(f"\n------ {day} ------")

    for entry in timetable[day]:
        print(
            f"{entry['slot']}  |  "
            f"{entry['subject']}  |  "
            f"{entry['teacher']}  |  "
            f"{entry['room']}"
        )

print("\n==========================================")
