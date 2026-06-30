#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 3

// Define the data structure
typedef struct {
    char name[50];
    int math_score;
    int science_score;
    float average;
} Student;

int main() {
    // Hardcoded project data (simulating a database)
    Student students[MAX_STUDENTS] = {
        {"Alice Smith", 85, 92, 0.0},
        {"Bob Jones", 78, 80, 0.0},
        {"Charlie Brown", 95, 88, 0.0}
    };

    // Process data using C logic
    for (int i = 0; i < MAX_STUDENTS; i++) {
        students[i].average = (students[i].math_score + students[i].science_score) / 2.0;
    }

    // Print header for CSV parsing
    printf("Name,Math,Science,Average\n");

    // Output data to standard output
    for (int i = 0; i < MAX_STUDENTS; i++) {
        printf("%s,%d,%d,%.2f\n", 
               students[i].name, 
               students[i].math_score, 
               students[i].science_score, 
               students[i].average);
    }

    return 0;
}
