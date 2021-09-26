import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python", "Container_Parking.py",'input.txt'], stdout=output)
