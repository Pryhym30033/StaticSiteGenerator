# %%
import os
import shutil

def RemoveFiles():
    shutil.rmtree("public")
    os.mkdir("public")
    
    return

def FolderfileCopier(srcdir, destdir):
    if not os.path.exists(destdir):
        os.mkdir(destdir)
        

    contents = os.listdir(srcdir)

    for item in contents:
        source = os.path.join(srcdir, item)
        destination = os.path.join(destdir, item)

        if os.path.isfile(source):
            shutil.copy(source, destination)
            
        else:
            FolderfileCopier(source, destination)    

def CopyControlFunc():
    RemoveFiles()
    FolderfileCopier("static", "public")
    return


# %%
