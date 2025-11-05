# Python Debugging Challenge

## Overview
Welcome to this technical interview debugging exercise. You have **20 minutes** to identify and fix bugs in a Student Grade Analyzer Pipeline. 

## Context
You are the "IT guy" at your local school. Once a year, there is a contest between the teachers at school, where the best class is honored. For this, you asked Github Copilot to setup a pipeline to do this task. This pipeline takes raw input data of student grades and does some calculations on it. Each student record contains grades of three tests and one homework, each graded in a range from **0 to 100 points.**

After the pipeline was executed, you was called by the school leadership that the pipeline did not calculate the result correctly. You see that there was an error when calculating the results of one class.

## Project Structure
```
grade_calculator/
├── main.py              # Main entry point
├── student_data.py      # Data handling module
├── grade_calculator.py  # Grade calculation utilities
├── students.csv         # Student data file (external data source)
└── INTERVIEWEE_README.md # This file
```

## Your Task - Follow These Steps in Order

### Step 1: Analyze Code and Understand It on an Abstract Level
- **Do NOT run the program yet** - analyze the code structure first
- Understand the data flow
- Identify the main components and their responsibilities

### Step 2: Analyze the Debug Log to Identify Issues
- Examine the provided log file from the failed pipeline run
- Look for issues

### Step 3: Find Root Causes and Fix Them
- Identify the root causes based on your log analysis
- Implement fixes for the identified problems
- Test your fixes by running `python3 main.py`

### Step 4: Think About What We Are Doing Here
- Reflect on the broader context of this exercise
    - *Hint*: Analyze the **students.csv** and think about the impact this has on our data cleaning efforts
- What risks do we encounter when working with this dataset?

Good luck!
