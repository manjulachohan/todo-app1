# Add Task Specification

## Feature Description
The application shall allow users to add new tasks to the todo list.

## Inputs
- Task description (string)
- Optional due date (string in YYYY-MM-DD format)

## Expected Behavior
- User can input a task description
- System creates a new task with unique ID
- Task is added to the in-memory task list
- New task is marked as incomplete by default
- System confirms successful addition

## Output
- Confirmation message showing the added task
- Task ID for reference

## Edge Cases
- Empty task description should be rejected
- Invalid date format should be handled gracefully
- Duplicate task descriptions are allowed

## Validation Rules
- Task description must not be empty or whitespace only
- Task description must be less than 500 characters