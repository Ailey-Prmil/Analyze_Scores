#Q1 : Which subject did each student receive with the highest score ? (done)
#Q2 : Pho diem theo khoi (A0,A1,B0,B1)
#Q3 : Bar chart describes the number of students could not score over 1 in tandem with the number of students scoring 10
#Q4 : KHTN and KHXH, which have higher score
import re
import matplotlib.pyplot as plt
students = []

def search_line(regex,index=1): # Searching using REGEX
    global line # using variable line outside the function
    compile = re.compile(regex) 
    search = compile.search(line)
    if search == None:
        return (0)
    result = search.group(index)
    return (result)
def bar_chart(x_axis, y_axis,x_label,y_label,title=None):
    # making barchart (x_axis,y_axis,x_label,y_label,title)
    #x_axis, y_axis : list
    #x_label, y_label, title : string
    plt.bar(x_axis,y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
def line_chart (x_axis, y_axis,x_label,y_label,title=None):
    # making line chart (x_axis,y_axis,x_label,y_label,title)
    #x_axis, y_axis : list
    #x_label, y_label, title : string
    plt.plot(x_axis,y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

with open ("clean_data.txt","r",encoding="utf-8") as file : #file having utf-8 encoding
    for line in file.readlines():
        if line == "\n": continue # remove blank lines
        elif "Không tìm thấy số báo danh này" in line : continue # remove outliers
        SBD = search_line(r"SBD\s*:\s*(\d{8})\s+(.*) Toán") # SBD_:_(8 digits)_(everything) Toan
        Name = search_line(r"SBD\s*:\s*(\d{8})\s+(.*) Toán",2) # regex : same as SBD but in grp 2
        Math = search_line(r"Toán:(\S+)") # Toan: (except space)
        Literature = search_line(r"Ngữ văn:(\S+)") # Ngu van: (except space)
        Language = search_line(r"Tiếng \w+:(\S+)") # Tieng words(1+):(except space)
        # need to divide students in two types
        if ("KHTN"in line): # 3 subjects in KHTN
            Mon1 = search_line(r"Vật lí:(\S+)") #same
            Mon2 = search_line(r"Hóa học:(\S+)") #same
            Mon3 = search_line(r"Sinh học:(\S+)") #same
            KHTN_KHXH = search_line(r"KHTN:\s*(\S+)")#same
            label = 0   #KHTN = 0
        else: #3 subjects in KHXH
            Mon1 = search_line(r"Lịch sử:(\S+)")#same
            Mon2 = search_line(r"Địa lí:(\S+)")#same
            Mon3 = search_line(r"GDCD:(\S+)")#same
            KHTN_KHXH = search_line(r"KHXH:\s*(\S+)")#same
            label = 1 #KHXH = 1
        #element_list = [SBD,tên,toán,văn,lý/sử,hóa/địa,sinh/GDCD,Ngoại ngữ, label, KHTN/KHXH] -> len = 10
        students.append([SBD, Name, Math, Literature, Mon1, Mon2, Mon3, Language,label,KHTN_KHXH])

# students = [[],[],[],[],[],[],...] each element contains [SBD,Name,Math,Liter,Mon1,Mon2,Mon3,Language,label,KHTN/KHXH]
# score = [[],[],[],[],[],[],...] each element contains [Math -> KHTN/KHXH] (len = 7)
    """ Bang index cua x in score :
    Toan : 0
    Van : 1
    Ly/ Su : 2
    Hoa/ Dia : 3
    Sinh/GDCD : 4
    Ngoai ngu : 5
    label : 6
    """
score = [x[2:10] for x in students]
for x in range (len(score)):# change str element in (score list elements) to float
    score[x]= [float(i) for i in score[x]]
def Q_1(score):
    sub = ["Math","Literature","Physics","Chemistry","Biology","Languages","History","Geography","GDCD"]
    count = [0 for i in range(len(sub))]
    for x in score :
        highest_score = max(x)
        index = [i for i in range(len(x)) if x[i]== highest_score]

        if x[6]==1: # thi môn KHXH
            for i in index :
                if i in [2,3,4]: # mon khxh
                    count[i+4]+=1
                elif i == 6: # label
                    continue
                else: # toán, văn, ngoại ngữ (0,1,5)
                    count [i]+=1
        else: # thi môn KHTN
            for i in index :
                if i == 6: 
                    continue
                count[i]+=1
    return (sub,count)
###Q1### - môn nào thí sinh thường có điểm cao nhất khi thi : Toán and GDCD
x_axis, y_axis = Q_1(score)
x_label = "Subjects"
y_label = "Times each subjects being the best score of a student"
title = "Which subject did each student receive with the highest score ?"
bar_chart (x_axis, y_axis,x_label,y_label,title)
#######
     
def sub_group (score,group):  #group = A0,A1 --->Q2
    group_score = []  
    stu_mark = 0
    for student in score :
        if (student[6]==1):
            continue
        else:
            A0 = student[0]+student[2]+student[3] #MATH + PHYSICS + CHEMISTRY
            A1 = student[0]+student[2]+student[5] #MATH + PHYSICS + LANGUAGE

            if group == "A1":
                group = A1
            else: 
                group = A0
        
            if(group)<20:
                continue
            else :
                group_score.append(group)
                
    x_axis=set(group_score)
    x_axis = sorted (list(x_axis))
    y_axis=[0 for i in range (len(x_axis))]
    group_score.sort() 
    for score in group_score:
        if score == x_axis[stu_mark]:
            y_axis[stu_mark] +=1
        else:
            stu_mark +=1
            y_axis[stu_mark] +=1
    print (group_score[277])
    print (x_axis[:10])
    print (y_axis[:10])
    return (x_axis,y_axis)
####Q2###
group = "A0"
x_axis, y_axis = sub_group(score,group)
line_chart(x_axis, y_axis,"Scores","Number of Students",f"Phổ điểm của {group}")
######