import subprocess
import os

idle_master_path = os.getcwd() + "\idlemaster"
batch_path = os.getcwd() + "\pybatchscript.bat"
txt = open("pybatchscript.bat", "w")
game_id = input("Game ID: ")

areyousure = input("Are you sure thats the correct game? [y/N]")

if areyousure == "n":
  game_id = input("Game ID: ")
  areyousure = input("Are you sure thats the correct game? [y/N]")
  if areyousure == "n":
    game_id = input("Game ID: ")
    areyousure = input("Are you sure thats the correct game? [y/N]")
  elif areyousure == "N":
    game_id = input("Game ID: ")
    areyousure = input("Are you sure thats the correct game? [y/N]")

elif areyousure == "N":
  game_id = input("Game ID: ")
  areyousure = input("Are you sure thats the correct game? [y/N]")
  if areyousure == "n":
    game_id = input("Game ID: ")
    areyousure = input("Are you sure thats the correct game? [y/N]")
  elif areyousure == "N":
    game_id = input("Game ID: ")
    areyousure = input("Are you sure thats the correct game? [y/N]")


batch_script = "@echo off \ncd idlemaster \nstart steam-idle " + game_id
txt.write(batch_script)
txt.close()

subprocess.call([batch_path])
if os.path.exists("pybatchscript.bat"):
  os.remove("pybatchscript.bat")
