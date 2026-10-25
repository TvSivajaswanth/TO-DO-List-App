import json
from tkinter import*

root = Tk()
root.title("To Do List App")
root.geometry("400x400")
container = Frame(root)
container.pack(fill="both", expand=True)


home_page = Frame(container)
add_page = Frame(container)
view_page = Frame(container)
complete_page = Frame(container)
delete_page = Frame(container)

pages = [
    home_page, add_page, view_page,
    complete_page, delete_page
]

for page in pages:
    page.grid(row=0,column=0,sticky="nsew")
    

def show_page(page):
    page.tkraise()

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
 
def store_task():
    with open("tasks.json", "w") as file:
      json.dump(tasks, file, indent=4)

tasks = load_tasks()


Label(
    home_page,
    text="To Do List App",
    font=("Arial", 20, "bold")
).pack(pady=20)


Button(home_page,text="Add Task",width=20,height=2,command=lambda: show_page(add_page)).pack(pady=5)   
Button(home_page,text="View Task",width=20,height=2,command=lambda: show_page(view_page)).pack(pady=5)   
Button(home_page, text="Complete Task",width=20,height=2, command=lambda: show_page(complete_page)).pack(pady=5)
Button(home_page, text="Delete Task",width=20,height=2, command=lambda: show_page(delete_page)).pack(pady=5)
Button(home_page,text="EXIT",width=20,height=2,command=root.quit).pack(pady=5)   


# -----add task-------

Label(add_page,text="ADD A TASK",font=("Arial", 20, "bold")).pack(padx=10,pady=10)

add_task = Entry(add_page, width=30, font=("Arial", 16))
add_task.pack(padx=10, pady=10)

result_add_task = Label(add_page, text="")
result_add_task.pack(padx=10,pady=10)

def add_tasks():
    task = add_task.get().strip()

    if not task:
        return

    task_id = max(
        (item["id"] for item in tasks),
        default=0
    ) + 1

    new_task = {
        "id": task_id,
        "task": task,
        "completed": False
    }

    tasks.append(new_task)
    store_task()
    result_add_task.config(text="Added Successfully")
    add_task.delete(0,END)
    

Button(add_page, text="SUBMIT",width=20,height=2, command=add_tasks).pack(padx=10, pady=10)

Button(add_page,text="Back to Home",width=20,height=2,command=lambda: show_page(home_page)).pack(padx=10,pady=10)

# ---view task---

Label(
    view_page, text="All Tasks",
    font=("Arial", 18, "bold")
).pack(pady=20)

task_list = Listbox(view_page, width=40, height=8,font=("Segoe UI", 10, "bold"),justify="center")
task_list.pack(pady=5)

def refresh():
    task_list.delete(0,END)
    
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_list.insert(
            END,
            f"{task["id"]}. {task["task"]} is [{status}]"
        )
refresh()    
Label(view_page,text="press Refresh to see up to date information").pack(padx=10,pady=10)
Button(
    view_page, text="Refresh List",width=20,height=2,
    command=refresh
).pack(pady=5)

Button(
    view_page, text="Back to Home",width=20,height=2,
    command=lambda: show_page(home_page)
).pack(pady=5)


# -----complete task------


Label(
    complete_page, text="complete Tasks Here",
    font=("Arial", 18, "bold")
).pack(pady=20)
Label(
    complete_page, text="Enter the ID here",
    font=("Arial", 10, "bold")
).pack(pady=20)

complete = Entry(complete_page, width=30, font=("Arial", 16))
complete.pack(padx=10,pady=10)
result_complete_task = Label(complete_page, text="")
result_complete_task.pack()

def complete_task():
    try:
      c_id = int(complete.get())
    except ValueError:
        result_complete_task.config(text="Please enter a valid number")
        return
    
    for t in tasks:
            if t["id"] == c_id:
                if t["completed"]:
                    result_complete_task.config(text="U Already completed this task")
                    complete.delete(0,END)
                    return
                else:
                     t["completed"] = True
                     store_task()
                     result_complete_task.config(text="Completed successfully")
                     complete.delete(0,END)
                     return
            else:
                  result_complete_task.config(text="Task ID not found")           
Button(
    complete_page, text="Complete Task",width=20,height=2,
    command= complete_task
).pack(pady=5)   
Button(
    complete_page, text="Back to Home",width=20,height=2,
    command=lambda: show_page(home_page)
).pack(pady=5)
# ======delete task======

Label(
    delete_page, text="Delete Task Here",
    font=("Arial", 18, "bold")
).pack(pady=20)
Label(
    delete_page, text="Enter the ID here to delete",
    font=("Arial", 10, "bold")
).pack(pady=20)

delete_task = Entry(delete_page, width=30, font=("Arial", 16))
delete_task.pack(padx=10,pady=10)
result_delete_task = Label(delete_page, text="")
result_delete_task.pack()

def delete_tasks():
    
    try:
          c_id = int(delete_task.get())
    except ValueError:
            result_delete_task.config(text="Please enter a valid number")
            delete_task.delete(0,END)
            return
    
    for t in tasks:
        if t["id"] == c_id:
            tasks.remove(t)
            store_task()
            result_delete_task.config(text=f"ID:{c_id} is Deleted successfully !")
            delete_task.delete(0,END)
            
            break
        else:
            result_delete_task.config(text = f"ID:{c_id} not found")
            delete_task.delete(0,END)
        
Button(
    delete_page, text="Delete Task",width=20,height=2,
    command= delete_tasks
).pack(pady=5)   
Button(
    delete_page, text="Back to Home",width=20,height=2,
    command=lambda: show_page(home_page)
).pack(pady=5)

show_page(home_page)
root.mainloop()