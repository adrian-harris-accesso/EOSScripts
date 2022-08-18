import csv

productMappingCSV = "CF.csv"

with open(productMappingCSV, newline='') as f:
    reader = csv.DictReader(f)

    with open('CA.csv','w') as CA:
        CAWriter = csv.writer(CA)
        counter = 0
        for row in reader:
            if counter < 1:
                CAWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Carowinds":
                CAWriter.writerow(row.values())
    CA.close()
    f.seek(0)

    with open('CP.csv','w') as CP:
        CPWriter = csv.writer(CP)
        counter = 0
        for row in reader:
            if counter < 1:
                CPWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Cedar Point":
                print(row)
                CPWriter.writerow(row.values())
    CP.close()
    f.seek(0)

    with open('CW.csv','w') as CW:
        CWWriter = csv.writer(CW)
        counter = 0
        for row in reader:
            if counter < 1:
                CWWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Canada's Wonderland":
                print(row)
                CWWriter.writerow(row.values())
    CW.close()
    f.seek(0)

    with open('DP.csv','w') as DP:
        DPWriter = csv.writer(DP)
        counter = 0
        for row in reader:
            if counter < 1:
                DPWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Dorney Park":
                print(row)
                DPWriter.writerow(row.values())
    DP.close()
    f.seek(0)

    with open('GA.csv','w') as GA:
        GAWriter = csv.writer(GA)
        counter = 0
        for row in reader:
            if counter < 1:
                GAWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Great America":
                print(row)
                GAWriter.writerow(row.values())
    GA.close()
    f.seek(0)

    with open('KBF.csv','w') as KBF:
        KBFWriter = csv.writer(KBF)
        counter = 0
        for row in reader:
            if counter < 1:
                KBFWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Knott's Berry Farm":
                print(row)
                KBFWriter.writerow(row.values())
    KBF.close()
    f.seek(0)

    with open('KD.csv','w') as KD:
        KDWriter = csv.writer(KD)
        counter = 0
        for row in reader:
            if counter < 1:
                KDWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Kings Dominion":
                print(row)
                KDWriter.writerow(row.values())
    KD.close()
    f.seek(0)

    with open('KI.csv','w') as KI:
        KIWriter = csv.writer(KI)
        counter = 0
        for row in reader:
            if counter < 1:
                KIWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Kings Island":
                print(row)
                KIWriter.writerow(row.values())
    KI.close()
    f.seek(0)

    with open('MA.csv','w') as MA:
        MAWriter = csv.writer(MA)
        counter = 0
        for row in reader:
            if counter < 1:
                MAWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Michigan's Adventure":
                print(row)
                MAWriter.writerow(row.values())
    MA.close()
    f.seek(0)

    with open('VF.csv','w') as VF:
        VFWriter = csv.writer(VF)
        counter = 0
        for row in reader:
            if counter < 1:
                VFWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Valleyfair":
                print(row)
                VFWriter.writerow(row.values())
    VF.close()
    f.seek(0)

    with open('WF.csv','w') as WF:
        WFWriter = csv.writer(WF)
        counter = 0
        for row in reader:
            if counter < 1:
                WFWriter.writerow(row.keys())
                counter += 1
            if row['name'] == "Worlds of Fun":
                print(row)
                WFWriter.writerow(row.values())
    WF.close()
    f.seek(0)

f.close()