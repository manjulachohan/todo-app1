# Update Task Specification

## Feature Description
The application shall allow users to update an existing task's description or due date.

## Inputs
- Task ID (integer)
- New task description (optional string)
- New due date (optional string in YYYY-MM-DD format)

## Expected Behavior
- User provides task ID and new information
- System validates the task ID exists
- Updates only the fields that are provided
- Maintains existing values for fields not provided
- System confirms successful update

## Output
- Confirmation message showing the updated task
- Updated task details

## Edge Cases
- Invalid task ID should be handled gracefully
- Empty description should be rejected if it's the only field being updated
- Invalid date format should be handled gracefully

## Validation Rules
- Task ID must exist in the task list
- If updating description, it must not be empty or whitespace only
- If updating due date, format must be valid