from Core.config import AVAILABLE_COMMANDS
from Commands import get_sysinfo, get_dashboard

def run_command(command: str):
    if command == "sysinfo":
        data = get_sysinfo()
        print(get_dashboard(data))
    elif command == "help":
        print("Available Commands:", ", ".join(AVAILABLE_COMMANDS))
    else:
        print(f"Unknown command: {command}")