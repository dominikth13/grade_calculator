#!/usr/bin/env python3
"""
Grade Calculator
Contains functions for calculating letter grades and grade statistics.
"""

def get_letter_grade(percentage):
    """
    Convert a percentage grade to a letter grade.
    
    Args:
        percentage (float): The percentage grade (0-100)
        
    Returns:
        str: The corresponding letter grade
    """
    if percentage >= 97:
        return "A+"
    elif percentage >= 93:
        return "A"
    elif percentage >= 90:
        return "A-"
    elif percentage >= 87:
        return "B+"
    elif percentage >= 83:
        return "B"
    elif percentage >= 80:
        return "B-"
    elif percentage >= 77:
        return "C+"
    elif percentage >= 73:
        return "C"
    elif percentage >= 70:
        return "C-"
    elif percentage >= 67:
        return "D+"
    elif percentage >= 63:
        return "D"
    elif percentage >= 60:
        return "D-"
    else:
        return "F"

def get_gpa_points(letter_grade):
    """
    Convert a letter grade to GPA points.
    
    Args:
        letter_grade (str): The letter grade
        
    Returns:
        float: The GPA points for the grade
    """
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }
    
    return grade_points.get(letter_grade, 0.0)

def calculate_class_gpa(students):
    """
    Calculate the overall class GPA.
    
    Args:
        students (list): List of student dictionaries with letter grades
        
    Returns:
        float: The class GPA
    """
    if not students:
        return 0.0
    
    total_points = 0.0
    for student in students:
        if 'letter_grade' in student:
            total_points += get_gpa_points(student['letter_grade'])
    
    return total_points / len(students)

def get_grade_distribution(students):
    """
    Calculate the distribution of letter grades.
    
    Args:
        students (list): List of student dictionaries with letter grades
        
    Returns:
        dict: Dictionary with letter grades as keys and counts as values
    """
    distribution = {}
    
    for student in students:
        if 'letter_grade' in student:
            grade = student['letter_grade']
            distribution[grade] = distribution.get(grade, 0) + 1
    
    return distribution

def is_passing_grade(percentage):
    """
    Determine if a percentage grade is passing (>= 60%).
    
    Args:
        percentage (float): The percentage grade
        
    Returns:
        bool: True if passing, False otherwise
    """
    return percentage >= 60.0

def calculate_needed_score(current_avg, target_avg, remaining_weight):
    """
    Calculate what score is needed on remaining assignments to reach target average.
    
    Args:
        current_avg (float): Current average
        target_avg (float): Target average
        remaining_weight (float): Weight of remaining assignments (0.0 to 1.0)
        
    Returns:
        float: Required score on remaining assignments
    """
    if remaining_weight == 0:
        return current_avg
    
    current_weight = 1.0 - remaining_weight
    needed_points = target_avg - (current_avg * current_weight)
    
    return needed_points / remaining_weight
