import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def search_files(source_folder, target_folder, result_folder):
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    source_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    source_names = {os.path.splitext(f)[0] for f in source_files}

    for root, dirs, files in os.walk(target_folder):
        for file in files:
            name, _ = os.path.splitext(file)
            if name in source_names:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(result_folder, file)
                shutil.move(source_path, destination_path)
                print(f"Moved: {file}")

def select_source_folder():
    folder = filedialog.askdirectory()
    entry_source.delete(0, tk.END)
    entry_source.insert(0, folder)

def select_target_folder():
    folder = filedialog.askdirectory()
    entry_target.delete(0, tk.END)
    entry_target.insert(0, folder)

def select_result_folder():
    folder = filedialog.askdirectory()
    entry_results.delete(0, tk.END)
    entry_results.insert(0, folder)

def start_search():
    source_folder = entry_source.get()
    target_folder = entry_target.get()
    result_folder = entry_results.get()
    
    if source_folder and target_folder and result_folder:
        search_files(source_folder, target_folder, result_folder)
        messagebox.showinfo("Completed", "File search and movement has been completed.")
    else:
        messagebox.showwarning("Warning", "Please select all the folders.")

# Create the main window
root = tk.Tk()
root.title("Bulk File Finder")

# Create and place the widgets
tk.Label(root, text="Source Folder:").grid(row=0, column=0, padx=10, pady=10)
entry_source = tk.Entry(root, width=50)
entry_source.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Select", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Target Folder:").grid(row=1, column=0, padx=10, pady=10)
entry_target = tk.Entry(root, width=50)
entry_target.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Select", command=select_target_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Result Folder:").grid(row=2, column=0, padx=10, pady=10)
entry_results = tk.Entry(root, width=50)
entry_results.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Select", command=select_result_folder).grid(row=2, column=2, padx=10, pady=10)

tk.Button(root, text="Start Search", command=start_search).grid(row=3, column=0, columnspan=3, padx=10, pady=20)

# Start the application loop
root.mainloop()
