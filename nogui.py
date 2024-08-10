# This is the version without a gui
# Make sure to run `pip install psutil`

import psutil  # Import the psutil module for process management

def kill_steam_processes():
    """
    Terminates all processes with 'steam' in their name.
    """
    # Iterate over all running processes
    for process in psutil.process_iter(['pid', 'name']):
        try:
            # Check if "steam" is in the process name (case insensitive)
            if 'steam' in process.info['name'].lower():
                # Print information about the process being terminated
                print(f"Terminating process: {process.info['name']} (PID: {process.info['pid']})")
                # Terminate the process using psutil's terminate method
                process.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle exceptions if the process is no longer available, access is denied, or the process is a zombie
            continue

if __name__ == "__main__":
    # Execute the function to kill all processes with 'steam' in their name
    kill_steam_processes()
