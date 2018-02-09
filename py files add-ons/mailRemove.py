import csv
import os
import xlrd
import time

cwd = os.getcwd()
filesDir = "/files"
subdirEmail = "/email"
filenameUsernum = "/usernum_list.xlsx" #.xlsx
subdirUsernum = "/usernum_list"
filenameRemove = "/toRemove" #.txt
outputFilenameDM = "/DM"
outputFilenameGift = "/Gift"
domainsFile =  "/domainsRemove.txt"
outputDir = cwd + filesDir + "/output"
services = ["na", "eu", "br"] #.txt

with open(outputDir + outputFilenameDM + services[1].upper() + ".txt") as emailFile:
    with open("emailRemoveused.txt", "w+") as outputFile:
        for line in emailFile:
            outputFile.write("%s\n" % (line.split(',')[0]))
