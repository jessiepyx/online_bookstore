import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
import shutil
import json
from bookmartket import BookMarket
def userReg(info):
    username=info.getvalue('username')
    password=info.getvalue('password')
    email=info.getvalue('email')
    reginfo=bk.createUser('username='+username+'&password='+password+'&email='+email)
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
            bookdir.update({i:{'bookname':bookinfo[1],'sellor':bookinfo[2],'beforeprice':bookinfo[3],'nowprice':bookinfo[4],'category':bookinfo[5],'introduction':bookinfo[6],'store':bookinfo[7]}})
        bsreturn={'success':'true','maindata':bookdir}
    else:
        bsreturn={'success':'false','maindata':''}
    
    return json.dumps(bsreturn,ensure_ascii=False)
            
def orderAdd(self,info):
    #info处需修改
    oraddinfo=bk.add_online_order(info)
    if oraddinfo==False:
        oraddreturn={'success':'false','maindata':'dataformerror'}
    else:
        oraddreturn={'success':'true','maindata':''}
        
    return json.dumps(oraddreturn)

def orderSearch(self,info):
    bookaccept=info.getvalue('bookaccept')
    bsinfo=bk.get_book_data(bookaccept)
    if bainfo:
        allaccept=bsinfo.split('|')
        i=1
        bookdir={}
        for book in allbook:
            bookinfo=book.split('&')
            bookdir.update({i:{'bookname':bookinfo[1],'bookmaster':bookinfo[2],'bookaccept':bookinfo[3],'num':bookinfo[4],'price':bookinfo[5],'destination':bookinfo[6],'mastertel':bookinfo[7],'accepttel':bookinfo[8]}})
        bsreturn={'success':'true','maindata':bookdir}
    else:
        bsreturn={'success':'false','maindata':''}
    
    return json.dumps(bsreturn,ensure_ascii=False)
        
    return json.dumps(oraddreturn)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler): 
    def do_GET(self): 
        mpath,margs=urllib.splitquery(self.path) # ?分割
        if margs==None:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_action(mpath, margs) 
    def do_POST(self): 
        mpath,margs=urllib.splitquery(self.path)
        datas = self.rfile.read(int(self.headers['content-length']))
        self.do_action(mpath, datas)
        
    def do_action(self, path, args):
        operation=args.getvalue('operation')
        if operation=='login':
            sendata=userLogin(args)
        elif operation=='register':
            sendata=userReg(args)
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
        self.end_headers()  
        shutil.copyfileobj(f,self.wfile)
        f.close()
        #self.wfile.write(content)            
 
bk = BookMarket()           
httpd = SocketServer.TCPServer(("127.0.0.1", 3306), ServerHandler) 
httpd.serve_forever() 
