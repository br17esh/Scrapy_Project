import requests
import re
import os
from bs4 import BeautifulSoup
from pprint import pprint
import scrapy
import mysql.connector
import pymysql
from scrapy.http import Request

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="djangotest",
  port = 3308
)

mycursor = mydb.cursor()

dirlist = sorted(os.listdir("/opt/lampp/htdocs/ASTROSAT_SAMPLE_DATA/"))

#pprint(dirlist)

path = []

ndfcount = 0
dphcount = 0
countrate = 0
housekeep = 0
ndfcount1 = 0
dphcount1 = 0
countrate1 = 0
housekeep1 = 0
id = 0
obs = ""

for i in range(0, len(dirlist)):
    path.append('http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[i] + '/index.html')
    print(path[i])

class Spiderman(scrapy.Spider):
    name = 'spidey'
    start_urls = path
    global id
    id = 0

    def parse(self, response):
        b = response.xpath("//li/b/text()").extract()
        obs = response.xpath("//li/text()").extract()
        tabvar = response.xpath("//table/tr/td/text()").extract()
        mode = response.xpath("//table/tr/th/text()").extract()
        global id
        pprint(path[id])
        pprint(len(path[id]))
        fol = path[id].split('/')
        UnID = fol[4]+obs[4]




        if (len(path[id]) == 90):
            pprint(path[id])

            #####################################################################################################################
            if(b[5]!="exposure"):
                sql = "INSERT INTO mg_iucaaapp_summary (folder, Observer, UID) VALUES ('"+fol[4]+"','"+obs[6]+"','"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()
            else:
                sql = "INSERT INTO mg_iucaaapp_summary (folder, Observer, UID) VALUES ('" + fol[4] + "','" + obs[
                    7] + "','" + UnID + "')"
                mycursor.execute(sql)
                mydb.commit()

            ##########################################################################################################################################################
            if(mode[3] == "Mode M9"):
                sql = "INSERT INTO mg_dqrreport_datainteg (UID,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP) VALUES ('"+UnID+"', '" + \
                tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[27] + "','" + tabvar[
                    28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + tabvar[
                    35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + tabvar[
                    42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + tabvar[
                    48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + tabvar[
                    55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + tabvar[
                    62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + tabvar[
                    68] + "')"
                mycursor.execute(sql)
                mydb.commit()

            if(mode[3] == "Mode M0"):
                sql = "INSERT INTO mg_dqrreport_datainteg (UID,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP) VALUES ('"+UnID+"', '" + \
                      tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[
                          27] + "','" + tabvar[
                          28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + \
                      tabvar[
                          35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + \
                      tabvar[
                          42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + \
                      tabvar[
                          48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + \
                      tabvar[
                          55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + \
                      tabvar[
                          62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + \
                      tabvar[
                          68] + "')"
                mycursor.execute(sql)
                mydb.commit()

            if(mode[3] == "Mode SS"):
                sql = "INSERT INTO mg_dqrreport_datainteg (UID,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP) VALUES ('"+UnID+"', '" + \
                      tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[
                          27] + "','" + tabvar[
                          28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + \
                      tabvar[
                          35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + \
                      tabvar[
                          42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + \
                      tabvar[
                          48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + \
                      tabvar[
                          55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + \
                      tabvar[
                          62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + \
                      tabvar[
                          68] + "')"
                mycursor.execute(sql)
                mydb.commit()
            #######################################################################################################################################
            # sql = "INSERT INTO mg_dqrreport_datainteg (UID,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP) VALUES ('"+UnID+"', '" + \
            # tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[27] + "','" + tabvar[
            #     28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + tabvar[
            #     35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + tabvar[
            #     42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + tabvar[
            #     48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + tabvar[
            #     55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + tabvar[
            #     62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + tabvar[
            #     68] + "')"
            # mycursor.execute(sql)
            # mydb.commit()
            ##############################################################################################################################################
            sql = "INSERT INTO mg_dqrreport_pixelprop (UID,PP_QA1_DID,PP_QA1_PID,PP_QA1_CNT,PP_QA1_SG,PP_QA2_DID,PP_QA2_PID,PP_QA2_CNT,PP_QA2_SG,PP_QA3_DID,PP_QA3_PID,PP_QA3_CNT,PP_QA3_SG,PP_QB1_DID,PP_QB1_PID,PP_QB1_CNT,PP_QB1_SG,PP_QB2_DID,PP_QB2_PID,PP_QB2_CNT,PP_QB2_SG,PP_QB3_DID,PP_QB3_PID,PP_QB3_CNT,PP_QB3_SG,PP_QC1_DID,PP_QC1_PID,PP_QC1_CNT,PP_QC1_SG,PP_QC2_DID,PP_QC2_PID,PP_QC2_CNT,PP_QC2_SG,PP_QC3_DID,PP_QC3_PID,PP_QC3_CNT,PP_QC3_SG,PP_QD1_DID,PP_QD1_PID,PP_QD1_CNT,PP_QD1_SG,PP_QD2_DID,PP_QD2_PID,PP_QD2_CNT,PP_QD2_SG,PP_QD3_DID,PP_QD3_PID,PP_QD3_CNT,PP_QD3_SG) VALUES ('"+UnID+"','"+tabvar[109]+"','"+tabvar[110]+"','"+tabvar[111]+"','"+tabvar[112]+"','"+tabvar[116]+"','"+tabvar[117]+"','"+tabvar[118]+"','"+tabvar[119]+"','"+tabvar[123]+"','"+tabvar[124]+"','"+tabvar[125]+"','"+tabvar[126]+"','"+tabvar[130]+"','"+tabvar[131]+"','"+tabvar[132]+"','"+tabvar[133]+"','"+tabvar[137]+"','"+tabvar[138]+"','"+tabvar[139]+"','"+tabvar[140]+"','"+tabvar[144]+"','"+tabvar[145]+"','"+tabvar[146]+"','"+tabvar[147]+"','"+tabvar[151]+"','"+tabvar[152]+"','"+tabvar[153]+"','"+tabvar[154]+"','"+tabvar[158]+"','"+tabvar[159]+"','"+tabvar[160]+"','"+tabvar[161]+"','"+tabvar[165]+"','"+tabvar[166]+"','"+tabvar[167]+"','"+tabvar[168]+"','"+tabvar[172]+"','"+tabvar[173]+"','"+tabvar[174]+"','"+tabvar[175]+"','"+tabvar[179]+"','"+tabvar[180]+"','"+tabvar[181]+"','"+tabvar[182]+"','"+tabvar[186]+"','"+tabvar[187]+"','"+tabvar[188]+"','"+tabvar[189]+"')"
            mycursor.execute(sql)
            mydb.commit()
            #################################################################################################################################################
            ##############################################################################################################################################
            sql = "INSERT INTO mg_dqrreport_quadprop (UID,QP_QA1_MN,QP_QA1_MD,QP_QA1_SG,QP_QA2_MN,QP_QA2_MD,QP_QA2_SG,QP_QA3_MN,QP_QA3_MD,QP_QA3_SG,QP_QB1_MN,QP_QB1_MD,QP_QB1_SG,QP_QB2_MN,QP_QB2_MD,QP_QB2_SG,QP_QB3_MN,QP_QB3_MD,QP_QB3_SG,QP_QC1_MN,QP_QC1_MD,QP_QC1_SG,QP_QC2_MN,QP_QC2_MD,QP_QC2_SG,QP_QC3_MN,QP_QC3_MD,QP_QC3_SG,QP_QD1_MN,QP_QD1_MD,QP_QD1_SG,QP_QD2_MN,QP_QD2_MD,QP_QD2_SG,QP_QD3_MN,QP_QD3_MD,QP_QD3_SG) VALUES ('"+UnID+"','"+tabvar[113]+"','"+tabvar[114]+"','"+tabvar[115]+"','"+tabvar[120]+"','"+tabvar[121]+"','"+tabvar[122]+"','"+tabvar[127]+"','"+tabvar[128]+"','"+tabvar[129]+"','"+tabvar[134]+"','"+tabvar[135]+"','"+tabvar[136]+"','"+tabvar[141]+"','"+tabvar[142]+"','"+tabvar[143]+"','"+tabvar[148]+"','"+tabvar[149]+"','"+tabvar[150]+"','"+tabvar[155]+"','"+tabvar[156]+"','"+tabvar[157]+"','"+tabvar[162]+"','"+tabvar[163]+"','"+tabvar[164]+"','"+tabvar[169]+"','"+tabvar[170]+"','"+tabvar[171]+"','"+tabvar[176]+"','"+tabvar[177]+"','"+tabvar[178]+"','"+tabvar[183]+"','"+tabvar[184]+"','"+tabvar[185]+"','"+tabvar[190]+"','"+tabvar[191]+"','"+tabvar[192]+"')"
            mycursor.execute(sql)
            mydb.commit()
            #################################################################################################################################################
            global housekeep1

            hk1 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_CZT_Counter.png'
            hk2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hkDVDD.png'
            hk3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hkTemperature1.png'
            hk4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hkVetoHV_Monitor.png'
            hk5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hkVetoLLD.png'
            hk6 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_AlphaCounter.png'
            hk7 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_CPM_Rate.png'
            hk8 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_CZT_Counter.png'
            hk9 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_POS_2DOT5V_Monitor.png'
            hk10 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_POS_5V_Monitor.png'
            hk11 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_ROLL_ROT.png'
            hk12 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_Roll_DEC.png'
            hk13 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_Roll_RA.png'
            hk14 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep1] + '/hk_VetoCounter.png'


            sql = "INSERT INTO mg_dqrreport_housekeeping (UID,plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9,plot10,plot11,plot12,plot13,plot14) VALUES ('"+UnID+"','"+hk1+"','"+hk2+"','"+hk3+"','"+hk4+"','"+hk5+"','"+hk6+"','"+hk7+"','"+hk8+"','"+hk9+"','"+hk10+"','"+hk11+"','"+hk12+"','"+hk13+"','"+hk14+"')"
            mycursor.execute(sql)
            mydb.commit()

            housekeep1 +=1

            ##################################################################################################################################################
            global countrate1

            crp1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/countrate1_histogram.png'
            cri1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/imageFULL_DPI.png'
            crp2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/countrate1_lightcurve.png'
            cri2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/imageFULL_DPI.png'
            crp3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/countrate1_modulerates.Q0.png'
            cri3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/imageQ0.png'
            crp4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/countrate1_modulerates.Q1.png'
            cri4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/imageQ1.png'
            crp5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/countrate1_modulerates.Q2.png'
            cri5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/imageQ2.png'
            crp6 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/countrate1_modulerates.Q3.png'
            cri6 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate1] + '/imageQ3.png'

            sql = "INSERT INTO mg_dqrreport_countrate (UID,crplot1,crimg1,crplot2,crimg2,crplot3,crimg3,crplot4,crimg4,crplot5,crimg5,crplot6,crimg6) VALUES ('"+UnID+"', '"+crp1+"', '"+cri1+"', '"+crp2+"', '"+cri2+"', '"+crp3+"', '"+cri3+"', '"+crp4+"', '"+cri4+"', '"+crp5+"', '"+cri5+"', '"+crp6+"', '"+cri6+"')"
            mycursor.execute(sql)
            mydb.commit()
            countrate1 += 1

            #################################################################################################################################################

            global dphcount1

            dphimg0 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount1] + '/dph.Q0.png'
            dphimg1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount1] + '/dph.Q1.png'
            dphimg2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount1] + '/dph.Q2.png'
            dphimg3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount1] + '/dph.Q3.png'

            # pprint(dphimg0)
            # pprint(dphimg1)
            # pprint(dphimg2)
            # pprint(dphimg3)

            sql = "INSERT INTO mg_dqrreport_dph (quadA,quadB,quadC,quadD,UID) VALUES ('"+dphimg0+"', '"+dphimg1+"', '"+dphimg2+"', '"+dphimg3+"', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

            dphcount1 += 1


            ######################################################################################################################################

            global ndfcount1
            noisyimg0 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount1] + '/noisytime.Q0.png'
            noisyimg1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount1] + '/noisytime.Q1.png'
            noisyimg2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount1] + '/noisytime.Q2.png'
            noisyimg3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount1] + '/noisytime.Q3.png'

            sql = "INSERT INTO mg_dqrreport_noisefrag (UID, QA_S1B, QA_B0C, QA_B2KC, QA_HRB, QA_NTT, QA_NDT, QA_MLC, QB_S1B, QB_B0C, QB_B2KC, QB_HRB, QB_NTT, QB_NDT, QB_MLC, QC_S1B, QC_B0C, QC_B2KC, QC_HRB, QC_NTT, QC_NDT, QC_MLC, QD_S1B, QD_B0C, QD_B2KC, QD_HRB, QD_NTT, QD_NDT, QD_MLC) VALUES ('"+UnID+"', '" + tabvar[85] + "', '" + tabvar[86] + "', '" + tabvar[87] + "', '" + tabvar[88] + "', '" + tabvar[89] + "', '" + tabvar[90] + "', '" + noisyimg0 + "', '" + tabvar[91] + "', '" + tabvar[92] + "', '" + tabvar[93] + "', '" + tabvar[94] + "', '" + tabvar[95] + "', '" + tabvar[96] + "', '" + noisyimg1 + "', '" + tabvar[97] + "', '" + tabvar[98] + "', '" + tabvar[99] + "', '" + tabvar[100] + "', '" + tabvar[101] + "', '" + tabvar[102] + "', '" + noisyimg2 + "', '" + tabvar[103] + "', '" + tabvar[104] + "', '" + tabvar[105] + "', '" + tabvar[106] + "', '" + tabvar[107] + "', '" + tabvar[108] + "', '" + noisyimg3 +"')"
            #
            #
            mycursor.execute(sql)
            mydb.commit()

            ndfcount1 += 1

            ###########################################################################################################################################

            sql = "INSERT INTO mg_dqrreport_dqrstats (filename_OF,filename_FF,size_bytes_OF,size_bytes_FF,size_OF,size_FF,events_quadA_OF,events_quadA_FF,events_quadB_OF,events_quadB_FF, events_quadC_OF, events_quadC_FF, events_quadD_OF, events_quadD_FF, UID) VALUES('"+tabvar[1]+"', '"+tabvar[2]+"', '"+tabvar[4]+"', '"+tabvar[5]+"','"+tabvar[7]+"', '"+tabvar[8]+"', '"+tabvar[10]+"', '"+tabvar[11]+"', '"+tabvar[13]+"', '"+tabvar[14]+"', '"+tabvar[16]+"', '"+tabvar[17]+"', '"+tabvar[19]+"', '"+tabvar[20]+"', '"+UnID+"')"

            mycursor.execute(sql)
            mydb.commit()
            ###########################################################################################################################################
            sql = "INSERT INTO mg_dqrreport_datasat (UID,QA_TS,QA_SS,QA_SP,QB_TS,QB_SS,QB_SP,QC_TS,QC_SS,QC_SP,QD_TS,QD_SS,QD_SP) VALUES ('"+UnID+"', '" + \
            tabvar[70] + "','" + tabvar[71] + "','" + tabvar[72] + "','" + tabvar[74] + "','" + tabvar[75] + "','" + tabvar[
                76] + "','" + tabvar[78] + "','" + tabvar[79] + "','" + tabvar[80] + "','" + tabvar[82] + "','" + tabvar[
                83] + "','" + tabvar[84] + "')"
            mycursor.execute(sql)
            mydb.commit()
            ########################################################################################################################################
            if b[0] != "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES (' ', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                          5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] != "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', ' ', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                          5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()


            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] != "date-end" and b[3] == "time-end" and b[
                4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                    b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', ' ', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                          5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] != "time-end" and b[
                4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                    b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', ' ', '" + obs[4] + "', '" + obs[
                          5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
                4] != "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                    b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', ' ', '" + obs[
                          5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
                4] == "obs_id" and b[5] == "sourceid" and b[6] == "observer" and b[7] == "ra_pnt" and \
                    b[8] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', 'NA', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
                4] == "obs_id" and b[5] == "exposure" and b[6] != "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                    b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', ' ', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
                4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] != "observer" and b[8] == "ra_pnt" and \
                    b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', ' ', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
                4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] != "ra_pnt" and \
                    b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', ' ', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
                4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                    b[9] != "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', ' ', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
                4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + \
                      obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                          5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
                mycursor.execute(sql)
                mydb.commit()

            if b[0] != "date-obs" and b[1] != "time-obs" and b[2] != "date-end" and b[3] != "time-end" and b[
                4] != "obs_id" and b[5] != "exposure" and b[6] != "sourceid" and b[7] != "observer" and b[8] != "ra_pnt" and b[9] != "dec_pnt":
                sql = "INSERT INTO mg_dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')"
                mycursor.execute(sql)
                mydb.commit()
            ###################################################################################################################################


        #####################################################################################################################
        if(b[5]!="exposure"):
            sql = "INSERT INTO iucaaapp_summary (folder, Observer, UID) VALUES ('"+fol[4]+"','"+obs[6]+"','"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()
        else:
            sql = "INSERT INTO iucaaapp_summary (folder, Observer, UID) VALUES ('" + fol[4] + "','" + obs[
                7] + "','" + UnID + "')"
            mycursor.execute(sql)
            mydb.commit()

        ##########################################################################################################################################################
        if(mode[3] == "Mode M9"):
            sql = "INSERT INTO dqrreport_datainteg (UID,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP) VALUES ('"+UnID+"', '" + \
            tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[27] + "','" + tabvar[
                28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + tabvar[
                35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + tabvar[
                42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + tabvar[
                48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + tabvar[
                55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + tabvar[
                62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + tabvar[
                68] + "')"
            mycursor.execute(sql)
            mydb.commit()

        if(mode[3] == "Mode M0"):
            sql = "INSERT INTO dqrreport_datainteg (UID,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP) VALUES ('"+UnID+"', '" + \
                  tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[
                      27] + "','" + tabvar[
                      28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + \
                  tabvar[
                      35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + \
                  tabvar[
                      42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + \
                  tabvar[
                      48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + \
                  tabvar[
                      55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + \
                  tabvar[
                      62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + \
                  tabvar[
                      68] + "')"
            mycursor.execute(sql)
            mydb.commit()

        if(mode[3] == "Mode SS"):
            sql = "INSERT INTO dqrreport_datainteg (UID,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP) VALUES ('"+UnID+"', '" + \
                  tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[
                      27] + "','" + tabvar[
                      28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + \
                  tabvar[
                      35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + \
                  tabvar[
                      42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + \
                  tabvar[
                      48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + \
                  tabvar[
                      55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + \
                  tabvar[
                      62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + \
                  tabvar[
                      68] + "')"
            mycursor.execute(sql)
            mydb.commit()
        #######################################################################################################################################
        # sql = "INSERT INTO dqrreport_datainteg (UID,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP) VALUES ('"+UnID+"', '" + \
        # tabvar[22] + "','" + tabvar[23] + "','" + tabvar[24] + "','" + tabvar[26] + "','" + tabvar[27] + "','" + tabvar[
        #     28] + "','" + tabvar[30] + "','" + tabvar[31] + "','" + tabvar[32] + "','" + tabvar[34] + "','" + tabvar[
        #     35] + "','" + tabvar[36] + "','" + tabvar[38] + "','" + tabvar[39] + "','" + tabvar[40] + "','" + tabvar[
        #     42] + "','" + tabvar[43] + "','" + tabvar[44] + "','" + tabvar[46] + "','" + tabvar[47] + "','" + tabvar[
        #     48] + "','" + tabvar[50] + "','" + tabvar[51] + "','" + tabvar[52] + "','" + tabvar[54] + "','" + tabvar[
        #     55] + "','" + tabvar[56] + "','" + tabvar[58] + "','" + tabvar[59] + "','" + tabvar[60] + "','" + tabvar[
        #     62] + "','" + tabvar[63] + "','" + tabvar[64] + "','" + tabvar[66] + "','" + tabvar[67] + "','" + tabvar[
        #     68] + "')"
        # mycursor.execute(sql)
        # mydb.commit()
        ##############################################################################################################################################
        sql = "INSERT INTO dqrreport_pixelprop (UID,PP_QA1_DID,PP_QA1_PID,PP_QA1_CNT,PP_QA1_SG,PP_QA2_DID,PP_QA2_PID,PP_QA2_CNT,PP_QA2_SG,PP_QA3_DID,PP_QA3_PID,PP_QA3_CNT,PP_QA3_SG,PP_QB1_DID,PP_QB1_PID,PP_QB1_CNT,PP_QB1_SG,PP_QB2_DID,PP_QB2_PID,PP_QB2_CNT,PP_QB2_SG,PP_QB3_DID,PP_QB3_PID,PP_QB3_CNT,PP_QB3_SG,PP_QC1_DID,PP_QC1_PID,PP_QC1_CNT,PP_QC1_SG,PP_QC2_DID,PP_QC2_PID,PP_QC2_CNT,PP_QC2_SG,PP_QC3_DID,PP_QC3_PID,PP_QC3_CNT,PP_QC3_SG,PP_QD1_DID,PP_QD1_PID,PP_QD1_CNT,PP_QD1_SG,PP_QD2_DID,PP_QD2_PID,PP_QD2_CNT,PP_QD2_SG,PP_QD3_DID,PP_QD3_PID,PP_QD3_CNT,PP_QD3_SG) VALUES ('"+UnID+"','"+tabvar[109]+"','"+tabvar[110]+"','"+tabvar[111]+"','"+tabvar[112]+"','"+tabvar[116]+"','"+tabvar[117]+"','"+tabvar[118]+"','"+tabvar[119]+"','"+tabvar[123]+"','"+tabvar[124]+"','"+tabvar[125]+"','"+tabvar[126]+"','"+tabvar[130]+"','"+tabvar[131]+"','"+tabvar[132]+"','"+tabvar[133]+"','"+tabvar[137]+"','"+tabvar[138]+"','"+tabvar[139]+"','"+tabvar[140]+"','"+tabvar[144]+"','"+tabvar[145]+"','"+tabvar[146]+"','"+tabvar[147]+"','"+tabvar[151]+"','"+tabvar[152]+"','"+tabvar[153]+"','"+tabvar[154]+"','"+tabvar[158]+"','"+tabvar[159]+"','"+tabvar[160]+"','"+tabvar[161]+"','"+tabvar[165]+"','"+tabvar[166]+"','"+tabvar[167]+"','"+tabvar[168]+"','"+tabvar[172]+"','"+tabvar[173]+"','"+tabvar[174]+"','"+tabvar[175]+"','"+tabvar[179]+"','"+tabvar[180]+"','"+tabvar[181]+"','"+tabvar[182]+"','"+tabvar[186]+"','"+tabvar[187]+"','"+tabvar[188]+"','"+tabvar[189]+"')"
        mycursor.execute(sql)
        mydb.commit()
        #################################################################################################################################################
        ##############################################################################################################################################
        sql = "INSERT INTO dqrreport_quadprop (UID,QP_QA1_MN,QP_QA1_MD,QP_QA1_SG,QP_QA2_MN,QP_QA2_MD,QP_QA2_SG,QP_QA3_MN,QP_QA3_MD,QP_QA3_SG,QP_QB1_MN,QP_QB1_MD,QP_QB1_SG,QP_QB2_MN,QP_QB2_MD,QP_QB2_SG,QP_QB3_MN,QP_QB3_MD,QP_QB3_SG,QP_QC1_MN,QP_QC1_MD,QP_QC1_SG,QP_QC2_MN,QP_QC2_MD,QP_QC2_SG,QP_QC3_MN,QP_QC3_MD,QP_QC3_SG,QP_QD1_MN,QP_QD1_MD,QP_QD1_SG,QP_QD2_MN,QP_QD2_MD,QP_QD2_SG,QP_QD3_MN,QP_QD3_MD,QP_QD3_SG) VALUES ('"+UnID+"','"+tabvar[113]+"','"+tabvar[114]+"','"+tabvar[115]+"','"+tabvar[120]+"','"+tabvar[121]+"','"+tabvar[122]+"','"+tabvar[127]+"','"+tabvar[128]+"','"+tabvar[129]+"','"+tabvar[134]+"','"+tabvar[135]+"','"+tabvar[136]+"','"+tabvar[141]+"','"+tabvar[142]+"','"+tabvar[143]+"','"+tabvar[148]+"','"+tabvar[149]+"','"+tabvar[150]+"','"+tabvar[155]+"','"+tabvar[156]+"','"+tabvar[157]+"','"+tabvar[162]+"','"+tabvar[163]+"','"+tabvar[164]+"','"+tabvar[169]+"','"+tabvar[170]+"','"+tabvar[171]+"','"+tabvar[176]+"','"+tabvar[177]+"','"+tabvar[178]+"','"+tabvar[183]+"','"+tabvar[184]+"','"+tabvar[185]+"','"+tabvar[190]+"','"+tabvar[191]+"','"+tabvar[192]+"')"
        mycursor.execute(sql)
        mydb.commit()
        #################################################################################################################################################
        global housekeep

        hk1 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_CZT_Counter.png'
        hk2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkDVDD.png'
        hk3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkTemperature1.png'
        hk4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkVetoHV_Monitor.png'
        hk5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkVetoLLD.png'
        hk6 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_AlphaCounter.png'
        hk7 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_CPM_Rate.png'
        hk8 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_CZT_Counter.png'
        hk9 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_POS_2DOT5V_Monitor.png'
        hk10 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_POS_5V_Monitor.png'
        hk11 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_ROLL_ROT.png'
        hk12 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_Roll_DEC.png'
        hk13 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_Roll_RA.png'
        hk14 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_VetoCounter.png'


        sql = "INSERT INTO dqrreport_housekeeping (UID,plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9,plot10,plot11,plot12,plot13,plot14) VALUES ('"+UnID+"','"+hk1+"','"+hk2+"','"+hk3+"','"+hk4+"','"+hk5+"','"+hk6+"','"+hk7+"','"+hk8+"','"+hk9+"','"+hk10+"','"+hk11+"','"+hk12+"','"+hk13+"','"+hk14+"')"
        mycursor.execute(sql)
        mydb.commit()

        housekeep +=1

        ##################################################################################################################################################
        global countrate

        crp1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_histogram.png'
        cri1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageFULL_DPI.png'
        crp2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_lightcurve.png'
        cri2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageFULL_DPI.png'
        crp3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q0.png'
        cri3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ0.png'
        crp4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q1.png'
        cri4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ1.png'
        crp5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q2.png'
        cri5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ2.png'
        crp6 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q3.png'
        cri6 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ3.png'

        sql = "INSERT INTO dqrreport_countrate (UID,crplot1,crimg1,crplot2,crimg2,crplot3,crimg3,crplot4,crimg4,crplot5,crimg5,crplot6,crimg6) VALUES ('"+UnID+"', '"+crp1+"', '"+cri1+"', '"+crp2+"', '"+cri2+"', '"+crp3+"', '"+cri3+"', '"+crp4+"', '"+cri4+"', '"+crp5+"', '"+cri5+"', '"+crp6+"', '"+cri6+"')"
        mycursor.execute(sql)
        mydb.commit()
        countrate += 1

        #################################################################################################################################################

        global dphcount

        dphimg0 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q0.png'
        dphimg1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q1.png'
        dphimg2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q2.png'
        dphimg3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q3.png'

        # pprint(dphimg0)
        # pprint(dphimg1)
        # pprint(dphimg2)
        # pprint(dphimg3)

        sql = "INSERT INTO dqrreport_dph (quadA,quadB,quadC,quadD,UID) VALUES ('"+dphimg0+"', '"+dphimg1+"', '"+dphimg2+"', '"+dphimg3+"', '"+UnID+"')"
        mycursor.execute(sql)
        mydb.commit()

        dphcount += 1


        ######################################################################################################################################

        global ndfcount
        noisyimg0 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q0.png'
        noisyimg1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q1.png'
        noisyimg2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q2.png'
        noisyimg3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q3.png'

        sql = "INSERT INTO dqrreport_noisefrag (UID, QA_S1B, QA_B0C, QA_B2KC, QA_HRB, QA_NTT, QA_NDT, QA_MLC, QB_S1B, QB_B0C, QB_B2KC, QB_HRB, QB_NTT, QB_NDT, QB_MLC, QC_S1B, QC_B0C, QC_B2KC, QC_HRB, QC_NTT, QC_NDT, QC_MLC, QD_S1B, QD_B0C, QD_B2KC, QD_HRB, QD_NTT, QD_NDT, QD_MLC) VALUES ('"+UnID+"', '" + tabvar[85] + "', '" + tabvar[86] + "', '" + tabvar[87] + "', '" + tabvar[88] + "', '" + tabvar[89] + "', '" + tabvar[90] + "', '" + noisyimg0 + "', '" + tabvar[91] + "', '" + tabvar[92] + "', '" + tabvar[93] + "', '" + tabvar[94] + "', '" + tabvar[95] + "', '" + tabvar[96] + "', '" + noisyimg1 + "', '" + tabvar[97] + "', '" + tabvar[98] + "', '" + tabvar[99] + "', '" + tabvar[100] + "', '" + tabvar[101] + "', '" + tabvar[102] + "', '" + noisyimg2 + "', '" + tabvar[103] + "', '" + tabvar[104] + "', '" + tabvar[105] + "', '" + tabvar[106] + "', '" + tabvar[107] + "', '" + tabvar[108] + "', '" + noisyimg3 +"')"
        #
        #
        mycursor.execute(sql)
        mydb.commit()

        ndfcount += 1

        ###########################################################################################################################################

        sql = "INSERT INTO dqrreport_dqrstats (filename_OF,filename_FF,size_bytes_OF,size_bytes_FF,size_OF,size_FF,events_quadA_OF,events_quadA_FF,events_quadB_OF,events_quadB_FF, events_quadC_OF, events_quadC_FF, events_quadD_OF, events_quadD_FF, UID) VALUES('"+tabvar[1]+"', '"+tabvar[2]+"', '"+tabvar[4]+"', '"+tabvar[5]+"','"+tabvar[7]+"', '"+tabvar[8]+"', '"+tabvar[10]+"', '"+tabvar[11]+"', '"+tabvar[13]+"', '"+tabvar[14]+"', '"+tabvar[16]+"', '"+tabvar[17]+"', '"+tabvar[19]+"', '"+tabvar[20]+"', '"+UnID+"')"

        mycursor.execute(sql)
        mydb.commit()
        ###########################################################################################################################################
        sql = "INSERT INTO dqrreport_datasat (UID,QA_TS,QA_SS,QA_SP,QB_TS,QB_SS,QB_SP,QC_TS,QC_SS,QC_SP,QD_TS,QD_SS,QD_SP) VALUES ('"+UnID+"', '" + \
        tabvar[70] + "','" + tabvar[71] + "','" + tabvar[72] + "','" + tabvar[74] + "','" + tabvar[75] + "','" + tabvar[
            76] + "','" + tabvar[78] + "','" + tabvar[79] + "','" + tabvar[80] + "','" + tabvar[82] + "','" + tabvar[
            83] + "','" + tabvar[84] + "')"
        mycursor.execute(sql)
        mydb.commit()
        ########################################################################################################################################
        if b[0] != "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES (' ', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                      5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] != "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', ' ', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                      5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()


        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] != "date-end" and b[3] == "time-end" and b[
            4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', ' ', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                      5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] != "time-end" and b[
            4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', ' ', '" + obs[4] + "', '" + obs[
                      5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
            4] != "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', ' ', '" + obs[
                      5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
            4] == "obs_id" and b[5] == "sourceid" and b[6] == "observer" and b[7] == "ra_pnt" and \
                b[8] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', 'NA', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
            4] == "obs_id" and b[5] == "exposure" and b[6] != "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', ' ', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
            4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] != "observer" and b[8] == "ra_pnt" and \
                b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', ' ', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
            4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] != "ra_pnt" and \
                b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', ' ', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
            4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
                b[9] != "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', ' ', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
            4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + \
                  obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
                      5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', '"+UnID+"')"
            mycursor.execute(sql)
            mydb.commit()

        if b[0] != "date-obs" and b[1] != "time-obs" and b[2] != "date-end" and b[3] != "time-end" and b[
            4] != "obs_id" and b[5] != "exposure" and b[6] != "sourceid" and b[7] != "observer" and b[8] != "ra_pnt" and b[9] != "dec_pnt":
            sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')"
            mycursor.execute(sql)
            mydb.commit()
        ###################################################################################################################################

        id = id + 1



