#!/usr/bin/env python3
"""
Student Grade Analyzer - Main Entry Point
This program analyzes student grades and generates a class report.
"""

import student_data
import grade_calculator
import logging_config

# Setup logging
logger = logging_config.setup_logging()

def main():
    try:
        logger.info("Starting Student Grade Analyzer")
        logger.info("=== Student Grade Analyzer ===")
        
        students = student_data.load_students()
        logger.info("Loaded %d students" % len(students))
        logger.info("Successfully loaded %d students" % len(students))
        
        student_data.save_backup()
        
        if not students:
            logger.warning("No students found in the data")
            logger.warning("No students found in the data - terminating execution")
            return
        
        logger.info("Calculating letter grades for all students")
        for student in students:
            student['letter_grade'] = grade_calculator.get_letter_grade(student['average'])
            logger.info("%s: %.1f%% (%s)" % (student['name'], student['average'], student['letter_grade']))
        
        logger.info("--- Individual Student Results ---")
        for student in students:
            logger.info("Result: %s: %.1f%% (%s)" % (student['name'], student['average'], student['letter_grade']))
        
        logger.info("Calculating class statistics")
        logger.info("--- Class Statistics ---")
        
        all_averages = [student['average'] for student in students]
                
        logger.debug("Filtering valid grades")
        valid_grades = [avg for avg in all_averages if avg >= 100]
        logger.debug("Valid grades: %s" % valid_grades)
        logger.debug("Number of valid grades: %d" % len(valid_grades))
        
        class_average = sum(valid_grades) / len(valid_grades)
        
        highest_grade = max(valid_grades)
        lowest_grade = min(valid_grades)
        
        logger.info("Class Average: %.1f%%" % class_average)
        logger.info("Highest Grade: %.1f%%" % highest_grade)
        logger.info("Lowest Grade: %.1f%%" % lowest_grade)
        
        if class_average >= 85:
            logger.info("Overall Class Performance: Excellent")
        elif class_average >= 75:
            logger.info("Overall Class Performance: Good")
        elif class_average >= 65:
            logger.info("Overall Class Performance: Average")
        else:
            logger.info("Overall Class Performance: Needs Improvement")
            
    except Exception as e:
        import traceback
        logger.error("PIPELINE FAILURE: %s: %s" % (type(e).__name__, e))
        logger.error("Error occurred in main() function")
        logger.error("Full traceback:")
        
        # Log the full stack trace
        tb_lines = traceback.format_exc().strip().split('\n')
        for line in tb_lines:
            logger.error(line)
        
        logger.critical("Pipeline execution terminated due to unhandled exception")
        raise

if __name__ == "__main__":
    main()
