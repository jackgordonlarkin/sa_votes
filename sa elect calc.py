import math
from pynode.main import *
import csv
votes = open ('sabooths.csv','r')
begin_pynode()
headers = votes.readline()
headers = headers.split(',')
TOTAL = votes.readline()
TOTAL = TOTAL.split(',')
other = -133
print (headers[2:43])
while other <= 0:
        lib = float(input("What % votes will the LNP recieve:"))/100
        alp = float(input("What % votes will the ALP recieve:"))/100
        grn = float(input("What % votes will the Greens recieve:"))/100
        nxt = float(input("What % votes will the NXT/SA Best recieve:"))/100
        other = float(1-grn-nxt-alp-lib)
grandtotal = int(TOTAL[2])+int(TOTAL[6])+int(TOTAL[10])+int(TOTAL[14])+int(TOTAL[28])              
alpm = alp/((int(TOTAL[2]))/grandtotal)
libm = lib/((int(TOTAL[6]))/grandtotal)
nxtm = nxt/((int(TOTAL[10]))/grandtotal)
grnm = grn/((int(TOTAL[14]))/grandtotal)
othm = other/((int(TOTAL[28]))/grandtotal)
SEATS = [0]*50
PRIMARY=[[0]*5 for i in range(50)]
CP3 = [[0]*3 for i in range(50)]
CP2 = [[0,0,0,0]for i in range(50)]
seattotal = ["seats", "ALP",0,"LIB",0,"NXT/SA BEST",0, "IND/OTHER",0]
seats = 0
store = 0
seats -= 1
electorate = [0]*41
incumbents = open('incumbent.csv','r')
incumbent = incumbents.readline()
incumbent = incumbent.split(',')
nxtcheck = incumbents.readline().split(',')
while seats < 47:
    booth = votes.readline()
    booth = booth.split(',')
    booth[2:43] =[int(i) for i in booth[2:43]]
    booth[2:43] = [float(i) for i in booth[2:43]]
    booth[3] = booth[3]+(booth[5]/2)
    booth[4] = booth[4]+(booth[5]/2)
    booth[2:6] = [i*alpm for i in booth[2:6]]
    booth[7] = booth[7]+(booth[9]/2)
    booth[8] = booth[8]+(booth[9]/2)
    booth[6:10] = [i * libm for i in booth[6:10]]
    booth[11] = booth[11]+(booth[13]/2)
    booth[12] = booth[12]+(booth[13]/2)
    booth[10:14] = [i * nxtm for i in booth[10:14]]
    if sum(booth[16:18]) != 0:
        booth[16:18] = [float(i)*(booth[15]/(booth[15]-booth[18])) for i in booth[16:18]]
    if sum(booth[20:22]) != 0:
        booth[20:22] = [float(i)*(booth[19]/(booth[19]-booth[22])) for i in booth[20:22]]
    if sum(booth[24:26]) != 0:
        booth[24:26] = [float(i)*(booth[23]/(booth[23]-booth[26])) for i in booth[24:26]]
    if sum(booth[15:27]) !=0:
        booth[15:27] = [float(i)*(int(booth[14])/(int(booth[14])-int(booth[27]))) for i in booth[15:27]]
    booth[14:28] = [float(i)*grnm for i in booth[14:28]]

    if booth[29]!=0:
        booth[29] += booth[41]/3
        oalpm = booth[29] / (booth[29] - (booth[41] / 3))
        booth[30:32] = [(float(i)+(booth[32]/2))*oalpm for i in booth[30:32]]
    if booth[33] !=0:
        booth[33] += booth[41] / 3
        olibm = booth[33] / (booth[33] - (booth[41] / 3))
        booth[34:36] = [(float(i)+(booth[36]/2))*olibm for i in booth[34:36]]

    if booth[37] != 0:
        booth[37] += booth[41]/3
        onxtm = booth[37]/(booth[37]-(booth[41]/3))
        booth[38:40] = [(float(i)+(booth[40]/2))*onxtm for i in booth[38:40]]
    """if sum(booth[30:32]) != 0:
        booth[30:32] = [float(i)+(booth[32]/2) for i in booth[30:32]]
    if sum(booth[34:36]) != 0:
        booth[34:36] = [float(i)+(booth[36]/2) for i in booth[34:36]]
    if sum(booth[38:40]) != 0:
        booth[38:40] = [float(i)+(booth[40]/2) for i in booth[38:40]]
    if sum(booth[29:41]) !=0:
        booth[29:41] = [float(i)*(booth[28])/(booth[28])-(booth[41]) for i in booth[29:41]]"""
    booth[28:42] = [float(i)*othm for i in booth[28:42]]
    if booth[0] != store:
        if sum(electorate) != 0:
            seats +=1
            SEATS[seats] = store
            PRIMARY[seats][0] = electorate[0]
            PRIMARY[seats][1] = electorate[4]
            PRIMARY[seats][2] = electorate[8]
            PRIMARY[seats][3] = electorate[12] 
            PRIMARY[seats][4] = electorate[26]
            if incumbent[seats] == "ALP":
                PRIMARY[seats][0] += (electorate[0]+electorate[4]+electorate[8]+electorate[12]+electorate[26])*0.01
                PRIMARY[seats][1:5] = [i*(((electorate[0]+electorate[4]+electorate[8]+electorate[12]+electorate[26])-PRIMARY[seats][0])/(electorate[4]+electorate[8]+electorate[12]+electorate[26]) )for i in PRIMARY[seats][1:5]]
            if incumbent[seats] == "LIB":
                PRIMARY[seats][1] += (electorate[0] + electorate[4] + electorate[8] + electorate[12] + electorate[26]) * 0.01
                PRIMARY[seats][2:5] =  [i*(((electorate[0]+electorate[4]+electorate[8]+electorate[12]+electorate[26])-PRIMARY[seats][1])/(electorate[0]+electorate[8]+electorate[12]+electorate[26])) for i in PRIMARY[seats][2:5]]
                PRIMARY[seats][0] *= ((electorate[0]+electorate[4]+electorate[8]+electorate[12]+electorate[26])-PRIMARY[seats][1])/(electorate[0]+electorate[8]+electorate[12]+electorate[26])
            CP3[seats][0] = electorate[0]+electorate[13]+electorate[27]
            CP3[seats][1] = electorate[4]+electorate[17]+electorate[31]
            CP3[seats][2] = electorate[8]+electorate[21]+electorate[35]
            if incumbent[seats] == "ALP":
                oldval = CP3[seats][0]
                CP3[seats][0] +=sum(CP3[seats])*.01
                CP3[seats][1] *= (sum(CP3[seats])-CP3[seats][0])/(sum(CP3[seats])-oldval)
                CP3[seats][2] *= (sum(CP3[seats])-CP3[seats][0])/(sum(CP3[seats])-oldval)
            if incumbent[seats] == "LIB":
                oldval = CP3[seats][1]
                CP3[seats][1] += sum(CP3[seats]) * .01
                CP3[seats][0] *= (sum(CP3[seats])-CP3[seats][1])/(sum(CP3[seats]) - oldval)
                CP3[seats][2] *= (sum(CP3[seats])-CP3[seats][1])/(sum(CP3[seats]) - oldval)
            if CP3[seats][0] < CP3[seats][1] and CP3[seats][0] < CP3[seats][2] and nxtcheck[seats]=="Y":
               CP2[seats][0] = "LIB"
               CP2[seats][1] = CP3[seats][1]+electorate[1]+electorate[15]+electorate[29]
               CP2[seats][2] = "NXT/SA BEST"
               CP2[seats][3] = CP3[seats][2]+electorate[2]+electorate[14]+electorate[28]
               if incumbent[seats] == "IND":
                   seattotal[8] +=1
                   CP2[seats].append("IND HOLD ASSUMED")
               elif CP2[seats][1] > CP2[seats][3]:
                   seattotal[4]+=1
                   CP2[seats].append("LIB")
               else:
                   seattotal[6]+=1
                   CP2[seats].append("NXT/SA BEST")
            if CP3[seats][1] < CP3[seats][0] and CP3[seats][1] < CP3[seats][2] and nxtcheck[seats]== "Y":
               CP2[seats][0] = "ALP"
               CP2[seats][1] = electorate[0]+electorate[13]+electorate[27] +electorate[5]+electorate[18]+electorate[32]
               CP2[seats][2] = "NXT/SA BEST"
               CP2[seats][3] = CP3[seats][2] + electorate[6]+electorate[19]+electorate[33]
               if incumbent[seats] == "IND":
                   CP2[seats].append("IND HOLD ASSUMED")
                   seattotal[8] +=1
               elif CP2[seats][1] > CP2[seats][3]:
                   seattotal[2] += 1
                   CP2[seats].append("ALP")
               else:
                   seattotal[6] += 1
                   CP2[seats].append("NXT/SA BEST")
            if CP3[seats][2] < CP3[seats][1] and CP3[seats][0] > CP3[seats][2] or nxtcheck[seats]== "N":
               CP2[seats][0] = "ALP"
               CP2[seats][1] = CP3[seats][0] + electorate[9]+electorate[22]+electorate[36]
               CP2[seats][2] = "LIB"
               CP2[seats][3]=  CP3[seats][1]+electorate[10]+electorate[23]+electorate[37]
               if incumbent[seats] == "IND":
                   seattotal[8] +=1
                   CP2[seats].append("IND HOLD ASSUMED")
               elif CP2[seats][1] > CP2[seats][3]:
                   seattotal[2] += 1
                   CP2[seats].append("ALP")
               else:
                   seattotal[4] += 1
                   CP2[seats].append("LIB")
            votetotal = sum(PRIMARY[seats])
            PRIMARY[seats][0]=(PRIMARY[seats][0]/votetotal)*100
            PRIMARY[seats][1] = (PRIMARY[seats][1]/votetotal)*100
            PRIMARY[seats][2] = (PRIMARY[seats][2]/votetotal)*100
            PRIMARY[seats][3] = (PRIMARY[seats][3]/votetotal)*100
            PRIMARY[seats][4] = (PRIMARY[seats][4]/votetotal)*100
            votetotal = sum(CP3[seats])
            CP3[seats][1] = (CP3[seats][1]/votetotal)*100
            CP3[seats][0] = (CP3[seats][0]/votetotal)*100
            CP3[seats][2] = (CP3[seats][2]/votetotal)*100
            CP2[seats][1] = (CP2[seats][1]/votetotal)*100
            CP2[seats][3] = (CP2[seats][3]/votetotal)*100
            if seats == 46:
                break
        electorate = [0]*41
    electorate = [electorate[idx]+float(booth[idx+2]) for idx in range(41)]
    store = booth[0]
seats = 0

with open('saprojectionmorgan.csv', 'w') as myfile:



    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(["Seat","Primary Votes","ALP","LIB","NXT/SA BEST","GRN","OTHER","3CP","ALP","LIB","NXT/SA BEST","2PP","Party 1","Votes","Party 2", "Votes","Assumed Winner"])
    alpcount = 0
    libcount = 0
    nxtcount = 0
    while seats < 49:
        wr.writerow([str(SEATS[seats]),""]+PRIMARY[seats]+[""]+CP3[seats]+[""]+CP2[seats])
        avote = int(CP2[seats][1])
        print(avote)
        nvote = int(CP2[seats][3])
        if CP2[seats][2] == "LIB":
            lvote = int(CP2[seats][3])
        if CP2[seats][0] == "LIB":
            lvote = int(CP2[seats][1])
        if seattotal[2] < seattotal[4] and seattotal[2] < seattotal[6]:
            if CP2[seats][-1] == "ALP":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(((alpcount+1) % 3)*0.075+.05, math.trunc(alpcount/3)*0.075+.33,relative=True).set_color(Color(255,(75-avote)*7,(75-avote)*7)).set_size(20)
                alpcount+=1
            if CP2[seats][-1] == "LIB":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(math.trunc(libcount/3)*.075+.15, ((libcount+1)%3)*0.075+.05,relative=True).set_color(Color((75-lvote)*7,(75-lvote)*7,255)).set_size(20)
                libcount += 1
            if CP2[seats][-1] == "NXT/SA BEST":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(math.trunc(nxtcount/3)*.075+.15,.95-((nxtcount+1)%3)*0.075,relative=True).set_color(Color(250,140+(75-nvote)*4,(75-nvote)*7)).set_size(20)
                nxtcount += 1
            if CP2[seats][-1] == "IND HOLD ASSUMED":
                graph.add_node(id=(seats), value=SEATS[seats]+"*").set_position(((seattotal[2] + 2) % 3) * 0.075 + .05,math.trunc((seattotal[2]+1) / 3) * 0.075 + .33,relative=True).set_size(20)
        if seattotal[6] < seattotal[4] and seattotal[2] > seattotal[6]:
            if CP2[seats][-1] == "NXT/SA BEST":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(((alpcount + 1) % 3) * 0.075 + .05, math.trunc(alpcount / 3) * 0.075 + .33,relative=True).set_color(Color(250,140+(75-nvote)*4,(75-nvote)*7)).set_size(20)
                alpcount += 1
            if CP2[seats][-1] == "LIB":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(math.trunc(libcount / 3) * .075 + .15, ((libcount + 1) % 3) * 0.075 + .05, relative=True).set_color(Color((75-lvote)*7, (75-lvote) * 7, 255)).set_size(20)
                libcount += 1
            if CP2[seats][-1] == "ALP":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(math.trunc(nxtcount / 3) * .075 + .15, .95 - ((nxtcount + 1) % 3) * 0.075, relative=True).set_color(Color(255,(75-avote)*7,(75-avote)*7)).set_size(20)
                nxtcount += 1
            if CP2[seats][-1] == "IND HOLD ASSUMED":
                graph.add_node(id=(seats), value=SEATS[seats]+"*").set_position(((seattotal[6] + 2) % 3) * 0.075 + .05,math.trunc((seattotal[6]+1) / 3) * 0.075 + .33,relative=True).set_size(20)
        if seattotal[6] > seattotal[4] and seattotal[2] > seattotal[4]:
            if CP2[seats][-1] == "LIB":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(((alpcount + 1) % 3) * 0.075 + .05, math.trunc(alpcount / 3) * 0.075 + .33,relative=True).set_color(Color((75-lvote)*7, (75-lvote)*7, 255)).set_size(20)
                alpcount += 1
            if CP2[seats][-1] == "NXT/SA BEST":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(math.trunc(libcount / 3) * .075 + .15, ((libcount + 1) % 3) * 0.075 + .05, relative=True).set_color(Color(250,140+(75-nvote)*4,(75-nvote)*7)).set_size(20)
                libcount += 1
            if CP2[seats][-1] == "ALP":
                graph.add_node(id=(seats), value=SEATS[seats]).set_position(math.trunc(nxtcount / 3) * .075 + .15, .95 - ((nxtcount + 1) % 3) * 0.075, relative=True).set_color(Color(255,(75-avote)*7,(75-avote)*7)).set_size(20)
                nxtcount += 1
            if CP2[seats][-1] == "IND HOLD ASSUMED":
                graph.add_node(id=(seats), value=SEATS[seats]+"*").set_position(((seattotal[4] + 2) % 3) * 0.075 + .05,math.trunc((seattotal[4]+1) / 3) * 0.075 + .33,relative=True).set_size(20)
        seats += 1
    wr.writerow(seattotal)
deletenodes=[]
def seat_info(node):
    global deletenodes
    for i in deletenodes:
        graph.remove_node(i)
    seatid = node.id()
    deletenodes =[]
    graph.add_node("Primary Vote Share").set_position(0.33, 0.4, relative=True).set_color(Color.TRANSPARENT).set_value_style(color=Color.BLACK)
    deletenodes.append("Primary Vote Share")
    for i in range(len(PRIMARY[seatid])):
        if i == 0:
            graph.add_node(round(PRIMARY[seatid][i],3)).set_position(0.4+i*.1,0.4,relative=True).set_color(Color(255,0,0)).set_size(round(PRIMARY[seatid][i]))
            deletenodes.append((round(PRIMARY[seatid][i],3)))
        if i == 1:
            graph.add_node(round(PRIMARY[seatid][i],3)).set_position(0.4 + i * 0.1,0.4,relative=True).set_color(Color(0, 0, 255)).set_size(round(PRIMARY[seatid][i]))
            deletenodes.append((round(PRIMARY[seatid][i], 3)))
        if i == 2:
            graph.add_node(round(PRIMARY[seatid][i],3)).set_position(0.4 + i * 0.1,0.4,relative=True).set_color(Color(255, 140, 0)).set_size(round(PRIMARY[seatid][i]))
            deletenodes.append((round(PRIMARY[seatid][i], 3)))
        if i == 3:
            graph.add_node(round(PRIMARY[seatid][i],3)).set_position(0.4+i*0.1,0.4,relative=True).set_color(Color.GREEN).set_size(round(PRIMARY[seatid][i]))
            deletenodes.append((round(PRIMARY[seatid][i], 3)))
        if i == 4:
            graph.add_node(round(PRIMARY[seatid][i],3)).set_position(0.4 +i * 0.1,0.4,relative=True).set_size(round(PRIMARY[seatid][i]))
            deletenodes.append((round(PRIMARY[seatid][i], 3)))
    graph.add_node("2 Candidate Preferred Vote").set_position(0.4 , 0.6, relative=True).set_color(Color.TRANSPARENT).set_value_style(color=Color.BLACK)
    deletenodes.append("2 Candidate Preferred Vote")
    if CP2[seatid][2] == "NXT/SA BEST":
        graph.add_node(round(CP2[seatid][3], 3)).set_position(0.5, 0.6, relative=True).set_color(Color(255, 140, 0)).set_size(round(CP2[seatid][3]))
        deletenodes.append(round(CP2[seatid][3], 3))
    if CP2[seatid][2] == "LIB":
        graph.add_node(round(CP2[seatid][3], 3)).set_position(0.5 , 0.6, relative=True).set_color(Color(0, 0, 255)).set_size(round(CP2[seatid][3]))
        deletenodes.append(round(CP2[seatid][3], 3))
    if CP2[seatid][0] == "LIB":
        graph.add_node(round(CP2[seatid][1], 3)).set_position(0.6 , 0.6, relative=True).set_color(Color(0, 0, 255)).set_size(round(CP2[seatid][1]))
        deletenodes.append(round(CP2[seatid][1], 3))
    if CP2[seatid][0] == "ALP":
        graph.add_node(round(CP2[seatid][1], 3)).set_position(0.6 , 0.6, relative=True).set_color(Color(255, 0, 0)).set_size(round(CP2[seatid][1]))
        deletenodes.append(round(CP2[seatid][1], 3))
register_click_listener(seat_info)




