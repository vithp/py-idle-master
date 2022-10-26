import subprocess
import os

idle_master_path = os.getcwd() + "\idlemaster"
batch_path = idle_master_path + "\pybatchscript.bat"
txt = open(batch_path, "w")
game_id = input("Game ID: ")

areyousure = input("Are you sure thats the correct game? [y/N]")

if areyousure == "n":
  game_id = input("Game ID: ")
  areyousure = input("Are you sure thats the correct game? [y/N]")
  if areyousure == "n":
    game_id = input("Game ID: ")
  elif areyousure == "N":
    game_id = input("Game ID: ")

elif areyousure == "N":
  game_id = input("Game ID: ")
  areyousure = input("Are you sure thats the correct game? [y/N]")
  if areyousure == "n":
    game_id = input("Game ID: ")
  elif areyousure == "N":
    game_id = input("Game ID: ")



batch_script = "@echo off \ncd idlemaster \nstart steam-idle " + game_id
txt.write(batch_script)
txt.close()

subprocess.call([batch_path])
if os.path.exists(batch_path):
  os.remove(batch_path)
