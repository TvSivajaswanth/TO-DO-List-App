# To Do List App

A simple desktop to-do list built with Python and Tkinter. No accounts, no internet, no extra libraries. Add your tasks, tick them off, and they're still there the next time you open the app.

I made this as a small project to practice Tkinter, multi-page GUIs, and saving data to a file.

## What it can do

- **Add** a task
- **View** all your tasks with their status (Pending / Completed)
- **Complete** a task by its ID
- **Delete** a task by its ID
- **Auto-save**: everything is stored in a `tasks.json` file, so nothing is lost when you close the app

## Getting started

### What you need

- **Python 3.12 or newer** (the code uses nested quotes inside f-strings, which older versions don't allow)
- Tkinter, which comes bundled with most Python installs

To check that Tkinter works on your machine:

```bash
python -m tkinter
```

A small test window should pop up. On some Linux systems you may need to install it first:

```bash
sudo apt install python3-tk
```

### Run it

1. Save the code as `main.py` (or any name you like).
2. Open a terminal in that folder and run:

```bash
python main.py
```

The app opens on the home screen. A `tasks.json` file will be created automatically the first time you add a task.

## How to use it

| Page | What to do |
|------|------------|
| **Add Task** | Type your task and hit **SUBMIT**. You'll see "Added Successfully". |
| **View Task** | Shows every task as `ID. task is [status]`. Hit **Refresh List** to see the latest changes. |
| **Complete Task** | Enter the task's ID and hit **Complete Task**. |
| **Delete Task** | Enter the task's ID and hit **Delete Task**. |
| **EXIT** | Closes the app. |

Every page has a **Back to Home** button.

> **Tip:** The View page doesn't update by itself. After adding, completing, or deleting something, go to View Task and press **Refresh List**.

## How the data is stored

Tasks are saved in `tasks.json` next to the script, like this:

```json
[
    {
        "id": 1,
        "task": "Buy groceries",
        "completed": false
    },
    {
        "id": 2,
        "task": "Finish homework",
        "completed": true
    }
]
```

IDs are assigned automatically (highest existing ID + 1). If the file is missing or broken, the app just starts with an empty list instead of crashing.

## Project structure

```
.
├── main.py       # the whole app
├── tasks.json    # created automatically when you add your first task
└── README.md
```

## How it works (quick overview)

- Each screen (home, add, view, complete, delete) is a `Frame` stacked in the same spot in the window.
- `show_page()` uses `tkraise()` to bring the chosen frame to the front, so there's only ever one window.
- Tasks live in a Python list of dictionaries and get written to `tasks.json` with the `json` module whenever something changes.

## Ideas for the future

- Refresh the task list automatically after any change
- Select a task from the list instead of typing its ID
- Edit existing tasks
- Due dates and priorities
- A confirmation popup before deleting
- Dark mode

## License

Free to use, change, and learn from. Do whatever you like with it.
