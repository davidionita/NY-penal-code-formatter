import json

jail = {
        "A-I Felony" : "15 Years-Life", 
        "A-II Felony" : "3 Years-Life", 
        "B Felony" : "9-25 Years", 
        "C Felony" : "6-15 Years", 
        "D Felony" : "0-7 Years", 
        "E Felony" : "0-4 Years",
        "B Violent Felony" : "5-25 Years",
        "C Violent Felony" : "3.5-15 Years",
        "D Violent Felony" : "2-7 Years",
        "E Violent Felony" : "1.5-4 Years",
        "A Misdemeanor" : "0-1 Years",
        "B Misdemeanor" : "0-3 Months",
        "Unclassified Misdemeanor" : "0-1 Years",
        "Violation" : "0-15 Days",
        "Traffic Infraction" : "0 Years",
        "Warning" : "0 Years"
}

bond = {
        "A-I Felony" : 100000, 
        "A-II Felony" : 50000, 
        "B Felony" : 30000, 
        "C Felony" : 15000, 
        "D Felony" : 5000, 
        "E Felony" : 5000,
        "B Violent Felony" : 5000,
        "C Violent Felony" : 5000,
        "D Violent Felony" : 5000,
        "E Violent Felony" : 5000,
        "A Misdemeanor" : 1000,
        "B Misdemeanor" : 500,
        "Unclassified Misdemeanor" : 1000,
        "Violation" : 250,
        "Traffic Infraction" : 0,
        "Warning" : 0
}

f = open("traffic.json", "r")
data = f.readline()
array = json.loads(data)
criminal = []

c = 0

for i in range(0, len(array)):
    if i % 3 == 0:
        criminal.append({})
        criminal[c]["code"] = "§ " + array[i][array[i].find(">")+1 : -4] + "." + array[i+1]
        criminal[c]["type"] = "Traffic Infraction"
        criminal[c]["title"] = array[i+2]

        criminal[c]["bondType"] = "Citation Release"

        criminal[c]["jailTime"] = jail["Traffic Infraction"]
        criminal[c]["bondAmount"] = bond["Traffic Infraction"]

        c -=- 1


nf = open("traffic-formatted.json", "w")
nf.write(json.dumps(criminal))
