import os
from tkinter import *
from tkinter import filedialog
import shutil
root = Tk()
root.title("MinecraftLoader")
Label(root,text="MinecraftLoader",font=("arial",30,"normal") , fg="green").grid(row=0,column=0)

def mods():
    pop = Tk()
    pop.title("MinecraftLoader")
    list_of_mods = os.listdir(f'C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\mods')
    row = 2
    frames=dict()
    def load():
        mod = filedialog.askopenfilename(title="Select your mod file").replace("/","\\")
        print(f'copy "{mod}" "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\mods"')
        os.system(f'copy "{mod}" "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\mods"')
        pop.destroy()
        mods()
    Label(pop,text="Mods:",font=("arial",30,"normal")).grid(row=0,column=0)
    Button(pop, text="Load a new mod",command=lambda: load()).grid(row=1,column=0)
    def delete(mod):
        os.remove(f'C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\mods\\{mod}')
        pop.destroy()
        mods()
    def move(mod):
        os.system(f'move "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\mods\\{mod}" "C:\\Users\\{os.getenv("username")}\\Downloads"')
        pop.destroy()
        mods()
    for mod in list_of_mods:
        row += 1
        frames[mod] = Frame(pop)
        frames[mod].grid(row=row,column=0)
        Label(frames[mod],text=mod).grid(row=0,column=0)
        Button(frames[mod],text="Delete this mod" , command=lambda: delete(mod)).grid(row=0,column=1)
        Button(frames[mod], text="Move this mod to downloads",command= lambda: move(mod)).grid(row=0, column=2)

def txtpack():
   pop = Tk()
   pop.title("MinecraftLoader")
   def zipf():
       file = filedialog.askopenfilename(title="Select your texturepack file").replace("/","\\")
       print(f'copy "{file}" "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\resourcepacks"')
       os.system(f'copy "{file}" "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\resourcepacks"')
       pop.destroy()

   def fold():
       backslash = "\\"
       file = filedialog.askdirectory(title="Select your texturepack folder").replace("/","\\")
       shutil.copytree(f"{file}",f'C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\resourcepacks\\{file.split(backslash)[-1]}')
       pop.destroy()
   Button(pop,text="Load a .zip texturepack", command=lambda: zipf()).grid(row=0,column=0,padx=20,pady=20)
   Button(pop, text="Load a folder texturepack", command= lambda: fold()).grid(row=1, column=0)

def world():
   pop = Tk()
   pop.title("MinecraftLoader")
   def zipf():
       file = filedialog.askopenfilename(title="Select  your  world file").replace("/","\\")
       print(f'copy "{file}" "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\saves"')
       os.system(f'copy "{file}" "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\saves"')
       pop.destroy()

   def fold():
       backslash = "\\"
       file = filedialog.askdirectory(title="Select your world folder").replace("/","\\")
       shutil.copytree(f"{file}",f'C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\saves\\{file.split(backslash)[-1]}')
       pop.destroy()
   Button(pop,text="Load a .zip world", command=lambda: zipf()).grid(row=0,column=0,padx=20,pady=20)
   Button(pop, text="Load a folder world", command= lambda: fold()).grid(row=1, column=0)

def datapack():
    list_of_worlds = os.listdir(f'C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\saves')
    pop = Tk()
    pop.title("MinecraftLoader")
    Label(pop,text="Select a world that you want to install the datapack",font=("arial",15,"normal")).grid(row=0,column=0)
    row = 0
    def action(world):
        pop.destroy()
        pop2 = Tk()
        pop2.title("MinecraftLoader")
        Label(pop2,text="Is your datapack a folder , or a zip file?").grid(row=0,column=0)
        fr = Frame(pop2)
        fr.grid(row=1,column=0)
        def fold():
            backslash = "\\"
            file = filedialog.askdirectory(title="Select your datapack folder").replace("/","\\")
            shutil.copytree(file,f'C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\saves\\{world}\\datapacks\\{file.split(backslash)[-1]}')
            pop.destroy()
        def zipf():
            file = filedialog.askopenfilename(title="Select your datapack file").replace("/","\\")
            os.system(f'copy "{file}" "C:\\Users\\{os.getenv("username")}\\AppData\\Roaming\\.minecraft\\saves\\{world}\\datapacks"')
            pop.destroy()
        Button(fr,text="Folder", command=lambda: fold()).grid(row=0,column=0)
        Button(fr,text="Zip file",command=lambda: zipf()).grid(row=0,column=1 , padx=12)
    for world in list_of_worlds:
        row += 1
        Button(pop,text=world,command=lambda: action(world)).grid(row=row,column=0)

Button(root,text="Mods",command=lambda: mods()).grid(row=1,column=0)
Button(root,text="Texture packs" , command=lambda: txtpack()).grid(row=2,column=0)
Button(root,text="Worlds", command=lambda: world()).grid(row=3,column=0)
Button(root,text="Datapacks", command=lambda: datapack()).grid(row=4,column=0)
root.mainloop()