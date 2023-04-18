from wbscraper import main
#import subprocess
#subprocess.call(['python', 'wbscraper.py', '3845811748', 'harshit@3126'])

gpa = main("3845811748", "harshit@3126")
print(round(gpa, 3))

#gpa = wbscraper("3845811748", "harshit@3126")
#print(gpa)