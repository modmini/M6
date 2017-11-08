# -*- coding: utf-8 -*-

import TOBY
import requests
from TOBY.lib.curve.ttypes import *
from datetime import datetime
# https://kaijento.github.io/2017/05/19/web-scraping-youtube.com/
# from imgurpython import ImgurClient
import time,random,sys,json,codecs,threading,glob,re

cl = TOBY.LINE()
cl.login(qr=True)
cl.loginResult

#client_id = ''
#client_secret = ''
#access_token = ''
#refresh_token = ''

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)


ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

#album = None
#image_path = 'tmp/tmp.jpg'

helpMessage ="""
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=[""]
creator=[""]
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Owner : line://ti/p/~tobyg74",
    "lang":"JP",
    "comment":"Owner : line://ti/p/~tobyg74",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

#---------------------------[AutoLike-nya]---------------------------#
def autolike():
			for zx in range(0,100):
				hasil = cl.activity(limit=100)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"􁄁􀆙Sale Tag􏿿รับติด฿ΦŦ ℣.10􁄁􀆙Sale Tag􏿿\n 􁄁􀆙Sale Tag􏿿ไปติดตั้งที่ห้อง บอท12ตัวราคา 180บาท\n􁄁􀆙Sale Tag􏿿ไปติดที่ห้องบออท37ตัว ราคา650บาท\n􁄁􀆙Sale Tag􏿿รับติดบอทแท็กชื่อ ราคา 300บาท จ่ายทีเดียวจบไม่มีรายเดือน เจ้าของห้องสามารถสัั่งแท็กเองได้\n􀔃􀅖red arrow lower right􏿿วิดีโอรีวิวบอทแท็กคน􀔃􀅘red arrow lower left􏿿\nhttps://timeline.line.me/post/_dSr84FveYQi6czTgsOHTD2bMB3Sc8TMBA14WSAk/1150915905809023920\n ☆ ☞ ความสามารถของบอทวี10 ☜☆\n\n1.)กันสมาชิกเปิดลิ้งห้อง\n2.)กันสมาชิกเปลี่ยนรูปกลุ่ม\n3.)กันสมาชิกเชิญคนนอกเข้า\n4.)กันสมาชิกเปลี่ยนชื่อกลุ่ม\n5.)กันคนนอกเข้ามาลบคนในกลุ่มถ้าลบเกิน3คนบอทจะลบออกทันที\n6.)สามารถดูคนที่แอบอ่านข้อความที่คุณส่งในห้องได้\n7.)บอทวี10สามารถมีแอดได้2คน\nทุกราคา+บอทคุยออโต้+คำสั่งบอทภาษาไทย1ตัว+รับประกันห้อง1ห้องทันที+ห้องคำสั่ง\n\n􁄁􀆙Sale Tag􏿿รับสั่งทำยอทคุยออโต้ บอทApi. บอทเลขา แบบกำหนดชื่อปกรูปได้ กำหนดคำได้ ราคา200บาทต่อตัว\nรับติดตั้งบอทกันทุกชนิด\nสนใจติดต่อ\nทราย 0902853778 0908927220\nhttp://line.me/ti/p/~bot_botv13")
						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like 10/30")
						print "DiLike"
					except:
							pass
				else:
						print "DiLike"
			time.sleep(0)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#-------------------------------------------------------#
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#-----------------------------------------------------#

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

#-------------------------------------------------------------------------------------#
        if op.type == 25:
            msg = op.message
            if msg.text in ["Speed","speed","Sp","sp"]:
                    start = time.time()
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#--------------------------------------------------------------------------------------#

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
