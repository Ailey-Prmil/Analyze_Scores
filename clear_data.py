import re

with open ("data_backward.txt","r") as file, open ("test1.txt", "a", encoding="utf-8") as to_file, open ("unicode.txt","r", encoding="utf-8") as translator:
    unicode = []
    for line in translator.readlines():
        line = line.strip("\n")
        each_line = line.split(" ")
        unicode.append(each_line)

    for line in file.readlines():
        delete = re.compile("<.*?>|\s{2,}|\\\(n|r)")
        new_line = delete.sub("",line)
        for i in range (len(unicode)):
            new_line = new_line.replace(unicode[i][1],unicode[i][0])
        new_line = new_line.replace("b'Show - Sở Giáo dục và Đào tạo TP HCMĐIỂM THI TRUNG HỌC PHỔ THÔNG QUỐC GIAHọ và TênNgày sinhKết quả"," ")
        new_line = new_line.replace("&copy; 2022 - Sở Giáo dục và Đào tạo Thành phố Hồ Chí Minh - '"," ")
        chr_code = re.compile("\&\#\d+")
        l = re.findall(chr_code,new_line)
        code = [int(i[2:]) for i in l]
        for i in range (len(l)):
            new_line = new_line.replace(l[i]+";",chr(code[i]))
        new_line = new_line.replace("sbd","SBD")
        to_file.write(new_line)
        to_file.write("\n")


        


