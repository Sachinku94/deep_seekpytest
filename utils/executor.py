import subprocess

def execute_generated_code(script_path="generated_code/temp_script.py"):
    try:
        subprocess.run(["python", script_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
        return False
