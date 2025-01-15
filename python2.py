
import subprocess

def execute_command(command):
    # This is vulnerable to shell injection attacks
    subprocess.run(command, shell=True)

# Example usage
execute_command("ls -la")
