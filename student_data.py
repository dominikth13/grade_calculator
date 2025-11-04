#!/usr/bin/env python3
"""
Student Data Handler
Handles loading and parsing student grade data.
"""

import logging
import warnings
import os
import csv

logger = logging.getLogger(__name__)

def load_students():
    """
    Load student data from CSV file.
    Reads student grades from students.csv file in the current directory.
    """
    csv_file_path = "students.csv"
    
    if not os.path.exists(csv_file_path):
        error_msg = "CSV file not found: %s" % csv_file_path
        logger.error(error_msg)
        raise FileNotFoundError(error_msg)
    
    students = []
    
    try:
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                try:
                    name = row['name'].strip()
                    test1 = int(row['test1'])
                    test2 = int(row['test2'])
                    test3 = int(row['test3'])
                    homework = int(row['homework'])
                    
                    test_avg = (test1 + test2 + test3) / 3.0
                    weighted_average = (test_avg * 0.6) + (homework * 0.4)
                    
                    student_info = "Processing student: %s with average: %.1f" % (name, weighted_average)
                    logger.info(student_info)
                    
                    student = {
                        'name': name,
                        'test1': test1,
                        'test2': test2,
                        'test3': test3,
                        'homework': homework,
                        'test_average': test_avg,
                        'average': weighted_average
                    }
                    
                    students.append(student)
                    
                    debug_msg = "Student %s: Tests=[%d,%d,%d], HW=%d" % (name, test1, test2, test3, homework)
                    logger.debug(debug_msg)
                    
                except (ValueError, KeyError) as e:
                    error_msg = "Error processing row for student %s: %s" % (row.get('name', 'Unknown'), str(e))
                    logger.error(error_msg)
                    continue
                    
    except Exception as e:
        error_msg = "Error reading CSV file %s: %s" % (csv_file_path, str(e))
        logger.error(error_msg)
        raise
    
    logger.info("Successfully loaded %d students from CSV file" % len(students))
    return students

def get_student_count():
    """Helper function to get total number of students."""
    students = load_students()
    return len(students)

def save_backup():
    """Save a backup of student data to a temporary file."""
    if not os.path.exists('temp'):
        os.makedirs('temp')
    
    backup_file = open('temp/student_backup.txt', 'w')
    backup_file.write("Student data backup\n")
    backup_file.write("Generated automatically\n")
    
    students = load_students()
    for student in students:
        line = "Student: %s, Average: %.1f\n" % (student['name'], student['average'])
        backup_file.write(line)
    
    logger.info("Backup saved successfully")
