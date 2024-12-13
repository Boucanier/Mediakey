import sys
import psutil


def is_script_running(script_path):
    for proc in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
        try:
            # Check if the process is a Python script
            if proc.info["name"] in ["python.exe", "pythonw.exe"]:
                # Check if the script path is in the command line arguments
                if script_path in " ".join(proc.info["cmdline"]):
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False


if __name__ == "__main__":
    script_to_check = "mediakey.py"
    if is_script_running(script_to_check):
        sys.exit(1)  # Return 1 if the script is running
    sys.exit(0)  # Return 0 if the script is not running
