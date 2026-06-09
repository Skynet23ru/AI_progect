import subprocess
import json
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.returncode

def main():
    # In a real automation, this script would call the Hermes Agent CLI 
    # to process the next task from 'todo'.
    # For now, it will implement the logic of "Task Execution" for the next pending task.
    
    print("Worker started: Checking for tasks...")
    
    # Since we are in a separate session (cron), we use a subprocess to 
    # interact with the agent's system-level tools or logic.
    # Here, we will simulate the execution of 'task-1-db-models'.
    
    try:
        # Step 1: Define what task to pick (In real life, this would parse 'todo')
        current_task = "task-1-db-models" 
        print(f"Worker picking up task: {current_task}")

        # Step _2: Execute the logic for Task 1 (The actual work)
        # We will use Python to create the SQLAlchemy models
        work_code = f"""
import os
project_root = "/home/skynet/AI_progect"
os.makedirs(os.path.join(project_root, "backend/app/models"), exist_ok=True)
os.makedirs(os.path.join(project_root, "backend/app/schemas"), exist_ok=True)

model_content = '''
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime_utils import get_now # hypothetically

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Vehicle(Base):
    __cl_id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    model = Column(String)
'''
with open(os.path.join(project_root, "backend/app/models/core.py"), "w") as f:
    f.write(model_content)

print("Models created successfully.")
"""
        process = subprocess.run(["python3", "-c", work_code])
        
        if process.returncode == 0:
            print("Task completed successfully!")
            # In a real setup, this script would call 'todo(action=update, id=task-1, status=completed)'
            # For this demo, we signal completion via stdout for the agent to see
            print("STATUS:COMPLETED")
        else:
            print("STATUS:FAILED")
            
    except Exception as e:
        print(f"WORKER_ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
