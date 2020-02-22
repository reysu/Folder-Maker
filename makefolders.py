import os
#makes folders with a depth that you set
#expands breath first
cwd = os.getcwd();
print (cwd);
def makefolders():
    for x in range(4):
        os.mkdir(str(x));

makefolders();

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

def recurse(x, cwd):
    if(x == 3):
        os.chdir("..");
        return x;
    for z in range (4):
        os.chdir(cwd + "/" + str(z));
        print("Z: " + str(os.getcwd()) );
        makefolders();
        recurse(x+1, os.getcwd());
    os.chdir("..");

recurse(0, os.getcwd());
