import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
import cgi
import shutil
import json
from bookmarket import BookMarket
def userReg(info):
    username=info['username']
    password=info['password']
    email=info['email']
    name=info.getvalue('name']
    telphone=info['telphone']
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
    username=info['username']
    password=info['password']
    loginfo=bk.login('username='+username+'&password='+password)
    if loginfo==True:
        logreturn={'success':'true','maindata':{'username':username,'password':password}}
    else:
        logreturn={'success':'false','maindata':'nameorpsw'}
        
    return json.dumps(logreturn)
            
def bookSearch(info):
    bookname=info['bookname']#需修改，可能不是书名
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
    bookid=info["id"]
    bookname=info["name"]
    booksel=info["sell"]
    bookbp=info["beforeprice"]
    booknp=info["nowprice"]
    bookcate=info["category"]
    bookintr=info["introduction"]
    booksto=info["store"]
    bookima=info["images"]
    bookinf='id='+bookid+'&name='+bookname+'&seil='+booksel+'&beforeprice='+bookbp+'&nowprice='+booknp+'&category='+bookcate+'&storm='+booksto+'&images='+bookima+'&introduction='+bookintr
    boaddinfo=bk.add_book_data(bookinf)
    
    if boaddinfo==True:
        boaddreturn={'success':'true','maindata':''}
    else:
        boaddreturn={'success':'false','maindata':'dataformerror'}
        
    return json.dumps(boaddreturn)
            
def orderAdd(self,info):
    orderid=info["id"]
    orderbook=info["bookname"]
    ordersel=info["sell"]
    orderseltel=info["selltel"]
    orderbuy=info["buy"]
    orderbuytel=info["buytel"]
    ordernum=info["num"]
    orderpri=info["price"]
    orderdes=info["destination"]
    ordersta=info["state"]
    orderinfo='id='+orderid+'&bookname='+orderbook+'&seil='+ordersel+'&seiltel='+orderseltel+'&buy='+orderbuy+'&buytel='+orderbuytel+'&num='+ordernum+'&price='+orderpri+'&destination='+orderdes+'&state='+ordersta
    oraddinfo=bk.add_online_order(orderinf)
    if oraddinfo==False:
        oraddreturn={'success':'false','maindata':'dataformerror'}
    else:
        oraddreturn={'success':'true','maindata':''}
        
    return json.dumps(oraddreturn)

def orderSearch(self,info):
    bookaccept=info['buy']
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
    orderid=info['id']
    orderstate=info['state']
    orupinfo=bk.update_online_order(orderstate,orderid)
    if orupinfo==False:
        orupreturn={'success':'false','maindata':'exceptionoccurs'}
    else:
        orupreturn={'success':'true','maindata':''}
    return json.dumps(orupreturn)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler): 
    def do_OPTIONS(self):
        self.send_response(200)   
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type")
    def do_GET(self): 
        mpath,margs=urllib.splitquery(self.path) # ?分割
        if margs==None:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_action(mpath, margs) 
            
    def do_POST(self): 
        mpath,margs=urllib.splitquery(self.path)
       # datas = cgi.FieldStorage(fp = self.rfile,headers = self.headers,environ = {'REQUEST_METHOD': 'POST'})
        datas = self.rfile.read(int(self.headers['content-length']))
        jsondatas=json.load(datas)
        self.do_action(mpath, jsondatas)
        #line = self.rfile.readline()
      #  self.do_action(mpath, line)

        
    def do_action(self, path, args):
        operation=args['operation']
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
        self.outputtxt(sendata)
            '''
        dh = dataHandler()
        result = dh.run(path, sendata)
        self.outputtxt(result)
        '''
        
    def outputtxt(self, content):
        enc = "UTF-8"  #指定返回编码
        content = content.encode(enc)               
        f = io.BytesIO()
        f.write(content)
        f.seek(0)  
        self.send_response(200)  
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Content-type", "text/html; charset=%s" % enc)  
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()  
        shutil.copyfileobj(f,self.wfile)
        f.close()
        #self.wfile.write(content)            
 
bk = BookMarket()           
httpd = SocketServer.TCPServer(("127.0.0.1", 3000), ServerHandler) 
httpd.serve_forever() 
