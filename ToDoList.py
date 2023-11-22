import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Create GUI components
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.pack()

        # Populate the listbox with existing tasks
        self.refresh_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_as_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task = f"{task} (Completed)"
            self.tasks[selected_index[0]] = task
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
