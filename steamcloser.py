# Made by toclick on discord ToClickx on GitHub

import tkinter as tk
from tkinter import messagebox
import psutil  # Import the psutil module for process management

def kill_steam_processes():
    """
    Terminates all processes with 'steam' in their name.
    """
    terminated = False
    # Iterate over all running processes
    for process in psutil.process_iter(['pid', 'name']):
        try:
            # Check if "steam" is in the process name (case insensitive)
            if 'steam' in process.info['name'].lower():
                # Print information about the process being terminated
                print(f"Terminating process: {process.info['name']} (PID: {process.info['pid']})")
                # Terminate the process using psutil's terminate method
                process.terminate()
                terminated = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle exceptions if the process is no longer available, access is denied, or the process is a zombie
            continue
    # Show a message box with the result
    if terminated:
        messagebox.showinfo("Success", "All 'steam' processes have been terminated.")
    else:
        messagebox.showinfo("No Processes Found", "No processes with 'steam' in their name were found.")

def create_gui():
    """
    Creates a GUI with a button to terminate all processes with 'steam' in their name.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Steam Steam")

    # Create a button to trigger process termination
    button = tk.Button(root, text="Terminate Steam Processes", command=kill_steam_processes, padx=20, pady=10)
    button.pack(padx=20, pady=20)

    tk.Label(root, text="Discord user: toclick GitHub: ToClickx").pack()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
