# percentage_calculator.py
"""
A simple grade percentage calculator
- Takes marks for 5 subjects
- Calculates overall percentage
"""

def calculate_percentage():
    print("\n--- Grade Percentage Calculator ---")
    
    subjects = {
        "English": None,
        "Physics": None,
        "Chemistry": None,
        "Maths": None,
        "Information Practices": None
    }

    # Input with validation
    for subject in subjects:
        while True:
            try:
                marks = float(input(f"Enter marks for {subject}: "))
                if 0 <= marks <= 100:
                    subjects[subject] = marks
                    break
                else:
                    print("Error: Marks must be between 0-100")
            except ValueError:
                print("Invalid input! Please enter a number.")

    # Calculation
    total = sum(subjects.values())
    percentage = (total / len(subjects)) 
    print(f"\nYour percentage: {percentage:.2f}%")

if __name__ == "__main__":
    calculate_percentage()
