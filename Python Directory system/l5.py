#!/usr/bin/python3
import datetime
datetime = datetime.datetime.now().month,'-',datetime.datetime.now().day,"-",datetime.datetime.now().year

class item:
    def __init__(self, name, p_dir, per_num):
        self.name = name
        self.p_dir = p_dir
        self.per_num = per_num

    def getName(self):
        return self.name

    def getParentDir(self):
        return self.p_dir

class Directory(item):
    def __init__(self, name, p_dir, per_num, update):
        self.item = item.__init__(self, name, p_dir, per_num)
        self.files = []

    def getFile(self):
        return self.files

class File(item):
    def __init__(self, name, p_dir,per_num, size):
        self.item = item.__init__(self, name, p_dir,per_num)
        self.size = size

# newdir = Directory("dirtest", "testparent")
# newfile = File("test", newdir)
# print(newfile.getName(), newfile.getParentDir().getName())
# filesystem.append(newdir)
filesystem = [Directory("/", "/","---",datetime)]
# filesystem[0].getName()
# print(newdir.getName(), newdir.getParentDir())


def find_directory(dir_name):
    for d in filesystem:
        if d.getName() == dir_name:
            return d
        if d.getName() is None:
            d = ""
            return d

def create_file():
    print("Please enter a File name or quit: ")
    user_input = input("> ")
    if user_input == "quit":
        return
    else:
        file_name = user_input

    print("Please enter a parent directory or quit: ")
    user_input = input("> ")
    if user_input == "quit":
        return
    else:
        f_pdir = user_input
        f_pdir_check = find_directory(f_pdir)

    # print (f_pdir_check);
    if f_pdir_check is None:
        print("ERROR: Parent Directory Does not Exist")
        return

    print("Please enter access permissions using format rwx or quit: ")
    while(True):
        user_input = input("> ")
        if user_input in ["---","--x","-w-", "-wx" ,"r--" ,"r-x" ,"rw-", "rwx"]:
            f_per_num = user_input
            break
        elif user_input == "quit":
            return
        else:
            print ("Enter permissions number rwx or ---")

    while(True):
        print("Please enter size (1-Small, 2-Medium, 3-Large): ")
        user_input = input("> ")
        if user_input == "1":
            f_size = "Small"
            break
        elif user_input == "2":
            f_size = "Medium"
            break
        elif user_input == "3":
            f_size = "Large"
            break
        else:
            print("Invalid input for size 1-3")

    new_file = File(file_name, f_pdir, f_per_num, f_size)
    find_directory(f_pdir).files.append(new_file)

def create_dir():
    print("Please enter Directory name or quit: ")
    user_input = input("> ")
    if user_input == "quit":
        return
    else:
        dir_name = user_input

    print("Please enter a parent directory or quit: ")
    user_input = input("> ")
    if user_input == "quit":
        return
    else:
        d_pdir = user_input
        d_pdir_check = find_directory(d_pdir)

    # print (f_pdir_check);
    if d_pdir_check is None:
        print("ERROR: Parent Directory Does not Exist")
        return

    print("Please enter access permissions using format rwx or quit: ")
    while(True):
        user_input = input("> ")
        if user_input in ["---","--x","-w-", "-wx" ,"r--" ,"r-x" ,"rw-", "rwx"]:
            f_per_num = user_input
            break
        elif user_input == "quit":
            return
        else:
            print ("Enter permissions number rwx or ---")


    new_dir = Directory(dir_name,d_pdir, f_per_num, datetime)
    filesystem.append(new_dir)

def print_system():
    # filesystem.sort(key=lambda x: x.getName())
    # for d in filesystem:
    #     print(d.getName())
    #     d.files.sort(key=lambda x: x.getName())
    #     for f in d.files:
    #         print("\t", f.getName())
    # if d.getParentDir() != "/":
    #   print(path.append(d.getName()))
    spacestring = ""
    for d in filesystem:
         directory = d.getParentDir()
         if directory == "/":
            print(d.getName())
            for f in d.files:
                print(spacestring +"\t", f.getName())
         if directory != "/":
            print(spacestring+ "\t",d.getName())
            for f in d.files:
                print(spacestring +"\t" +"\t", f.getName())

def remove_dir_file():
    print("Do you want to remove 1.File or 2.Directory:")
    choice = input("> ")
    if choice == "1":
        print("Enter the File You want to delete: ")
        file_input = input("> ")
        print("Enter the Directory that File in delete: ")
        dir_input = input("> ")
        for d in filesystem:
            if (d.getName() == dir_input):
                for f in d.files:
                    if(f.getName() == file_input):
                        d.files.remove(f)
    elif choice == "2":
        print("Enter the Directory You want to delete: ")
        dir_input = input("> ")
        for d in filesystem:
            if (d.getName() == dir_input):
                filesystem.remove(d)
    else:
        print("Invalid input 1 or 2")



if __name__ == "__main__":
    print("Welcome to Python's File System")
    while(True):
        print("1. Create a File\n2. Create a Directory\n3. Remove a File/Directory\n4. Display File System\n5. Exit")
        choice = input("> ")
        if choice == "1":
            create_file()
        elif choice == "2":
            create_dir()
        elif choice == "3":
            remove_dir_file()
        elif choice == "4":
            print_system()
        elif choice == "5":
            break
        else:
            print("Invalid input 1-5")
