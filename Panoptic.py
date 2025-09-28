from Core.cli import run_command

def main():
    while True:
        cmd = input("Panoptic> ").strip()
        if cmd in ("exit", "quit"):
            break
        run_command(cmd)

if __name__ == "__main__":
    main()