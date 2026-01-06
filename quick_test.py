"""
Quick test to verify the Todo App runs without errors
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from main import TodoApp, Task

def test_basic_functionality():
    """Test basic functionality without user input"""
    print("Testing basic functionality...")
    
    # Create app instance
    app = TodoApp()
    print("[PASS] App created successfully")

    # Test adding tasks
    result = app.add_task("Test task 1")
    assert result == True, "Add task should succeed"
    print("[PASS] Add task works")

    # Test adding task with description
    result = app.add_task("Test task 2", "Test description")
    assert result == True, "Add task with description should succeed"
    print("[PASS] Add task with description works")

    # Test viewing tasks (this will print to console)
    app.view_tasks()
    print("[PASS] View tasks works")

    # Test updating task
    result = app.update_task(1, "Updated task title")
    assert result == True, "Update task should succeed"
    print("[PASS] Update task works")

    # Test toggling completion
    result = app.toggle_task_completion(1)
    assert result == True, "Toggle completion should succeed"
    print("[PASS] Toggle completion works")

    # Test toggling completion again (back to incomplete)
    result = app.toggle_task_completion(1)
    assert result == True, "Toggle completion should succeed"
    print("[PASS] Toggle completion works again")

    # Test getting task count
    count = app.get_task_count()
    assert count == 2, f"Should have 2 tasks, got {count}"
    print("[PASS] Get task count works")

    # Test error case - non-existent task
    result = app.update_task(999, "Non-existent task")
    assert result == False, "Update non-existent task should fail"
    print("[PASS] Error handling works")

    print("\n[SUCCESS] All basic functionality tests passed!")
    print("[SUCCESS] The Todo App is working correctly")

if __name__ == "__main__":
    test_basic_functionality()