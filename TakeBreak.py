import webbrowser
import time

print "The program started "+time.ctime()
for i in range(3):
    time.sleep(60*60*2)
    webbrowser.open("https://www.youtube.com/watch?v=S-tJuHsCDzc")
