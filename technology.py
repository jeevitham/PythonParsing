#This class is used to store Technology data from foundry companies#
import os

class Technology :
    def __init__(self, lef, lib, sdc, drc , lvs, synthesis ):
        self.lef = lef
        self.lib = lib
        self.sdc = sdc
        self.drc = drc
        self.lvs = lvs
        self.synthesis = synthesis

    def generateFile(self, output,path):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with open(path , 'w+') as f:
            f.write(output)

    def generatePnR(self):
        output= "set rda_IASICt(ui_qxconf_file) {} \n " \
                "set rda_IASICt(flip_first) {1} \n " \
                "set rda_IASICt(double_back) {1} \n " \
                "set rda_IASICt(ui_timingcon_file) " +self.sdc + "\n" \
                "set rda_IASICt(assign_buffer) {0} \n" \
                "set rda_IASICt(ui_timelib,min) "+ self.lib + "\n" \
                "set rda_IASICt(ui_pg_connections) \n" \
                "set rda_IASICt(ui_gen_footprint) {1} \n" \
                "set rda_IASICt(ui_leffile) " + self.lef + "\n"

        self.generateFile(output,"output/pnr/dtmf.conf")

    def generateDRC(self,top, gds):
        output= "drc -top_cell " + top + " -gds " + gds + "  -deck " + self.drc +"\n"
        self.generateFile(output,"output/drc/drc.txt")

    def generateLVS(self,top, gds,sch):
        output= "lvs -top  "+ top + " -gds "+ gds + " -sch "+ sch  + " -deck " + self.lvs + "\n"
        self.generateFile(output,"output/lvs/lvs.txt")

    def generateLogicSynthesis(self):
        output= "include   /ee/setup/synopsys/synopsys_setup_ASIC018.inc \n" \
                "read -f verilog mux_using_assign.v \n " \
                "current_design = mux_using_assign \n " \
                "link \n "\
                "compile \n " \
                "create_schematic \n " \
                "plot -output mux_using_assign.ps \n " \
                "write -f verilog -o mux_using_assign.vs -hierarchy \n " \
                "exit \n "

        self.generateFile(output,"output/syn/syn.txt")

    def generatePower(self, gds,sch,pwr,defi):
        output =" power_grid -lef "+ self.lef + " -gds "+ gds + " -sch "+sch  + \
                " -dotlib "+ self.lib + " -vdd "+pwr + " -sdc " + self.sdc + " -def " +defi + "\n"
        self.generateFile(output,"output/pwr/IR/EM/pwr.txt")



