import psutil
import sys

def stop_script(script_name):
    for proc in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
        try:
            if proc.info["name"] in ["python.exe", "pythonw.exe"] and script_name in " ".join(proc.info["cmdline"]):
                print(f"Stoping {proc.pid} executing {script_name}...")
                proc.terminate()  # Send SIGTERM signal
                proc.wait(timeout=5)  # Wait for process to terminate
                print(f"Successfully stoped {proc.pid}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print(f"No process found for {script_name}")
    return False

if __name__ == "__main__":
    script_to_stop = "mediakey.py"
    if stop_script(script_to_stop):
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Fail
