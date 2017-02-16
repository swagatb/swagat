from subprocess import call
import time

def temp_mon_off():
    a = 0
    while True:
        call("export DISPLAY=:0 && sudo xset dpms force off",shell=True)
        a += 1
        print a
        time.sleep(15)
    
def mon_on():
    call(["sudo", "vbetool", "dpms", "on"])
    
if __name__ == "__main__":
    temp_mon_off()
