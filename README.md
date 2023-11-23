# Student Management Application

## Introduction

This Student Management Application is built using Flask, a powerful Python web framework. The application allows administrators to efficiently handle student information, access records, and manage academic data.

## Features

- View All Students: Administrators can easily access a complete list of all students available.

- Access Student Records: The application enables administrators to view detailed records and academic information for each student.

- Add New Students:  Allows to add new students to the system, ensuring an up-to-date student records in Json File.

- Delete Existing Students: Administrators can remove student records when necessary.

- Add Marks for Students: The application includes features to record and manage academic performance by adding marks for individual students.

- Average Marks and Percentage Display: Calculates and displays the average marks and percentage for each student, providing a quick overview of their academic standing.

## Student's Record Format

Each student's record includes the following details:

- Full Name
- Age
- Date of Birth
- Class
- Subjects List
- Marks in Each Subject
- Percentage and Grade
  
## Project Structure

The project is organized with the following structure:

- templates:
  - home_page.html: HTML template for the home page.
  - add_student.html: HTML template for adding new students.

- static:
  - home.css: CSS file for styling the home page.
  - add_student.css: CSS file for styling the add student page.

- data:
  - details.json: JSON file serving as the file-based storage system to store student details.

## Technologies Used

- Flask Framework: For backend of the application, providing a lightweight and efficient web framework for Python.

- File-Based Storage System (JSON): Utilizes JSON for a simple and effective file-based storage system, ensuring easy data management.

- HTML and CSS: Basic HTML for structure and CSS for styling create a straightforward frontend.

## Functionality

### 1. View Student List
- On the left side of the web page, find a section containing the list of all available students.
- Each student's name is a clickable link.

### 2. View Student Details
- Clicking on a specific student's name on the left side displays detailed information about that student on the right side of the web page.
- Information includes Full Name, Age, Date of Birth, Class, Subjects List, and Marks.

### 3. Delete Student
- While viewing a student's details, you have the option to delete that student.
- Upon deletion, the student is removed from the list, and the updated student list is displayed.

### 4. Add New Student
- A dedicated "Add Student" button is available, leading to a form where you can input details for a new student.
- After submitting the form, the new student is added to the list, and you can view their details by clicking on their name.

### 5. Update Student Details
- Clicking on the "Update Details" button for a student navigates you to a form where you can update the student's information.
- After updating, the student's details are refreshed, and the changes are reflected in the student list.

## Deployment

The application is deployed using [Render](https://render.com/) by connecting to the GitHub repository. Click here for the Hosted Website [Student Management Application](https://student-management-flask-app.onrender.com)
