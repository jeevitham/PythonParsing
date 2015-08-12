import argparse
from technology import Technology

./code.py -t Technology (tsmc65 or umc45) -p Process(6m) -g layout_full_path -s sch_full_path -n top_cell_name -r RTL_verilog_full_path
-d DEF_full_path -v power_value

parser = argparse.ArgumentParser()
parser.add_argument("-t","Technology")
parser.add_argument('-p')
parser.add_argument('-g')
parser.add_argument('-s')
parser.add_argument('-n')
parser.add_argument('-r')
parser.add_argument('-d')
parser.add_argument('-v')

args = parser.parse_args()

if (args.)

technology= "tsmc45"
process= "6m"
#txt= open("input/"+ technology + "_" + process + ".txt")

with open("input/"+ technology + "_" + process + ".txt") as f:
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
    tech.generateDRC(top='TOP',gds='gds')
    tech.generateLVS(top='Bla', gds='gds',sch='sch')
