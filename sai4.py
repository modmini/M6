# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess


cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = cl

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')
i = 0
c_text = """ Auto Like By. SAI

􁄁􀆙Sale Tag􏿿รับติดBot V10 􁄁􀆙Sale Tag􏿿

BotV10ประกอบไปด้วย

 1⃣.しりちゃん v10
 2⃣.Parry v10
 3⃣.Eliza v10
 4⃣.Doctor.A v10
 5⃣.Rakko v10
 6⃣. しりちゃん追加保護ボット 7 -32 ตัว

􀔃􀄒novice􏿿ราคาไปติดที่กลุ่ม􀔃􀄒novice􏿿

􁄁􀆙Sale Tag􏿿180บาท v.10 12ตัว+บอทคำสั่ง&คุยภาษาไทย1ตัว

􁄁􀆙Sale Tag􏿿200บาท v.10 12ตัว+บอทคำสั่ง&คุยภาษาไทย1ตัว+ประกันห้อง1ห้อง

􁄁􀆙Sale Tag􏿿700บาท v.10 37ตัว+บอทคำสั่ง&คุยภาษาไทยตัว+ประกันห้อง1ห้อง

􁄁􀆙Sale Tag􏿿รับติดตั้งบอทแท็กคน เจ้าของห้องและคนอื่นสามารถสั่งแท็กเองได้ แท็กได้แบบไม่จำกัด แท็กทั้งห้อง(คำสั่งภาษาไทย) ราคา300บ.  จ่ายทีเดียวจบไม่มีเรียกเก็บรายเดือน

􀔃􀅖red arrow lower right􏿿วิดีโอรีวิวบอทแท็กคน􀔃􀅘red arrow lower left􏿿
https://timeline.line.me/post/_dSr84FveYQi6czTgsOHTD2bMB3Sc8TMBA14WSAk/1150915905809023920

􁄁􀆙Sale Tag􏿿รับติดกันคนลบ+แท็กคนแอบอ่าน

ความสามารถบอทกันลบ
1. กันการลบ1บอทลบ
2. กันเชิญใครเชิญบอทเตะคนเชิญ+ยกเลิก
3. กันการเปิดลิ้งค์กลุ่ม
4. กันสมาชิกยกเลิกค้างเชิญใครยกเลิกบอทเตะ
5. กันการเพิ่มโน้ต ใครเพิ่มบอทลบ
6. สั่งเตะคนได้+ทำดำขาวได้+สั่งดูคนแอบอ่านได้และฟังชั่นอีกมาก
􀐂􀅷red flag􏿿ทุกราคา+บอทคุยออโต้+คำสั่งบอทภาษาไทย1ตัว+รับประกันห้ออง1ห้องทันที+ห้องคำสั่ง

􀔃􀄄double arrow right􏿿คุณสมบัติของบอทวี10􀔃􀄁double arrow left􏿿

1.)กันสมาชิกเปิดลิ้งห้อง
2.)กันสมาชิกเปลี่ยนรูปกลุ่ม
3.)กันสมาชิกเชิญคนนอกเข้า
4.)กันสมาชิกเปลี่ยนชื่อกลุ่ม
5.)กันคนนอกเข้ามาลบคนในกลุ่ม
ถ้าลบเกิน3คนบอทจะลบออกทันที
6.)สามารถดูคนที่แอบอ่านข้อความที่คุณส่งในห้องได้
7.)บอทสิริวี10สามารถมีแอดได้2คน


􁄁􀆙Sale Tag􏿿รับสั่งทำยอทคุยออโต้ บอทApi. บอทเลขา แบบกำหนดชื่อปกรูปได้ กำหนดคำได้

ติดต่อสอบถามคลิ้กที่ลิ้งด้านล่าง
ทราย
􀔃􀄎LINE messenger􏿿http://line.me/ti/p/~saibot01
0902853778
"""

helpMessage ="""✯==== ꧁ ⋆⋆⋆〖SAI〗 Softbot⋆⋆⋆ ꧂ ====✯

❂͜͡☆➣ [Id]
❂͜͡☆➣ [Mid]
❂͜͡☆➣ [Me]
❂͜͡☆➣ [Tl "text"]
❂͜͡☆➣ [Bye bye]: You left the group
❂͜͡☆➣ [Cn "text"]
❂͜͡☆➣ [Gift]
❂͜͡☆➣ [Mc "mid"]: convert mid to contact
❂͜͡☆➣ [Groups]
❂͜͡☆➣ [Like:on/off]: Auto like Post Timeline
❂͜͡☆➣ [album→ ]
❂͜͡☆➣ [album merit "id"]
❂͜͡☆➣ [album remove "id"]tact:on]
❂͜͡☆➣ [Rgroups]: Reject spam invitation groups
❂͜͡☆➣ [Auto add message "text"]
❂͜͡☆➣ [Auto add message confirm]
❂͜͡☆➣ [Clock:on/off]
❂͜͡☆➣ [Clock  "text"︎]
❂͜͡☆➣ [Update]: Update clock
❂͜͡☆➣ [Update status]: Update your profile status message
❂͜͡☆➣ [Comment confirm]
❂͜͡☆➣ [Comment "text"]
❂͜͡☆➣ [Comment bl add]
❂͜͡☆➣ [Comment bl del]
❂͜͡☆➣ [Comment bl confirm]
❂͜͡☆➣ [Ban]
❂͜͡☆➣ [Set]: Show your Auto setting
❂͜͡☆➣ [Set]: Auto setting room
❂͜͡☆➣ [Unban]
❂͜͡☆➣ [Banlist]
❂͜͡☆➣ [Check banlist]
❂͜͡☆➣ [Check mbl]
❂͜͡☆➣ [Ginfo]
❂͜͡☆➣ [Groups]
❂͜͡☆➣ [Cancel]
❂͜͡☆➣ [Clean]
❂͜͡☆➣ [Invite [mid]]Invite by mid people
❂͜͡☆➣ [Gn "the group name"]
❂͜͡☆➣ [Gurl]
❂͜͡☆➣ [gurl merit"the group ID"]
❂͜͡☆➣ [Nk "the name/tag"]
❂͜͡☆➣ [Kick: "mid"]
❂͜͡☆➣ [Fuck "Tag"]
❂͜͡☆➣ [Kill]
❂͜͡☆➣ [Url open]
❂͜͡☆➣ [Url close]

✯==== ꧁ Command for kicker ꧂ ====✯

❂͜͡☆➣ [Kicker]: All kicker join
❂͜͡☆➣ [K1 gift]: K1,k2,k3 have much kicker
❂͜͡☆➣ [K1/K2/K3 join]: Kicker join one by one
❂͜͡☆➣ [K1 rename: "text"]
❂͜͡☆➣ [Bye]: All kicker Leave
❂͜͡☆➣ [K1/K2K3 @bye]: Kicker leave one by one
❂͜͡☆➣ [K1/K2/K3 fuck "Tag"]: K1/K2 kick people
❂͜͡☆➣ [K1 invite [mid]]: Kicker invite by mid people
❂͜͡☆➣ [K1 gn "the group name"]: K1/K2
❂͜͡☆➣ [K1 upstatus]: Kicker update profile status
❂͜͡☆➣ [K1/K2/K3 rgroups]: Kicker reject spam groups

✯==== ꧁ Auto Setting Command ꧂ ====✯

❂͜͡☆➣ [Contact:on/off]
❂͜͡☆➣ [Auto add:on/off]
❂͜͡☆➣ [Share:on/off]
❂͜͡☆➣ [Comment:on/off]
❂͜͡☆➣ [Auto join:on/off]

✯==== ꧁ Protection ꧂ ====✯

❂͜͡☆➣ [Protect:on/off]
❂͜͡☆➣ [Pro url:on/off]
❂͜͡☆➣ [Blockinvite:on/off]

〖SAI〗☞B❂T

✯===== ⋆⋆〖SAI〗 Softbot⋆⋆ ======✯
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,"ubcd678c1e478baff8a4c453e52049dbf"]
admin=["ubcd678c1e478baff8a4c453e52049dbf"]
me = cl.getProfile().mid
bot1 = cl.getProfile().mid
main = cl.getProfile().mid
kicker1 = ki.getProfile().mid
bots = me + kicker1
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []

omikuzi = ["大吉","中吉","小吉","末吉","大凶","凶"]

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Self Bot SAI",
    "lang":"JP",
    "comment":"Self Bot SAI",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
	"pnharfbot":{},
    "pname":{},
    "pro_name":{},
	"posts":True,
	}

wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }

setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}


def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def autolike(op):
    try:
		for posts in cl.activity(1)["result"]["posts"]:
			if wait["posts"] == True:
				if posts["postInfo"]["liked"] is False:
					cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					print u"liked" + str(i)
					i += 1
    except Exception as e:
            print e

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
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user flushing is complete")

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = ks.getGroup(op.param1)
                                except:
                                    try:
                                        G = kb.getGroup(op.param1)
				    except:
					try:
                                            G = ks.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    ks.updateGroup(G)
                                except:
                                    try:
                                        kb.updateGroup(G)
                                    except:
                                        try:
                                            kr.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ks.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kr.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL can not be changed")
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ubcd678c1e478baff8a4c453e52049dbf":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ks.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = kk.getGroup(list_[1])
                            X = ks.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            kk.updateGroup(X)
                            ks.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already on the blacklist。")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I decided not to comment。")
                        f=codecs.open('st2.json','w','utf-8')
                        json.dump(wait["commentBlack"], f, sort_keys=True, indent=4,ensure_ascii=False)
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"I deleted it from the black list。")
                        wait["dblack"] = False
                        f=codecs.open('st2.json','w','utf-8')
                        json.dump(wait["commentBlack"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list。")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already on the blacklist。")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to blacklist。")
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"I deleted it from the black list。")
                        wait["dblacklist"] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list。")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("P1 gn:" in msg.text):
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    G.name = msg.text.replace("P1 gn:","")
                    ki.updateGroup(G)
                else:
                    ki.sendText(msg.to,"Not for use less than group")
            elif ("P2 gn " in msg.text):
                if msg.toType == 2:
                    G = kk.getGroup(msg.to)
                    G.name = msg.text.replace("P2 gn ","")
                    kk.updateGroup(G)
                else:
                    kk.sendText(msg.to,"Not for use less than group")
            elif ("P3 gn " in msg.text):
                if msg.toType == 2:
                    G = ks.getGroup(msg.to)
                    G.name = msg.text.replace("P2 gn ","")
                    ks.updateGroup(G)
                else:
                    ks.sendText(msg.to,"Not for use less than group")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "P1 invite " in msg.text:
                midd = msg.text.replace("K1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "P2 invite " in msg.text:
                midd = msg.text.replace("K2 invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "P3 invite " in msg.text:
                midd = msg.text.replace("K3 invite ","")
                ks.findAndAddContactsByMid(midd)
                ks.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "P1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                ki.sendMessage(msg)
            elif "P2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                kk.sendMessage(msg)
            elif "P3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                ks.sendMessage(msg)
            elif msg.text in ["愛のプレゼント","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Bot1 gift","P1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Bot2 gift","P2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["Bot3 gift","P3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ks.sendMessage(msg)
            elif msg.text in ["ยกเลิก","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["บอทยกเลิก","Clean"]:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Block url:on","เปิดป้องกันลิ้ง"]:
				protecturl.append(msg.to)
				cl.sendText(msg.to,"เปิดป้องกันลิ้งเรียบร้อย..")
				cl.sendText(msg.to,"Link protection..")
            elif msg.text in ["Block url:off","ปิดป้องกันลิ้ง"]:
				if msg.from_ in Administrator:
					protecturl.remove(msg.to)
					cl.sendText(msg.to,"ปิดป้องกันลิ้งเรียบร้อย..")
					cl.sendText(msg.to,"Allowed Links..")
				else:
					cl.sendText(msg.to,"already")
            elif msg.text in ["Url open","Ourl","#เปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(ms.to,"already open")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Url close","Curl","#ปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "P1 mid" == msg.text:
                ki.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,mid)
                kk.sendText(msg.to,mid)
                ks.sendText(msg.to,mid)
            elif "P2 mid" == msg.text:
                kk.sendText(msg.to,mid)
            elif "P3 mid" == msg.text:
                ks.sendText(msg.to,mid)
            elif "Bot mid" == msg.text:
                ki.sendText(msg.to,mid)
                kk.sendText(msg.to,mid)
                ks.sendText(msg.to,mid)
            elif "Lol" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif "Hmm" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif "Hello" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif "Tl:" in msg.text:
                tl_text = msg.text.replace("Tl:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Cn:" in msg.text:
                string = msg.text.replace("Cn:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif "P1ชื่อ:" in msg.text:
                string = msg.text.replace("P1ชื่อ:","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif "P2ชื่อ:" in msg.text:
                string = msg.text.replace("P2ชื่อ:","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif "P3ชื่อ:" in msg.text:
                string = msg.text.replace("P3ชื่อ:","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ks.getProfile()
                    profile_B.displayName = string
                    ks.updateProfile(profile_B)
                    ks.sendText(msg.to,"name " + string + " done")
            elif "Mc:" in msg.text:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif "เปลี่ยนตัส:" in msg.text:
                string = msg.text.replace("เปลี่ยนตัส:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"display message " + string + " done")
            elif "P1ตัส:" in msg.text:
                string = msg.text.replace("P1ตัส:","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"display message " + string + " done")
            elif "P2ตัส:" in msg.text:
                string = msg.text.replace("P2ตัส:","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = kk.getProfile()
                    profile_C.statusMessage = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"display message " + string + " done")
            elif "P3ตัส:" in msg.text:
                string = msg.text.replace("P3ตัส:","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = ks.getProfile()
                    profile_C.statusMessage = string
                    ks.updateProfile(profile_C)
                    ks.sendText(msg.to,"display message " + string + " done")
            elif msg.text in ["Contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["自動参加:オン","Join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif "Auto cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Auto cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Share off","#Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif "Set" == msg.text:
                md = "꧁ ⋆ SAI Self BOT Lv.6.2.4⋆ ꧂\n\n"
                if wait["contact"] == True: md+="❂͜͡☆➣ contact on\n"
                else: md+="❂͜͡☆➣ contact off\n"
                if wait["autoJoin"] == True: md+="❂͜͡☆➣ auto join on\n"
                else: md +="❂͜͡☆➣ auto join off\n"
                if wait["autoCancel"]["on"] == True:md+="❂͜͡☆➣ auto cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "❂͜͡☆➣ auto cancel off\n"
                if wait["leaveRoom"] == True: md+="❂͜͡☆➣ auto leave on\n"
                else: md+="❂͜͡☆➣ auto leave off\n"
                if wait["timeline"] == True: md+="❂͜͡☆➣ share on\n"
                else:md+="❂͜͡☆➣ share off\n"
                if wait["autoAdd"] == True: md+="❂͜͡☆➣ auto add on\n"
                else:md+="❂͜͡☆➣ auto add off\n"
                if wait["commentOn"] == True: md+="❂͜͡☆➣ comment on\n"
                else:md+="❂͜͡☆➣ comment off\n"
                cl.sendText(msg.to,md)
            elif "album merit" in msg.text:
                gid = msg.text.replace("album merit","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"相册没在。")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "以下是对象的相册"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album" in msg.text:
                gid = msg.text.replace("album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"相册没在。")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "以下是对象的相册"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove" in msg.text:
                gid = msg.text.replace("album remove","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "删除了事的相册。")
            elif msg.text in ["Groups","Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["ลบค้างเชิญทั้งหมด","ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Finished")
                else:
                    cl.sendText(msg.to,"Rejected all invitation group")
            elif msg.text in ["P1 rgroup"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Finished")
                else:
                    ki.sendText(msg.to,"Rejected all invitation group")
            elif msg.text in ["P2 rgroup"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"Finished")
                else:
                    kk.sendText(msg.to,"Rejected all invitation group")
            elif msg.text in ["P3 rgroup"]:
                gid = ks.getGroupIdsInvited()
                for i in gid:
                    ks.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ks.sendText(msg.to,"Finished")
                else:
                    ks.sendText(msg.to,"Rejected all invitation group")
            elif "album remove" in msg.text:
                gid = msg.text.replace("album remove","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "删除了事的相册。")
            elif msg.text in ["Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Add off","/Auto add:off","自動追加：關"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif "Com:" in msg.text:
                wait["message"] = msg.text.replace("Com:","")
                cl.sendText(msg.to,"message changed")
            elif "Auto add quest adjust " in msg.text:
                wait["message"] = msg.text.replace("Auto add quest adjust ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"变更了信息。")
            elif msg.text in ["Auto add message confirm","Com check"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"自动追加信息像以下一样地被设定。\n\n" + wait["message"])
            elif "Comment " in msg.text:
                c = msg.text.replace("Comment ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "/settings " in msg.text:
                c = msg.text.replace("/settings ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Coment on","/Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["/Comment:off","Coment off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Comment confirm","Coment check"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "#url" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("#url","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
            elif "gotgurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gotgurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["/Comment bl add"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"added")
            elif msg.text in ["/Comment bl del"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"deleted")
            elif msg.text in ["/Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"The following is a black list")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["/Clock:on","Clock on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["/Clock:off","Clock off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif "/Change clock:" in msg.text:
                n = msg.text.replace("Change clock:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["/Update","Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"updated")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")
            elif msg.text in ["P1 join","P1 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["P2 join","P2 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["P3 join","P3 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ks.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(msg.to)

            elif msg.text in ["Kicker"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)


            elif msg.text in ["P1 @bye","P1 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ki.leaveGroup(msg.to)
                except:
                     pass

            elif msg.text in ["P2 @bye","P2 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kk.leaveGroup(msg.to)
                except:
                     pass

            elif msg.text in ["P3 @bye","P3 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ks.leaveGroup(msg.to)
                except:
                     pass

            elif msg.text in ["#bye","#Bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
					ks.leaveGroup(msg.to)
                except:
                     pass

            elif msg.text in ["#Bye Me"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					cl.leaveGroup(msg.to)
                except:
                     pass


            elif "MK:" in msg.text:
				OWN = "ubcd678c1e478baff8a4c453e52049dbf"
				if msg.from_ in OWN:
					pass
				else:
					mk0 = msg.text.replace("MK:","")
					mk1 = mk0.lstrip()
					mk2 = mk1.replace("@","")
					mk3 = mk2.rstrip()
					_name = mk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"user does not exist")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ki.kickoutFromGroup(msg.to,[target])
									kk.kickoutFromGroup(msg.to,[target])
									ks.kickoutFromGroup(msg.to,[target])
							except:
									kicker1 = [ki,kk,ks]
									random.choice(kicker1).kickoutFromGroup(msg.to, [target])
									pass
            elif "Tkick" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
            elif msg.text in ["NK "]:
				OWN = "ubcd678c1e478baff8a4c453e52049dbf"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("NK ","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"user does not exist")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									kicker1 = [cl,ki,kk,ks]
									random.choice(kicker1).kickoutFromGroup(msg.to, [target])
							except:
									kicker1 = [cl,ki,kk,ks]
									random.choice(kicker1).kickoutFromGroup(msg.to, [target])
									pass
            elif "/Tkick" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
            elif "/Fuck" in msg.text:
				OWN = "ubcd678c1e478baff8a4c453e52049dbf"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("Fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"user does not exist")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									cl.kickoutFromGroup(msg.to, [target])
							except:
									cl.kickoutFromGroup(msg.to, [target])
									pass
            elif "NK1" in msg.text:
				OWN = "ubcd678c1e478baff8a4c453e52049dbf"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("NK1","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"user does not exist")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ki.kickoutFromGroup(msg.to, [target])
							except:
									ki.kickoutFromGroup(msg.to, [target])
									pass
            elif "NK2" in msg.text:
				OWN = "ubcd678c1e478baff8a4c453e52049dbf"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("NK2","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"user does not exist")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									kk.kickoutFromGroup(msg.to, [target])
							except:
									kk.kickoutFromGroup(msg.to, [target])
									pass

            elif "NK3" in msg.text:
				OWN = "ubcd678c1e478baff8a4c453e52049dbf"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("NK3","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"user does not exist")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ks.kickoutFromGroup(msg.to, [target])
							except:
									ks.kickoutFromGroup(msg.to, [target])
									pass

#-------------------------------------------------------------------蹴り返し
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist","Meban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing")
                else:
                    cl.sendText(msg.to,"The following is a black list")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Check ban","Meban Check"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "↵")
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
						kicker1 = [cl,ki,kk,ks]
						random.choice(kicker1).kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user flushing is complete")
            elif msg.text in ["/Clear","ยกเลิก1"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "radom:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("radom:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "/album→" in msg.text:
                try:
                    albumtags = msg.text.replace("album→","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "Prourl on" == msg.text:
                try:
                    protecturl.append(msg.to)
                    cl.sendText(msg.to,"protect url on")
                except:
                    cl.sendText(msg.to,"Error")
            elif "Prourl off" == msg.text:
                if msg.to in protecturl:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"protect url off")
            elif "Like on" == msg.text:
				if wait["posts"] == True:
					for posts in cl.activity(1)["result"]["posts"]:
							cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
							cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
							print u"liked" + str(i)
							i += 1
							cl.sendText(msg.to,"like on")
            elif "Like off" == msg.text:
				for posts in cl.activity(1)["result"]["posts"]:
					if wait["posts"] == False:
							cl.sendText(msg.to,"like off")
            elif "Protect on" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"already on")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"turned on")
            elif "Protect off" == msg.text:
				try:
					if msg.from_ in Administrator:
						protection.remove(msg.to)
						cl.sendText(msg.to,"turned off")
					else:
						cl.sendText(msg.to,"already off")
				except:
					pass

            elif "Namelock on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Turned on")
                else:
                    cl.sendText(msg.to,"Already on")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Turn off")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"Already off")

            elif "Blockinvite on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Protect invitation on")
            elif "Blockinvite off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Protect invitation off")
				except:
					pass

#-----------------------------------------------
            elif "#set" in msg.text:
				cl.sendText(msg.to, "Let's see who lazy to type")
				try:
					del wait2['readPoint'][msg.to]
					del wait2['readMember'][msg.to]
				except:
					pass
				wait2['readPoint'][msg.to] = msg.id
				wait2['readMember'][msg.to] = ""
				wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				wait2['ROM'][msg.to] = {}
				print wait2
            elif "#read" in msg.text:
				if msg.to in wait2['readPoint']:
					if wait2["ROM"][msg.to].items() == []:
						chiya = ""
					else:
						chiya = ""
						for rom in wait2["ROM"][msg.to].items():
							print rom
							chiya += rom[1] + "\n"

					cl.sendText(msg.to, "people who reading%s\n is this\n\n\nDate and time I started it:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
				else:
					cl.sendText(msg.to, "read point not set ‚\nReading point settingIf you send it it will send an esxisting one")
            elif "#V10" in msg.text:
                cl.sendText(msg.to,"""[SELFBOT]\n\n
Set up protection within groups.

Protect:on/off
Namelock:on/off
Blockinvite:on/off
protect url:on/off

Do not think I will try.
""")

            elif "วี10" in msg.text:
                cl.sendText(msg.to,"""

คำสั่งบอท siri
คำนี้เป็นการล็อกห้องสั่งแล้วทุกคนจะทำอะไรไม่ได้นอกจากเจ้าของห้องทำได้คนเดียวเช่น•เปิดลิงค์•เชิญเพื่อน•เปลี่ยนรูปกลุ่ม•เปลี่ยนชื่อกลุ่มไรแบบนี้• บอทจะไม่เตะเเอทมินทุกกรณี
มีตั้งเเต่ชุดบอท 12-37 บอท
ชุดล๊อกห้อง
ล๊อกกันรันสติ๊กเกอร์
Set:StampLimitation:on

ล๊อกชื่อกลุ่ม
Set:changenamelock:on

ล๊อกการเชิญของสมาชิก
Set:blockinvite:on

ล๊อกแอทมินกลุ่ม
Set:ownerlock:on

ล๊อกรูปกลุ่ม
Set:iconlock:on

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeowner
เปลี่ยนเจ้าของห้องสั่งแล้วส่งคอลแทคคนที่จะเป็นเจ้าของห้องคนต่อไปลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addblacklist
บัญชีดำแบ็คลิสคนไม่ให้เข้ากลุ่มสั่งแล้วส่งคอลแทคคนที่เราจะแบ็คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addwhitelist
บัญชีขาวแก้ดำสั่งแล้วส่งคอลแทคคนที่เราจะแก้แบ๊คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:blockinvite:off  ปลดล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:on  ล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:inviteurl         เปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:DenyURLInvite  ปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:cancelinvite  ยกเลิกค้างเชิญสั่ง2ครั้ง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:groupcreator เช็คเจ้าของบ้านตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:extracreator  เช็คเจ้าของบ้านคนสำรอง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeextraowner
เพิ่มเจ้าของบ้านคนที2หรือเรียกคนสำรองสั่งแล้วส่งคอลแทคคนที่จะเป็นคนสำรองลงในกลุ่ม

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:turncreator

สลับให้เจ้าของบ้านคนที่2เป็นตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

ดูคนอ่าน

สั่งตั้งค่าก่อนแล้วค่อยสั่งอ่านคน

Setlastpoint     ตั้งค่า

Viewlastseen   สั่งอ่าน
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

สนใจติดต่อที่

ทราย
http://line.me/ti/p/~bot_botv13
0902853778
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
""")
            elif ("Hack " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
            elif ("PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error(｡•́︿•̀｡)")

            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif msg.text == "เช็ค":
              if msg.from_ in admin:
                cl.sendText(msg.to, "!เปิดระบบเช็คคนแอบอ่าน กรุณาพิมพ์ [อ่าน]")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "อ่าน":
              if msg.from_ in admin:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

                    cl.sendText(msg.to, "||=====[SELFBOT]=====||\n\n|[รายการอ่าน]\n%s\n\n[รายการอ่านทั้งหมด]\n%s\n\n[เวลาที่ตั้งอ่านครั้งล่าสุด][%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
	          else:
	            cl.sendText(msg.to, "ไม่สามารถอ่านได้กรุณาตั้งค่าใหม่พิมพ์\n[เช็ค]\nตั้งค่าเสร็จสิ้นกรุณาพิมพ์\n[อ่าน]")
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["SAI","sai","ทรายแท็ก","ทรายแท็กชื่อ","ฺBot.","แท็ก"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif "แท็กชื่อ" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
            elif "Bot@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki.sendMessage(msg)





#-----------------------------------------------
            elif "sai Say " in msg.text:
				bctxt = msg.text.replace("sai Say ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt))
            elif msg.text in ["Salam1"]:
                ki.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                ki.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")

#-----------------------[Help Section]------------------------
            elif msg.text in ["sai /help","sai /Help","sai help","sai help","คำสั่งBot","คำสั่งบอท","ทรายคำสั่ง","sai คำสั่ง"]:
                if wait["lang"] == "JP":
                    random.choice(KAC).sendText(msg.to,helpMessage)
                    print "[Command]/help executed"
                else:
                    cl.sendText(msg.to,helpt)
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PING 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PING 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ks.sendText(msg.to,"PING 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Responsename","respon"]:
                ki.sendText(msg.to,"Bot1 on")
                kk.sendText(msg.to,"Bot2 on")
                ks.sendText(msg.to,"Bot3 on")
#-----------------------------------------------
#------------------------------------------------------------------
            elif "Bl " in msg.text:
               if msg.toType == 2:
                    if msg.from_ in admin:
                       ban0 = msg.text.replace("Bl ","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Success")
                                except:
                                    cl.sendText(msg.to,"error")
#-----------------------------------------------------------
            elif "Midb:" in msg.text:
                midd = msg.text.replace("Midb:","")
                wait["blacklist"][midd] = True
                f=codecs.open('st2__b.json','w','utf-8')
                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#-----------------------------------------------------------
            elif "Wl " in msg.text:
               if msg.toType == 2:
                    if msg.from_ in admin:
                       unb0 = msg.text.replace("Wl ","")
                       unb1 = unb0.lstrip()
                       unb2 = unb1.replace("@","")
                       unb3 = unb2.rstrip()
                       x_name = unb3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if x_name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Success")
                                except:
                                    cl.sendText(msg.to,"error")
#-----------------------------------------------------------
#-------------------------------------------------------------------蹴り返し
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


                elif op.param3 in Amid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass


		if op.type == 19:
			try:
				if op.param3 in kimid:
					if op.param2 in ki2mid:
						G = ks.getGroup(op.param1)
						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)
					else:
						G = ks.getGroup(op.param1)

						ks.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki2mid:
					if op.param2 in ki3mid:
						G = kr.getGroup(op.param1)
						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)
					else:
						G = kr.getGroup(op.param1)

						kr.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki3mid:
					if op.param2 in ki4mid:
						G = kl.getGroup(op.param1)
						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)
					else:
						G = kl.getGroup(op.param1)

						kl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki4mid:
					if op.param2 in ki5mid:
						G = km.getGroup(op.param1)
						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)
					else:
						G = km.getGroup(op.param1)

						km.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki5mid:
					if op.param2 in ki6mid:
						G = kn.getGroup(op.param1)
						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kn.updateGroup(G)
					else:
						G = kn.getGroup(op.param1)

						kn.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki6mid:
					if op.param2 in mid:
						G = cl.getGroup(op.param1)
						G.preventJoinByTicket = False
						cl.updateGroup(G)
						Ticket = cl.reissueGroupTicket(op.param1)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						cl.updateGroup(G)
					else:
						G = cl.getGroup(op.param1)

						cl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						cl.updateGroup(G)
						Ticket = cl.reissueGroupTicket(op.param1)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						cl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

        if op.type == 19:
            try:
                if op.param3 in kimid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


                elif op.param3 in ki2mid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass


		if op.type == 19:
			try:
				if op.param3 in ki3mid:
					if op.param2 in ki2mid:
						G = ks.getGroup(op.param1)
						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)
					else:
						G = ks.getGroup(op.param1)

						ks.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki4mid:
					if op.param2 in ki3mid:
						G = kr.getGroup(op.param1)
						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)
					else:
						G = kr.getGroup(op.param1)

						kr.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki5mid:
					if op.param2 in ki4mid:
						G = kl.getGroup(op.param1)
						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)
					else:
						G = kl.getGroup(op.param1)

						kl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki6mid:
					if op.param2 in ki5mid:
						G = km.getGroup(op.param1)
						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)
					else:
						G = km.getGroup(op.param1)

						km.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in mid:
					if op.param2 in ki6mid:
						G = kn.getGroup(op.param1)
						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kn.updateGroup(G)
					else:
						G = kn.getGroup(op.param1)

						kn.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

        if op.type == 19:
            try:
                if op.param3 in ki6mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


                elif op.param3 in ki6mid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass


		if op.type == 19:
			try:
				if op.param3 in ki6mid:
					if op.param2 in ki2mid:
						G = ks.getGroup(op.param1)
						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)
					else:
						G = ks.getGroup(op.param1)

						ks.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki6mid:
					if op.param2 in ki3mid:
						G = kr.getGroup(op.param1)
						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)
					else:
						G = kr.getGroup(op.param1)

						kr.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki6mid:
					if op.param2 in ki4mid:
						G = kl.getGroup(op.param1)
						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)
					else:
						G = kl.getGroup(op.param1)

						kl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki6mid:
					if op.param2 in ki5mid:
						G = km.getGroup(op.param1)
						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)
					else:
						G = km.getGroup(op.param1)

						km.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in kimid:
					if op.param2 in ki6mid:
						G = kn.getGroup(op.param1)
						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kn.updateGroup(G)
					else:
						G = kn.getGroup(op.param1)

						kn.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in kimid:
					if op.param2 in mid:
						G = cl.getGroup(op.param1)
						G.preventJoinByTicket = False
						cl.updateGroup(G)
						Ticket = cl.reissueGroupTicket(op.param1)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						cl.updateGroup(G)
					else:
						G = cl.getGroup(op.param1)

						cl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						cl.updateGroup(G)
						Ticket = cl.reissueGroupTicket(op.param1)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						cl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

        if op.type == 19:
            try:
                if op.param3 in ki2mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


                elif op.param3 in ki2mid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass


		if op.type == 19:
			try:
				if op.param3 in ki3mid:
					if op.param2 in ki2mid:
						G = ks.getGroup(op.param1)
						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)
					else:
						G = ks.getGroup(op.param1)

						ks.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki2mid:
					if op.param2 in ki3mid:
						G = kr.getGroup(op.param1)
						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)
					else:
						G = kr.getGroup(op.param1)

						kr.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki2mid:
					if op.param2 in ki4mid:
						G = kl.getGroup(op.param1)
						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)
					else:
						G = kl.getGroup(op.param1)

						kl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki2mid:
					if op.param2 in ki5mid:
						G = km.getGroup(op.param1)
						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)
					else:
						G = km.getGroup(op.param1)

						km.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki2mid:
					if op.param2 in ki6mid:
						G = kn.getGroup(op.param1)
						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kn.updateGroup(G)
					else:
						G = kn.getGroup(op.param1)

						kn.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

        if op.type == 19:
            try:
                if op.param3 in ki3mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


                elif op.param3 in Amid:
                    if op.param2 in ki3mid:
                        G = kr.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kr.updateGroup(G)
                        Ticket = kr.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kr.updateGroup(G)
                    else:
                        G = kr.getGroup(op.param1)

                        kr.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kr.updateGroup(G)
                        Ticket = kr.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kr.updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass


		if op.type == 19:
			try:
				if op.param3 in ki4mid:
					if op.param2 in ki2mid:
						G = ks.getGroup(op.param1)
						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)
					else:
						G = ks.getGroup(op.param1)

						ks.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki5mid:
					if op.param2 in ki3mid:
						G = kr.getGroup(op.param1)
						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)
					else:
						G = kr.getGroup(op.param1)

						kr.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki6mid:
					if op.param2 in ki4mid:
						G = kl.getGroup(op.param1)
						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)
					else:
						G = kl.getGroup(op.param1)

						kl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki3mid:
					if op.param2 in ki5mid:
						G = km.getGroup(op.param1)
						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)
					else:
						G = km.getGroup(op.param1)

						km.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki3mid:
					if op.param2 in ki6mid:
						G = kn.getGroup(op.param1)
						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kn.updateGroup(G)
					else:
						G = kn.getGroup(op.param1)

						kn.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki3mid:
					if op.param2 in mid:
						G = cl.getGroup(op.param1)
						G.preventJoinByTicket = False
						cl.updateGroup(G)
						Ticket = cl.reissueGroupTicket(op.param1)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						cl.updateGroup(G)
					else:
						G = cl.getGroup(op.param1)

						cl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						cl.updateGroup(G)
						Ticket = cl.reissueGroupTicket(op.param1)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						cl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

        if op.type == 19:
            try:
                if op.param3 in ki4mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


                elif op.param3 in ki4mid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass


		if op.type == 19:
			try:
				if op.param3 in ki4id:
					if op.param2 in ki2mid:
						G = ks.getGroup(op.param1)
						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)
					else:
						G = ks.getGroup(op.param1)

						ks.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						ks.updateGroup(G)
						Ticket = ks.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in ki6mid:
					if op.param2 in ki3mid:
						G = kr.getGroup(op.param1)
						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)
					else:
						G = kr.getGroup(op.param1)

						kr.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kr.updateGroup(G)
						Ticket = kr.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kr.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in op.param3:
					if op.param1 in protection:
						OWN = ""
					if op.param2 in OWN:
						kicker1 = [cl,ki,kk,ks]
						G = random.choice(kicker1).getGroup(op.param1)
						G.preventJoinByTicket = False
						random.choice(kicker1).updateGroup(G)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						random.choice(kicker1).updateGroup(G)
					else:
						G = random.choice(kicker1).getGroup(op.param1)

						random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						random.choice(kicker1).updateGroup(G)
						Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						random.choice(kicker1).updateGroup(G)
						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


				elif op.param3 in ki6mid:
					if op.param2 in ki4mid:
						G = kl.getGroup(op.param1)
						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)
					else:
						G = kl.getGroup(op.param1)

						kl.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kl.updateGroup(G)
						Ticket = kl.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kl.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

		if op.type == 19:
			try:
				if op.param3 in Amid:
					if op.param2 in ki5mid:
						G = km.getGroup(op.param1)
						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)
					else:
						G = km.getGroup(op.param1)

						km.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						km.updateGroup(G)
						Ticket = km.reissueGroupTicket(op.param1)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						km.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

				elif op.param3 in ki3mid:
					if op.param2 in ki6mid:
						G = kn.getGroup(op.param1)
						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						kn.updateGroup(G)
					else:
						G = kn.getGroup(op.param1)

						kn.kickoutFromGroup(op.param1,[op.param2])

						G.preventJoinByTicket = False
						kn.updateGroup(G)
						Ticket = kn.reissueGroupTicket(op.param1)
						ks.acceptGroupInvitationByTicket(op.param1,Ticket)
						ki.acceptGroupInvitationByTicket(op.param1,Ticket)
						kk.acceptGroupInvitationByTicket(op.param1,Ticket)
						cl.acceptGroupInvitationByTicket(op.param1,Ticket)
						G.preventJoinByTicket = True
						ks.updateGroup(G)

						wait["blacklist"][op.param2] = True
						f=codecs.open('st2__b.json','w','utf-8')
						json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

			except:
				pass

        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass

        if op.param1 in autocancel:
			OWN ="ubcd678c1e478baff8a4c453e52049dbf"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				cl.cancelGroupInvitation(op.param1,InviterX)
				ki.cancelGroupInvitation(op.param1,InviterX)
				kk.cancelGroupInvitation(op.param1,InviterX)
				ks.cancelGroupInvitation(op.param1,InviterX)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#-----------------------------
        if op.type == 32:
			OWN ="ubcd678c1e478baff8a4c453e52049dbf"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#--------------------------------------------------
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                cl.sendText(op.param1,"Do not do this.")
                try:
					kicker1 = [ki,kk,ks]
					random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])
                except:
					gfb = cl.createGroup()
					ki.inviteIntoGroup(gfb,[op.param2])
#-----------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n✪" + Name
                        wait2['ROM'][op.param1][op.param2] = "✪" + Name
                else:
                    cl.sendText
            except:
                  pass

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
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
for posts in cl.activity(1)["result"]["posts"]:
  if wait["posts"] == True:
   if posts["postInfo"]["liked"] is False:
    cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
    cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
    print u"liked" + str(i)
    i += 1
