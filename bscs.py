# Define a dictionary of subjects for each year level and semester
subjects = {
    "1st year": {
        "1st sem": [
            "CS 101: Introduction to Programming",
            "CS 102: Discrete Mathematics",
            "CS 103: Data Structures and Algorithms",
        ],
        "2nd sem": [
            "CS 104: Object-Oriented Programming",
            "CS 105: Linear Algebra",
            "CS 106: Computer Organization and Architecture",
        ],
    },
    "2nd year": {
        "1st sem": [
            "CS 201: Software Engineering",
            "CS 202: Database Systems",
            "CS 203: Operating Systems",
        ],
        "2nd sem": [
            "CS 204: Web Development",
            "CS 205: Artificial Intelligence",
            "CS 206: Theory of Computation",
        ],
    },
    "3rd year": {
        "1st sem": [
            "CS 301: Computer Networks",
            "CS 302: Machine Learning",
            "CS 303: Compiler Design",
        ],
        "2nd sem": [
            "CS 304: Mobile Development",
            "CS 305: Computer Graphics",
            "CS 306: Cryptography",
        ],
    },
    "4th year": {
        "1st sem": [
            "CS 401: Distributed Systems",
            "CS 402: Natural Language Processing",
            "CS 403: Data Mining",
        ],
        "2nd sem": [
            "CS 404: Cloud Computing",
            "CS 405: Cybersecurity",
            "CS 406: Capstone Project",
        ],
    },
}

# Prompt the user for input
name = input("Enter your name: ")
year = input("Enter your year level (e.g. 1st year, 2nd year, etc.): ")
sem = input("Enter your semester (e.g. 1st sem, 2nd sem): ")

# Validate the input
if year not in subjects:
    print("Invalid year level.")
elif sem not in subjects[year]:
    print("Invalid semester.")
else:
    # Print the output
    print(f"Hello, {name}. You are a {year} CS student in the {sem}.")
    print(f"Here are the subjects you need to enroll:")
    for subject in subjects[year][sem]:
        print(f"- {subject}")
