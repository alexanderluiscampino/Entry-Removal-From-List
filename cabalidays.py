import csv
import os
import xlrd
import time

##################Filename definitions and subdirectories#######################
cwd = os.getcwd()
filesDir = "/cabalidays dm"
subdirEmail = "/email"
filenameUsernum = "/usernum_list.xlsx" #.xlsx
subdirUsernum = "/usernum_list"
filenameRemove = "/toRemove" #.txt
outputFilenameDM = "/DM"
outputFilenameGift = "/Gift"
domainsFile =  "/domainsRemove.txt"
outputDir = cwd + filesDir + "/output"
services = ["na", "eu", "br"] #.txt

##################### Create outputfoder, if this doesnt exist##################
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for service in services: #Iterates through BR, EU, and NA
    start = time.clock() #Measures time taken to create files
    ###########################Initiate Variables###############################
    dataDM={}
    dataDM["ID"] = []
    dataDM["email"]  = []
    dataDM["link1"]  = []
    dataDM["link2"]  = []
    dataDM["remove"]  = []

    dataGifts ={}
    dataGifts["PBuserNum"]  =[]
    dataGifts["CRMuserNum"]  =[]
    dataGifts["ID"]  =[]
    dataGifts["email"]  =[]
    dataGifts["remove"]  = []

    emailtoRemove = []

    #############################Remove domains################################
    header ='';
    domainRemoval ={"br":[],
                    "eu":[],
                    "na":[]
                    }

    with open(cwd + filesDir  + domainsFile) as domainFile:
        for line in domainFile:
            #if it is a header
            if line.split(':')[0] in ['br', 'na', 'eu'] :
                header = line.split(':')[0];
            #if it is a domain
            if line.split(':')[0] not in ['br', 'na', 'eu', ''] :
                domainRemoval[header].append(line.split('\n')[0])

    ##############################Collect emails to remove######################
    with open(cwd + filesDir + filenameRemove + ".txt") as toRemoveFile:
        for email in toRemoveFile:
            emailtoRemove.append(email.split('\n')[0])

    ##################Read DM File, collect Data, Write Output##################
    with open(cwd + filesDir + subdirEmail  + "/" + service + ".txt") as emailFile:
        with open(outputDir + outputFilenameDM + service.upper() + ".txt", "w+") as outputFile:
            i = 0
            for line in emailFile:
                dataDM["ID"].append(line.split(',')[1])
                dataDM["email"].append(line.split(',')[0])
                dataDM["link1"].append(line.split(',')[2])
                dataDM["link2"].append(line.split(',')[3])
                dataDM["remove"].append("False")
                email = dataDM["email"][i]
                #Remove emails that are on toRemove list
                if email in emailtoRemove:
                    dataDM["remove"][i]="True"
                #Remove bad domains
                for domain in domainRemoval[service]:
                    if email.find(domain)>0:
                        dataDM["remove"][i]="True"
                #Write Output File
                if  dataDM["remove"][i] == "False":
                    outputFile.write("%s,%s,%s,%s \n" % (dataDM["email"][i], dataDM["ID"][i], dataDM["link1"][i], dataDM["link2"][i]))
                i+=1

    #################Open Username List and Collect Data########################

    workbook = xlrd.open_workbook(cwd + filesDir + subdirUsernum + filenameUsernum)
    sheet = workbook.sheet_by_name(service.upper())
    header = True; #define boolean
    with open(outputDir + outputFilenameGift + service.upper() + ".txt", "w+") as outputFile:
        i = 0
        for rowx in range(sheet.nrows):
           cols = sheet.row_values(rowx)
           if header == False: #skip the first row, which is headers
                if service == "na": #because excel file has different config for services
                    dataGifts["CRMuserNum"].append(int(cols[0]))
                    dataGifts["PBuserNum"].append(int(cols[0]))
                    dataGifts["ID"].append(cols[2])
                    dataGifts["email"].append(cols[1])
                    dataGifts["remove"].append("False")
                else:
                    dataGifts["CRMuserNum"].append(int(cols[0]))
                    dataGifts["PBuserNum"].append(int(cols[1]))
                    dataGifts["ID"].append(cols[2])
                    dataGifts["email"].append(cols[4])
                    dataGifts["remove"].append("False")

                email = dataGifts["email"][i]
                #Remove emails that are on toRemove list
                if email in emailtoRemove:
                    dataGifts["remove"][i]="True"
                #Remove bad domains
                for domain in domainRemoval[service]:
                    if email.find(domain)>0:
                        dataGifts["remove"][i]="True"
                #Write Output File
                if  dataGifts["remove"][i] == "False":
                    outputFile.write("%d\n" % (dataGifts["PBuserNum"][i]))
                i+=1

           header = False
    ######################### Print Success Messages ##########################

    print("File %s and %s Created Successfully. Time Taken: %ds" %(outputFilenameGift
     + service.upper(), outputFilenameDM + service.upper(), int(time.clock() - start)))

print("\n\n All Files Processed and Created Successfully\n\n")
