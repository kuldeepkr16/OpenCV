import subprocess

# call this method to lock your mac screen
def screen_lock():

    cmd = "/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend"
    returned_value = subprocess.call(cmd, shell=True)
    print('returned value:', returned_value)


