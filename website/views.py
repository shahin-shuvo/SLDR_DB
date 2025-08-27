from flask import Blueprint, render_template
import pandas as pd


views = Blueprint('views', __name__)

#Database Att
att_sheet_id = "1_xpuXqZglOPeQ6JpuUKFEC-8hplgdl8Ci8YFUCbugTk"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{att_sheet_id}/export?format=csv")
df= df.fillna("-")
att_records = df.to_dict(orient="records")


#Database P Lve
plve_sheet_id = "116QJp59ZHsjSRgQTwfmId49IFn-dp5wHOLerYRaFLIY"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{plve_sheet_id}/export?format=csv")
df= df.fillna("-")
plve_records = df.to_dict(orient="records")

#Database C Lve M Lve State
clve_sheet_id = "1zH9FVrCWx7wdKDqFZdNOxcQMlqNPsg83fHz9AeVx8Ls"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{clve_sheet_id}/export?format=csv")
df= df.fillna("-")
clve_records = df.to_dict(orient="records")

#Database Course State
course_sheet_id = "1o70_LfZP-bjXkPQz9D07_jqkvDmgpmh-qYIn-tV_r4A"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{course_sheet_id}/export?format=csv")
df= df.fillna("-")
course_records = df.to_dict(orient="records")

#Database Present State
present_sheet_id = "14eFl9sg2BhYifJgODA4r2eJt5pS8JzQYf0GDJ5V8VkE"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{present_sheet_id}/export?format=csv")
df= df.fillna("-")
present_records = df.to_dict(orient="records")


#COY WISE ALL SLDR DATA
#COY WISE ALL SLDR DATA
bhq_sheet = "107wm63WqR4hFS96-d6kqjq2zbCuPex4L5rVnkPjsR0c"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{bhq_sheet}/export?format=csv")
bhq_records = df.to_dict(orient="records")

hq_sheet = "1lnmc8evYqdqVCskBIa8QhM08TZfLMQ9vI-vTUWYBMlw"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{hq_sheet}/export?format=csv")
hq_records = df.to_dict(orient="records")

radio_sheet = "1jMlNL2aY5LlRSnRl2h1LsRPCM1iRdQNikRG1YNqjVs0"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{radio_sheet}/export?format=csv")
radio_records = df.to_dict(orient="records")

op_sheet = "1rqphZM0FaRiDSydPQoNSlRhxzHYSwwK6r-w-8URHvXI"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{op_sheet}/export?format=csv")
op_records = df.to_dict(orient="records")

rr_sheet = "11t0jyQ52iY9EEMdpNbxb9kSvYgXEP90CP_xPLd38b38"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{rr_sheet}/export?format=csv")
rr_records = df.to_dict(orient="records")

bsc123_sheet = "19K1W4kc-BViwrlRNB3gmLPdh98AHGqiRbaNfXfeYW-8"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{bsc123_sheet}/export?format=csv")
bsc123_records = df.to_dict(orient="records")

bsc127_sheet = "15IhAQz9_6HUH8fhQ83bRGjaFTScqVntGydh0YlGw1Lk"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{bsc127_sheet}/export?format=csv")
bsc127_records = df.to_dict(orient="records")

bsc128_sheet = "1td0pTGZYwAXyGgFCVrUhagjEocrqdsaCaJS0Xs89YkY"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{bsc128_sheet}/export?format=csv")
bsc128_records = df.to_dict(orient="records")

bsc212_sheet = "1zUvqnsvQ9WLoIjpI6s5-zftSxa3W6n2DL-Cy64giMPY"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{bsc212_sheet}/export?format=csv")
bsc212_records = df.to_dict(orient="records")

ict_sheet = "1_yCzSK9EwuevmK7Zow9zUpy4XpY2NGGaHghkSbsIFi8"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{ict_sheet}/export?format=csv")
ict_records = df.to_dict(orient="records")

eme_sheet = "1ze42ZvzEAktfHjTcXMVG8fLRGjV8Ok_SecxHecXOzaM"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{eme_sheet}/export?format=csv")
eme_records = df.to_dict(orient="records")

posted_manpower = bhq_records+ hq_records+ radio_records + rr_records + op_records + bsc123_records + bsc127_records + bsc128_records+ bsc212_records + ict_records + eme_records


#IN AID TO CIV POWER
aidToCiv_sheet = "1EmwHtUWUabZT-pOjqzqZjaW-qJu5LeZejs37gAUJfHc"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{aidToCiv_sheet}/export?format=csv")
df= df.fillna("-")
aidToCiv_records = df.to_dict(orient="records")


coy_list = [["HQ", hq_records], ["BHQ", bhq_records],
                ["RADIO COY", radio_records], ["OP COY", op_records],
                 ["RR & LINE COY", rr_records], ["123 BSC", bsc123_records],
                  ["127 BSC", bsc127_records], ["128 BSC", bsc128_records],
                   ["212 ABSC", bsc212_records], ["ICT GP", ict_records], ]

@views.route('/')
def home():
    #coy_name = ["HQ", "BHQ", "RADIO", "RR & LINE", "OP COY", "123 BSC", "127 BSC", "128 BSC", "212 BSC"]
   
    return render_template("home.html", coy_list = coy_list,
                           posted_count = len(posted_manpower),
                           att_count = len(att_records),
                           aidToCiv_count = len(aidToCiv_records),
                           plve_count = len(plve_records),
                           course_count = len(course_records),
                           clve_count = len(clve_records),
                           present_count = len(present_records))

@views.route('/about')
def aboutpgcc():
    return render_template("about.html")

@views.route('/sldr_db')
def sldr_db():
    return render_template("sldr_db.html", posted_manpower= posted_manpower)

@views.route('/aidtociv')
def aidtociv():
    return render_template("aidtociv.html", aidToCiv_records= aidToCiv_records)

@views.route('/att')
def att():
    return render_template("att.html", att_records= att_records)

@views.route('/plve')
def plve():
    return render_template("plve.html", plve_records= plve_records)

@views.route('/course')
def course():
    return render_template("course.html", course_records= course_records)

@views.route('/clve')
def clve():
    return render_template("clve.html", clve_records= clve_records)



@views.route('/present')
def presnt():
    return render_template("present.html", present_records= present_records)

@views.route('/coywise/<index>')
def coywise(index):
    index = int(index, base=10) -1
    return render_template("coywise.html", coy_records= coy_list[index][1], coy_name = coy_list[index][0])
