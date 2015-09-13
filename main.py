#Jeevitha Muppala, Stud ID: 87833 ,CEN 900 2 Computer Engineering

from technology import Technology
import argparse

#list of arguments

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store',dest="tech")
parser.add_argument('-p', action='store',dest="process")
parser.add_argument('-g', action='store',dest="layout")
parser.add_argument('-s', action='store',dest="sch")
parser.add_argument('-n', action='store',dest="top")
parser.add_argument('-r', action='store',dest="rtl")
parser.add_argument('-d', action='store',dest="defpath")
parser.add_argument('-v', action='store',dest="power")

#parser.add_argument('-h', '--help', type=str)

args = parser.parse_args()
print(args.tech)
print(args.process)
print(args.layout)
print(args.sch)
print(args.top)
print(args.rtl)
print(args.defpath)
print(args.power)

with open("input/"+ args.tech + "_" + args.process + ".txt") as f:
    for line in f:
        line= line.rstrip('\n')
        data= line.split(":")
        if (data[0] == "lef"):
            lef=data[1]
        elif (data[0] == "lib"):
            lib=data[1]
        elif (data[0] == "sdc"):
            sdc=data[1]
        elif (data[0] == "drc"):
            drc=data[1]
        elif (data[0] == "lvs"):
            lvs=data[1]
        elif (data[0] == "synthesis"):
            synthesis=data[1]

    tech = Technology(lef,lib,sdc,drc,lvs,synthesis)
    tech.generatePnR()
    tech.generateLogicSynthesis()
    tech.generateDRC(top=args.top,gds=args.layout)
    tech.generateLVS(top=args.top, gds='gds',sch=args.sch)
    tech.generatePower(gds=args.layout,sch=args.sch,pwr=args.power,defi=args.defpath)
