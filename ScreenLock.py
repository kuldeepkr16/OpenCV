import subprocess

# call this method to lock your mac screen
def screen_lock_mac():

    cmd = "/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend"
    returned_value = subprocess.call(cmd, shell=True)
    print('returned value:', returned_value)



# call this method to lock your windows screen
def screen_lock_win():

    cmd = "rundll32.exe user32.dll,LockWorkStation"
    returned_value = subprocess.call(cmd, shell=True)
    print('returned value:', returned_value)

