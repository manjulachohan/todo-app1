# Delete Task Specification

## Feature Description
The application shall allow users to delete an existing task from the todo list.

## Inputs
- Task ID (integer)

## Expected Behavior
- User provides task ID
- System validates the task ID exists
- Removes the task from the in-memory task list
- System confirms successful deletion

## Output
- Confirmation message showing the deleted task
- Success message

## Edge Cases
- Invalid task ID should be handled gracefully
- Deleting the last task should work correctly
- After deletion, remaining tasks maintain their IDs (no renumbering)

## Validation Rules
- Task ID must exist in the task list