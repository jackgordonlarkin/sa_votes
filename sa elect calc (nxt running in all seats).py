import numpy as np
import csv
votes = open ('sabooths.csv','r')

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
while seats < 46:
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
            if CP3[seats][0] < CP3[seats][1] and CP3[seats][0] < CP3[seats][2]:
               CP2[seats][0] = "LIB"
               CP2[seats][1] = CP3[seats][1]+electorate[1]+electorate[15]+electorate[29]
               CP2[seats][2] = "NXT/SA BEST"
               CP2[seats][3] = CP3[seats][2]+electorate[2]+electorate[14]+electorate[28]
               if incumbent[seats] == "IND":
                   seattotal[8] +=1
                   CP2[seats].append("IND HOLD ASSUMED")
               elif CP2[seats][1] > CP2[seats][3]:
                   seattotal[4]+=1
               else:
                   seattotal[6]+=1
            if CP3[seats][1] < CP3[seats][0] and CP3[seats][1] < CP3[seats][2]:
               CP2[seats][0] = "ALP"
               CP2[seats][1] = electorate[0]+electorate[13]+electorate[27] +electorate[5]+electorate[18]+electorate[32]
               CP2[seats][2] = "NXT/SA BEST"
               CP2[seats][3] = CP3[seats][2] + electorate[6]+electorate[19]+electorate[33]
               if incumbent[seats] == "IND":
                   CP2[seats].append("IND HOLD ASSUMED")
                   seattotal[8] +=1
               elif CP2[seats][1] > CP2[seats][3]:
                   seattotal[2] += 1
               else:
                   seattotal[6] += 1
            if CP3[seats][2] < CP3[seats][1] and CP3[seats][0] > CP3[seats][2]:
               CP2[seats][0] = "ALP"
               CP2[seats][1] = CP3[seats][0] + electorate[9]+electorate[22]+electorate[36]
               CP2[seats][2] = "LIB"
               CP2[seats][3]=  CP3[seats][1]+electorate[10]+electorate[23]+electorate[37]
               if incumbent[seats] == "IND":
                   seattotal[8] +=1
                   CP2[seats].append("IND HOLD ASSUMED")
               elif CP2[seats][1] > CP2[seats][3]:
                   seattotal[2] += 1
               else:
                   seattotal[4] += 1
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
        electorate = [0]*41
    electorate = np.array(electorate) +np.array([float(i) for i in booth[2:43]])
    store = booth[0]
seats = 0
with open('saprojectionmorganallseats.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(["Seat","Primary Votes","ALP","LIB","NXT/SA BEST","GRN","OTHER","3CP","ALP","LIB","NXT/SA BEST","2PP","Party 1","Votes","Party 2", "Votes"])
    while seats < 49:
        wr.writerow([str(SEATS[seats]),""]+PRIMARY[seats]+[""]+CP3[seats]+[""]+CP2[seats])
        seats+=1
    wr.writerow(seattotal)
print("done")
