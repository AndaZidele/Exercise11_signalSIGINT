import time
import sys
import signal

# Write a program that executes a long task and has implementation to catch “CRTL+C” 
# and exit gracefully (without throwing exception).

def doThisTask(i):
    print("Step number {}.".format(i))

# funkcija, kas apstrādā CTRL+C signālu
def signalCatcher(sig, frame):
    print(" ")
    print("Signal catched!")
    sys.exit(0)

# lai tiktu reaģēts uz CTRL+C
signal.signal(signal.SIGINT, signalCatcher)

if __name__ == "__main__":
    i = 1
    try:
        while i < 100:
            doThisTask(i)
            time.sleep(1) # pēc vienas sekundes pildīt nnākamo fāzi
            i = i+1
    except KeyboardInterrupt:
        print(" ")
        print("Signal hasn't catched!")
        sys.exit(0) # lai neizvada kļūdas, ja arī gadījumā netika uzspiests CTRL+C