import subprocess

# call this method to bright your mac screen
def screen_bright():

    cmd = "brightness 0.7"
    returned_value = subprocess.call(cmd, shell=True)
    print('returned value:', returned_value)

# call this method to dim your mac screen
def screen_dim():

    cmd = "brightness 0.1"
    returned_value = subprocess.call(cmd, shell=True)
    print('returned value:', returned_value)



