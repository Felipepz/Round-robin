#!/usr/bin/env python3

import threading
import time
from time import sleep

quantum_time = 2
time_current = 0
queue = []

tasks = [
 {"name": "t.1", "time_ingress": 0, "duration": 5, "priority": 2},
 {"name": "t.2", "time_ingress": 0, "duration": 2, "priority": 3},
 {"name": "t.3", "time_ingress": 1, "duration": 4, "priority": 1},
 {"name": "t.4", "time_ingress": 3, "duration": 1, "priority": 4},
 {"name": "t.5", "time_ingress": 5, "duration": 2, "priority": 5},
]

def _processing(task):
  global tasks, time_current, queue
  print(f"Allocation q={quantum_time} time to the task {task['name']} at the time t={time_current}")

  taskduration = task['duration']
  auxduration = taskduration
  for i in range(quantum_time):
    if auxduration > 0: 
      print(f"A tarefa {task['name']} esta sendo processada ... ")
      time_current += 1
      auxduration -= 1
      sleep(1)
      get_tasks()
  taskduration -= quantum_time
  task.update(duration = taskduration)
  if taskduration >0:
    queue.append(task)
  print()
  pass

def get_tasks():
  global tasks, time_current, queue
  for item in tasks:
    if item['time_ingress'] == time_current:
      queue.append(item)
  pass

def run_scheduler():
    global tasks, time_current, queue
    print(r"Scheduler running...")
    while True:
      print(f"Getting the process list at the time t={time_current}\n")
      get_tasks()
      if len(queue) == 0:
        print(f"There is no task done at the time t={time_current}")
        time.sleep(1)
        time_current += 1
        break
      else:
        while True:
          try:
            queue=sorted(queue,reverse=True,key=lambda x:x['priority'])
            task = queue.pop(0)
            _processing(task=task)
          except IndexError:
            print(f"There is no item in the queue at the time t={time_current}")
            break

if __name__ == "__main__":
  scheduler = threading.Thread(target=run_scheduler)
  scheduler.start()
  scheduler.join()

