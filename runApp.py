# run_app.py
import os
import subprocess

def run_prophet_model():
    try:
        # Ensure the python command is compatible with the user's environment
        python_command = 'python' if os.name == 'nt' else 'python3'
        subprocess.run([python_command, 'machineLearning/prophetModel.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running prophetModel.py: {e}")
        print("Please check the script for errors and ensure all dependencies are installed.")

def launch_gui():
    try:
        python_command = 'python' if os.name == 'nt' else 'python3'
        subprocess.run([python_command, 'machineLearning/vacationGui.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running vacationGui.py: {e}")
        print("Please check the script for errors.")

if __name__ == '__main__':
    print("Running the forecast model...")
    run_prophet_model()
    print("Launching the GUI...")
    launch_gui()
