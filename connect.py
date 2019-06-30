import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
import cgi
import shutil
import json
from bookmarket import BookMarket
def userReg(info):
    username=info.getvalue('username')
    password=info.getvalue('password')
    email=info.getvalue('email')
    name=info.getvalue('name')
    telphone=info.getvalue('telphone')
    reginfo=bk.createUser('username='+username+'&password='+password+'&email='+email+'&name='+name+'&telphone='+telphone)
    if reginfo==0:
        regreturn={'success':'true','maindata':{'username':username,'password':password}}
    elif reginfo==1:
        regreturn={'success':'false','maindata':'dataformerror'}
    elif reginfo==2:
        regreturn={'success':'false','maindata':'namesize'}
    elif reginfo==3:
        regreturn={'success':'false','maindata':'pswsize'}
    elif reginfo==4:
        regreturn={'success':'false','maindata':'emailformat'}
    elif reginfo==5:
        regreturn={'success':'false','maindata':'namerepeat'}
    else:
        regreturn={'success':'false','maindata':'emailrepeat'}
        
    return json.dumps(regreturn)

def userLogin(info):
    username=info.getvalue('username')
    password=info.getvalue('password')
    loginfo=bk.login('username='+username+'&password='+password)
    if loginfo==True:
        logreturn={'success':'true','maindata':{'username':username,'password':password}}
    else:
        logreturn={'success':'false','maindata':'nameorpsw'}
        
    return json.dumps(logreturn)
            
def bookSearch(info):
    bookname=info.getvalue('bookname')#需修改，可能不是书名
    bsinfo=bk.get_book_data('bookname='+bookname)
    if bsinfo:
        allbook=bsinfo.split('|')
        i=1
        bookdir={}
        for book in allbook:
            bookinfo=book.split('&')
            bookdir.update({i:{'id':bookinfo[0][3:],'bookname':bookinfo[1][5:],'sellor':bookinfo[2][7:],'beforeprice':bookinfo[3][12:],'nowprice':bookinfo[4][9:],'category':bookinfo[5][9:],'introduction':bookinfo[6][13:],'store':bookinfo[7][6:]}})
            i=i+1
        bsreturn={'success':'true','maindata':bookdir}
    else:
        bsreturn={'success':'false','maindata':''}
    
    return json.dumps(bsreturn,ensure_ascii=False)

def bookAdd(self,info):
    bookid=info.getvalue("id")
    bookname=info.getvalue("name")
    booksel=info.getvalue("sell")
    bookbp=info.getvalue("beforeprice")
    booknp=info.getvalue("nowprice")
    bookcate=info.getvalue("category")
    bookintr=info.getvalue("introduction")
    booksto=info.getvalue("store")
    bookima=info.getvalue("images")
    bookinf='id='+bookid+'&name='+bookname+'&seil='+booksel+'&beforeprice='+bookbp+'&nowprice='+booknp+'&category='+bookcate+'&storm='+booksto+'&images='+bookima+'&introduction='+bookintr
    boaddinfo=bk.add_book_data(bookinf)
    
    if boaddinfo==True:
        boaddreturn={'success':'true','maindata':''}
    else:
        boaddreturn={'success':'false','maindata':'dataformerror'}
        
    return json.dumps(boaddreturn)
            
def orderAdd(self,info):
    orderid=info.getvalue("id")
    orderbook=info.getvalue("bookname")
    ordersel=info.getvalue("sell")
    orderseltel=info.getvalue("selltel")
    orderbuy=info.getvalue("buy")
    orderbuytel=info.getvalue("buytel")
    ordernum=info.getvalue("num")
    orderpri=info.getvalue("price")
    orderdes=info.getvalue("destination")
    ordersta=info.getvalue("state")
    orderinfo='id='+orderid+'&bookname='+orderbook+'&seil='+ordersel+'&seiltel='+orderseltel+'&buy='+orderbuy+'&buytel='+orderbuytel+'&num='+ordernum+'&price='+orderpri+'&destination='+orderdes+'&state='+ordersta
    oraddinfo=bk.add_online_order(orderinf)
    if oraddinfo==False:
        oraddreturn={'success':'false','maindata':'dataformerror'}
    else:
        oraddreturn={'success':'true','maindata':''}
        
    return json.dumps(oraddreturn)

def orderSearch(self,info):
    bookaccept=info.getvalue('bookaccept')
    bsinfo=bk.get_online_order(bookaccept)
    if bainfo:
        allaccept=bsinfo.split('|')
        i=1
        orderdir={}
        for order in allaccept:
            orderinfo=order.split('&')
            orderdir.update({i:{'id':orderinfo[0][3:],'bookname':orderinfo[1][9:],'sell':orderinfo[2][5:],'selltel':orderinfo[3][8:],'buy':orderinfo[4][4:],'buytel':orderinfo[5][7:],'num':bookinfo[6][4:],'price':bookinfo[7][6:],'destination':bookinfo[8][11:],'state':bookinfo[9][6:]}})
            i=i+1
        bsreturn={'success':'true','maindata':orderdir}
    else:
        bsreturn={'success':'false','maindata':''}
    
    return json.dumps(bsreturn,ensure_ascii=False)
        

def orderUpdate(self,info):
    orderid=info.getvalue('id')
    orderstate=info.getvalue('state')
    orupinfo=bk.update_online_order(orderstate,orderid)
    if orupinfo==False:
        orupreturn={'success':'false','maindata':'exceptionoccurs'}
    else:
        orupreturn={'success':'true','maindata':''}
    return json.dumps(orupreturn)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler): 
    def do_GET(self): 
        mpath,margs=urllib.splitquery(self.path) # ?分割
        if margs==None:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_action(mpath, margs) 
    def do_POST(self): 
        mpath,margs=urllib.splitquery(self.path)
        datas = cgi.FieldStorage(fp = self.rfile,headers = self.headers,environ = {'REQUEST_METHOD': 'POST'})
        self.do_action(mpath, datas)
        
    def do_action(self, path, args):
        operation=args.getvalue('operation')
        if operation=='login':
            sendata=userLogin(args)
        elif operation=='register':
            sendata=userReg(args)
        elif operation=='addorder':
            sendata=orderAdd(args)
        elif operation=='addbook':
            sendata=bookAdd(args)
        elif operation=='searchorder':
            sendata=orderSearch(args)
        elif operation=='searchbook':
            sendata=bookSearch(args)
        elif operation=='updateoder':
            sendata=orderUpdate(args)
        dh = dataHandler()
        result = dh.run(path, sendata)
        self.outputtxt(result)
        
    def outputtxt(self, content):
        enc = "UTF-8"  #指定返回编码
        content = content.encode(enc)               
        f = io.BytesIO()
        f.write(content)
        f.seek(0)  
        self.send_response(200)  
        self.send_header("Content-type", "text/html; charset=%s" % enc)  
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()  
        shutil.copyfileobj(f,self.wfile)
        f.close()
        #self.wfile.write(content)            
 
bk = BookMarket()           
httpd = SocketServer.TCPServer(("127.0.0.1", 3000), ServerHandler) 
httpd.serve_forever() 
