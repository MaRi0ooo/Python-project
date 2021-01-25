from zipfile import *

arch = 1
i = 1

zipfilename = "test1.zip"
while arch:
    dictionary = "dictionary.txt"
    try:
        zip_file = ZipFile(zipfilename)
    except:
        v = 0
    if arch:
        Pass = None
        f = open(dictionary, "r")
        for line in f.readlines():
            Pass = line.strip('\n')
            try:
                zip_file.extractall(pwd=password.encode())
                print("Congratulations", Pass)
                f.close()
                zip_file.close()
                break
            except:
                continue
        zipfilename = "test1("+line+").zip"
        i += 1



# zipfilename = 'test1.zip'
# zipfilename_2 = 'test2.zip'
# dictionary = 'dictionary.txt'

# zip_file = zipfile.ZipFile(zipfilename)
# password = None
# f = open(dictionary, "r")

# for line in f.readlines():
#     password = line.strip('\n')
#     try:
#         zip_file.extractall(pwd=password.encode())
#         zipfile_name = zipfile.ZipFile(zipfilename_2)
#         print("Congratulations", password)
#         for line in f.readlines():
#             password = line.strip('\n')
#             try:
#                 zipfile_name.extractall(pwd=password.encode())
#                 print("Congratulations", password)
#                 f.close()
#                 break
#             except:
#                 print("myau", password)
#                 f.close()
#     except:
#         print("myau", password)
# f.close()

# a="*"
# row = [[a for i in range(8)]for j in range(8)]
# print(row)