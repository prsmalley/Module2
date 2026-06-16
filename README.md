# Module 2 - Getting Input from the User

## For Students

### Getting Started
1. Accept the assignment invite link provided by your instructor
2. Once your repo is created, click the green **Code** button and select **Open with Codespaces**
3. Wait for the environment to load — Python and all extensions will be set up automatically

### Completing the Assignment
- Open `assignment02.py` and follow the instructions in the comments
- Complete each task in order (Task 01 through Task 04)
- This module is all about `input()` — remember to convert input with `int()` or `float()` before doing math!
- You can run your code at any time by clicking the **Run** button or typing `python assignment02.py` in the terminal. When it asks for input, type an answer in the terminal and press Enter.

### Extra Practice (not graded)
- `practice02.py` — five extra problems to practice `input()` and type conversion
- `madlibs02.py` — build a silly Mad Libs story; great practice and fun to share

### Submitting
- When you're done, save your file and commit your changes:
  1. Click the **Source Control** icon in the left sidebar (or press `Ctrl+Shift+G`)
  2. Type a commit message (e.g. "completed assignment 02")
  3. Click **Commit**, then **Sync Changes**
- The autograder will run automatically after every push — check the **Actions** tab in your repo to see your results
- You can push as many times as you like before the deadline

---

## For Instructors

### How This Repo Works
- `assignment02.py` — the student-facing template with task instructions and starter code (graded)
- `practice02.py` / `madlibs02.py` — ungraded extra practice files
- `tests/test_assignment02.py` — autograder tests that check each task's output
- `.github/workflows/grade.yml` — GitHub Action that runs on every push to `main`, executes the tests, and posts results as a commit comment
- `.devcontainer/devcontainer.json` — configures the Codespaces environment (Python 3.11, VS Code extensions, AI features disabled)

### Setting Up GitHub Classroom
1. Go to [classroom.github.com](https://classroom.github.com) and create/open your classroom
2. Click **New assignment** and use this repo as the starter code
3. Set visibility to **Private** so students can't see each other's work
4. Add an autograding test (**Run command**: `python tests/test_assignment02.py`) to populate the gradebook
5. Consider protecting `tests/` and `.github/` via **protected file paths**
6. Share the generated invite link with students
