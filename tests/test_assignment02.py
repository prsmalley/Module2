import subprocess
import sys

# The program asks the user questions with input(). To test it automatically,
# we send some answers in through stdin instead of typing them by hand.
FAKE_INPUT = "5\n" * 20

def run_assignment():
    result = subprocess.run(
        [sys.executable, 'assignment02.py'],
        input=FAKE_INPUT,
        capture_output=True, text=True
    )
    return result.stdout, result.returncode

def test_runs_without_errors():
    _, returncode = run_assignment()
    assert returncode == 0, "Code crashed — check for syntax/runtime errors (remember to convert input() with int() or float() before doing math)."

def test_all_sections_present():
    output, _ = run_assignment()
    for label in ('Task 01', 'Task 02', 'Task 03', 'Task 04'):
        assert label in output, f"Missing section: {label}."

def test_task01_output():
    output, _ = run_assignment()
    assert 'The remainder is:' in output, "Task 01: remainder not printed correctly."

def test_task03_output():
    output, _ = run_assignment()
    assert 'The area of the triangle is:' in output, "Task 03: triangle area not printed correctly."

def test_task04_output():
    output, _ = run_assignment()
    assert 'year' in output.lower(), "Task 04: message about the year they turn 100 not printed."

if __name__ == '__main__':
    tests = [
        test_runs_without_errors,
        test_all_sections_present,
        test_task01_output,
        test_task03_output,
        test_task04_output,
    ]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"  ✅ PASSED: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  ❌ FAILED: {test.__name__} — {e}")

    print(f"\n{passed}/{len(tests)} checks passed.")
    if passed < len(tests):
        sys.exit(1)  # Causes the Action to show as failed in GitHub
