import os

#Creating file 0 with text
myfile0 = open("2_file_1.txt","w+",encoding="utf-8")
myfile0.write("ее скотчем к пульту от телевизора и звонить на него, когда тот теряется!")
myfile0.close()

#Creating file 1 with text
myfile1 = open("2_file_2.txt","w+",encoding="utf-8")
myfile1.write("Только мой папа догадался купить новую мобилу, примотать ")
myfile1.close()

#Append text from first file to the end of second 
with open("2_file_1.txt",encoding=("utf-8")) as f:
    with open("2_file_2.txt","a+",encoding=("utf-8")) as f1:
        for line in f:
            f1.write(line)
f.close()
f1.close()

#Deleting file 0
os.remove("2_file_1.txt")