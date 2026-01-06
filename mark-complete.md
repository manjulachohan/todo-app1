# Mark Task Complete Specification

## Feature Description
The application shall allow users to mark an existing task as complete or incomplete.

## Inputs
- Task ID (integer)
- Completion status (boolean - true for complete, false for incomplete)

## Expected Behavior
- User provides task ID and desired completion status
- System validates the task ID exists
- Updates the task's completion status
- System confirms successful status change

## Output
- Confirmation message showing the task and its new status
- Updated task details

## Edge Cases
- Invalid task ID should be handled gracefully
- Attempting to change status of already completed/incomplete task should work normally
- Task should maintain all other properties when status changes

## Validation Rules
- Task ID must exist in the task list