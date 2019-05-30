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

pprint(dirlist)

path = []

ndfcount = 0
dphcount = 0
countrate = 0
housekeep = 0

obs = ""

for i in range(0, 17):
    path.append('http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[i] + '/index.html')
    print(path[i])


class Spiderman(scrapy.Spider):
    name = 'spidey'
    start_urls = path

    def parse(self, response):
        b = response.xpath("//li/b/text()").extract()
        obs = response.xpath("//li/text()").extract()
        tabvar = response.xpath("//table/tr/td/text()").extract()


        ################################################################################################################
        # global housekeep
        #
        # hk1 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_CZT_Counter.png'
        # hk2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkDVDD.png'
        # hk3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkTemperature1.png'
        # hk4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkVetoHV_Monitor.png'
        # hk5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hkVetoLLD.png'
        # hk6 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_AlphaCounter.png'
        # hk7 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_CPM_Rate.png'
        # hk8 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_CZT_Counter.png'
        # hk9 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_POS_2DOT5V_Monitor.png'
        # hk10 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_POS_5V_Monitor.png'
        # hk11 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_ROLL_ROT.png'
        # hk12 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_Roll_DEC.png'
        # hk13 =  'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_Roll_RA.png'
        # hk14 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[housekeep] + '/hk_VetoCounter.png'
        #
        #
        # print("hello")
        #
        # print(hk1)
        # print(hk2)
        #
        # housekeep +=1



        #################################################################################################################
        # global countrate
        #
        # crp1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_histogram.png'
        # cri1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageFULL_DPI.png'
        # crp2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_lightcurve.png'
        # cri2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageFULL_DPI.png'
        # crp3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q0.png'
        # cri3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ0.png'
        # crp4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q1.png'
        # cri4 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ1.png'
        # crp5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q2.png'
        # cri5 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ2.png'
        # crp6 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/countrate_modulerates.Q3.png'
        # cri6 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[countrate] + '/imageQ3.png'
        #
        # print("Hello")
        # print(crp1)
        # print(cri1)
        # countrate += 1

        ################################################################################################################

        # global dphcount
        #
        # dphimg0 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q0.png'
        # dphimg1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q1.png'
        # dphimg2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q2.png'
        # dphimg3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[dphcount] + '/dph.Q3.png'
        #
        # print(dphimg0)
        # print(dphimg1)
        # print(dphimg2)
        # print(dphimg3)
        #
        # dphcount += 1


        #####################################################################################################

        # global ndfcount
        # noisyimg0 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q0.png'
        # noisyimg1 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q1.png'
        # noisyimg2 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q2.png'
        # noisyimg3 = 'http://192.168.43.12/ASTROSAT_SAMPLE_DATA/' + dirlist[ndfcount] + '/noisytime.Q3.png'
        #
        # sql = "INSERT INTO dqrreport_noisefrag (UID, QA_S1B, QA_B0C, QA_B2KC, QA_HRB, QA_NTT, QA_NDT, QA_MLC, QB_S1B, QB_B0C, QB_B2KC, QB_HRB, QB_NTT, QB_NDT, QB_MLC, QC_S1B, QC_B0C, QC_B2KC, QC_HRB, QC_NTT, QC_NDT, QC_MLC, QD_S1B, QD_B0C, QD_B2KC, QD_HRB, QD_NTT, QD_NDT, QD_MLC) VALUES (2018020607, '" + tabvar[85] + "', '" + tabvar[86] + "', '" + tabvar[87] + "', '" + tabvar[88] + "', '" + tabvar[89] + "', '" + tabvar[90] + "', '" + noisyimg0 + "', '" + tabvar[91] + "', '" + tabvar[92] + "', '" + tabvar[93] + "', '" + tabvar[94] + "', '" + tabvar[95] + "', '" + tabvar[96] + "', '" + noisyimg1 + "', '" + tabvar[97] + "', '" + tabvar[98] + "', '" + tabvar[99] + "', '" + tabvar[100] + "', '" + tabvar[101] + "', '" + tabvar[102] + "', '" + noisyimg2 + "', '" + tabvar[103] + "', '" + tabvar[104] + "', '" + tabvar[105] + "', '" + tabvar[106] + "', '" + tabvar[107] + "', '" + tabvar[108] + "', '" + noisyimg3 +"')"
        # #
        # #
        # mycursor.execute(sql)
        # mydb.commit()
        #
        # ndfcount += 1

        ##########################################################################################################

        # sql = "INSERT INTO dqrreport_dqrstats (filename_OF,filename_FF,size_bytes_OF,size_bytes_FF,size_OF,size_FF,events_quadA_OF,events_quadA_FF,events_quadB_OF,events_quadB_FF, events_quadC_OF, events_quadC_FF, events_quadD_OF, events_quadD_FF, UID) VALUES('"+tabvar[1]+"', '"+tabvar[2]+"', '"+tabvar[4]+"', '"+tabvar[5]+"','"+tabvar[7]+"', '"+tabvar[8]+"', '"+tabvar[10]+"', '"+tabvar[11]+"', '"+tabvar[13]+"', '"+tabvar[14]+"', '"+tabvar[16]+"', '"+tabvar[17]+"', '"+tabvar[19]+"', '"+tabvar[20]+"', 2018020607)"
        #
        ##################################
        # sql = "INSERT INTO dqrreport_datainteg (UID,M9_A_BD,M9_A_TP,M9_A_DP,M9_B_BD,M9_B_TP,M9_B_DP,M9_C_BD,M9_C_TP,M9_C_DP,M9_D_BD,M9_D_TP,M9_D_DP,M0_A_BD,M0_A_TP,M0_A_DP,M0_B_BD,M0_B_TP,M0_B_DP,M0_C_BD,M0_C_TP,M0_C_DP,M0_D_BD,M0_D_TP,M0_D_DP,SS_A_BD,SS_A_TP,SS_A_DP,SS_B_BD,SS_B_TP,SS_B_DP,SS_C_BD,SS_C_TP,SS_C_DP,SS_D_BD,SS_D_TP,SS_D_DP) VALUES (2018020607, '" + \
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
        ############################################################
        # sql = "INSERT INTO dqrreport_datasat (UID,QA_TS,QA_SS,QA_SP,QB_TS,QB_SS,QB_SP,QC_TS,QC_SS,QC_SP,QD_TS,QD_SS,QD_SP) VALUES (2018020607, '" + \
        # tabvar[70] + "','" + tabvar[71] + "','" + tabvar[72] + "','" + tabvar[74] + "','" + tabvar[75] + "','" + tabvar[
        #     76] + "','" + tabvar[78] + "','" + tabvar[79] + "','" + tabvar[80] + "','" + tabvar[82] + "','" + tabvar[
        #     83] + "','" + tabvar[84] + "')"
        # mycursor.execute(sql)
        # mydb.commit()
        #####################################################################
        # if b[0] != "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES (' ', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
        #               5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] != "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', ' ', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
        #               5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] != "date-end" and b[3] == "time-end" and b[
        #     4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
        #         b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', ' ', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
        #               5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] != "time-end" and b[
        #     4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
        #         b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', ' ', '" + obs[4] + "', '" + obs[
        #               5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
        #     4] != "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
        #         b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', ' ', '" + obs[
        #               5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
        # #     4] == "obs_id" and b[5] == "sourceid" and b[6] == "observer" and b[7] == "ra_pnt" and \
        # #         b[8] == "dec_pnt":
        # #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', 0, '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', 2018020607)"
        # #     mycursor.execute(sql)
        # #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
        #     4] == "obs_id" and b[5] == "exposure" and b[6] != "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
        #         b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', ' ', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
        #     4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] != "observer" and b[8] == "ra_pnt" and \
        #         b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', ' ', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
        #     4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] != "ra_pnt" and \
        #         b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', ' ', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
        #     4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and \
        #         b[9] != "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', ' ', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] == "date-obs" and b[1] == "time-obs" and b[2] == "date-end" and b[3] == "time-end" and b[
        #     4] == "obs_id" and b[5] == "exposure" and b[6] == "sourceid" and b[7] == "observer" and b[8] == "ra_pnt" and b[9] == "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES ('" + \
        #           obs[0] + "', '" + obs[1] + "', '" + obs[2] + "', '" + obs[3] + "', '" + obs[4] + "', '" + obs[
        #               5] + "', '" + obs[6] + "', '" + obs[7] + "', '" + obs[8] + "', '" + obs[9] + "', 2018020607)"
        #     mycursor.execute(sql)
        #     mydb.commit()
        #
        # if b[0] != "date-obs" and b[1] != "time-obs" and b[2] != "date-end" and b[3] != "time-end" and b[
        #     4] != "obs_id" and b[5] != "exposure" and b[6] != "sourceid" and b[7] != "observer" and b[8] != "ra_pnt" and b[9] != "dec_pnt":
        #     sql = "INSERT INTO dqrreport_obsinfo (date_obs,time_obs,date_end,time_end,obs_id,exposure,sourceid,observer,ra_pnt,dec_pnt,UID) VALUES (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')"
        #     mycursor.execute(sql)
        #     mydb.commit()
        ##############################







