import os
#makes folders with a depth that you set
#expands breath first
cwd = os.getcwd();
folders = int(input("How many folders do you want to make: "));
depth  = int(input("What depth do you want: "));

print (cwd);
def makefolders(folders):
    for x in range(folders):
        os.mkdir(str(x));


#brute force method (depth 3)
'''
for z in range (4):
    os.chdir(os.getcwd() + "/" + str(z));
    print("Z: " + str(os.getcwd()) );
    makefolders();
    for x in range (4):
        os.chdir(os.getcwd() + "/" + str(x));
        print("X: " + str(os.getcwd()) );
        makefolders();
        for y in range(4):
            os.chdir(os.getcwd() + "/" + str(y));
            print("Y: " + str(os.getcwd()) );
            makefolders();
            os.chdir("..");
        os.chdir("..");
    os.chdir("..");
'''

def recurse(d, cwd):
    if(d == depth):
        os.chdir("..");
        return d;
    for z in range (folders):
        os.chdir(cwd + "/" + str(z));
        print("Z: " + str(os.getcwd()) );
        makefolders(folders);
        recurse(d+1, os.getcwd());
    os.chdir("..");


#makefolders(folders);
#recurse(0, os.getcwd());
#print (cwd);

def make(cd, dp):
    if (dp == depth):
        return;
    for z in range (folders):
        try:
            os.mkdir(cd + "/" + str(z));
            print(str(cd + "/" + str(z)));
            make(cd + "/" + str(z) , dp + 1);
        except FileExistsError:
            next;
make(cwd, 0);



print("Done.")
