# task-tracker-cli

Self-built CLI to add, monitor, and get information about tasks.


### Prerequisites

- Requirements installations. In project directory, run the following line:
```bash
- pip install -r requirements.txt
```


Update path. This is a little bit complicated, must do in the following order.
#### In Windows:
    1) Press Win + R, type: sysdm.cpl → Enter
    2) Go to: Advanced → Environment Variables
    3) Under User variables, find Path → Click Edit
    4) Click New and add path to the project (thanks to task-cli.bat file, it works).


# How To Use

- Methods allowed:
  - add | add "Task X" | Output will be the id of the task
  - update | update {{ task-id }} "New task description" 
  - list | list {{ filter }} | Output will be list of tasks in a desired status, if filter parameter is unfilled, all tasks will be shown.
  - mark progress | mark-in-progress / mark-done / mark-todo {{ task-id }}
  - delete | delete {{ task-id }}

### Future Additions:
- Tests
- Validation and security
- Priority attribute
- Smart task saving

## Project URL
https://roadmap.sh/projects/task-tracker

