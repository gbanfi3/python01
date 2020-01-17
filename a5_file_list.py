import os

for dirname, dirnames, filenames in os.walk('/home/gbanfi3/alma'):
    # print path to all subdirectories first.
    # print("-- ", dirname)
    # print(dirnames)
    # print(filenames)
    # for subdirname in dirnames:
    #     print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        print(filepath)
        print(os.stat(filepath).st_size)

    # # Advanced usage:
    # # editing the 'dirnames' list will stop os.walk() from recursing into there.
    # if '.git' in dirnames:
    #     # don't go into any .git directories.
    #     dirnames.remove('.git')