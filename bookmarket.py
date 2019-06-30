#encoding=utf-8
import pymysql
import time
'''这个程序执行模拟书店功能'''

class BookMarket(object):
    # _instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super(User, cls).__new__(cls, *args, **kwargs)
    #         return cls._instance

    def __init__(self):
        '''
        初始化数据库'''
        self.connect_obj = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            database='bookmarket',
            user='root',
            password='123456',
            charset='utf8')
        self.cur = self.connect_obj.cursor()  # 操作
        #self.login_name = ''  # 登录之后的用户名
        #self.login_flag = 0  # 登陆验证

    def close(self):
        self.connect_obj.close()
        self.cur.close()
        print('Bye~')

    def CheckEmail(self,email_info):
        if '@' not in email_info:
            return False
        
        s = email_info.split('@')
        if '.zju.edu.cn' in s[1]:
            return True
        elif '.qq.com' in s[1]:
            return True
        elif '.126.com' in s[1]:
            return True
        else:
            return False

    def createUser(self,user_info):
        '''这是一个注册操作，返回一个整数'''
        ''''''
        try:
            split_info = user_info.split('&')
            new_id = split_info[0][9:]
            new_password = split_info[1][9:]
            new_email = split_info[2][6:]
            new_name = split_info[3][5:]
            new_telphone = split_info[4][9:]
        except:
            print('Transfer Data Error!')
            return 1
            
        sql_1 = 'select * from user where id = %s'
        sql_2 = 'select * from user where email = %s'
        sql_3 = 'insert user (id,pwd,email) values(%s,%s,%s)'

        try:
            ret_1 = self.cur.execute(sql_1, [new_name,])
            ret_2 = self.cur.execute(sql_2, [new_email,])
        except Exception as e:
            print(e)
            
        if len(new_name)<=6:
            print('name is below 6 bytes')
            return 2
        elif len(new_password)<=6:
            print('password is below 6 bytes')
            return 3
        elif self.CheckEmail(email_info=new_email)==False:
            print('email format is wrong')
            return 4
        elif ret_1 == 0:
            print(new_name)
            print('name has been created')
            return 5
        elif ret_2 == 0:
            print('email has been created')
            return 6
            
        try:
            ret_3 = self.cur.execute(sql_3, [new_name,new_password,new_email])
            print('create user successful')
        except Exception as e:
            print(e)
        return 0

    def login(self, user_info):
        '''这个是登录操作,返回一个布尔值'''
        #  username=zzz&password=123 取出名字和密码
        try:
            split_info = user_info.split('&')
            inname = split_info[0][9:]
            inpassword = split_info[1][9:]
        except :
            print('Transfer Data Error')
            return False

        sql = 'select * from user where id=%s and pwd=%s'
        try:
            # 参数列表化
            ret = self.cur.execute(sql, [inname, inpassword])
        except Exception as e:
            print(e)
        if ret == 0:
            print('error!')
            return False
        print('login successful')
        return True

    def get_book_data(self):
        '''这是一个遍历书籍操作'''
        print('all books in store')
        try:
            sql = '''select * from book'''
            ret = self.cur.execute(sql)
            data_str = ''
            if ret:
                rows = self.cur.fetchall()
                for row in rows:
                    for i in row:
                        data_str += str(i)
                        data_str += '&'
                    data_str += '|'
                print(data_str)
            return data_str
        except Exception as e:
            print(e)
            
    def select_book_data(self,data_info):
        '''这是一个查询书籍操作'''
        print('select book in store')
        if data_info == '':
            return ''

        try:
            s = data_info.split('&')
            sql = '''select * from book where '''
            sql = sql + s[0];
            for tr in s[1:]:
                sql = sql + ''' and ''' + tr
            ret = self.cur.execute(sql)
            data_str = ''
            if ret:
                rows = self.cur.fetchall()
                for row in rows:
                    for i in row:
                        data_str += str(i)
                        data_str += '&'
                    data_str += '|'
                print(data_str)
            return data_str
        except Exception as e:
            print(e)
    
    def add_book_data(self,book_info):
        '''这是一个添加书籍操作'''
        print('insert book')
        try:
            split_info = book_info.split('&')
            new_id = split_info[0][3:]
            new_name = book_info[1][5:]
            new_seil = split_info[2][5:]
            new_beforeprice = float(split_info[3][12:])
            new_nowprice = float(book_info[4][9:])
            new_category = int(split_info[5][9:])
            new_storm = int(split_info[6][6:])
            new_images = split_info[7][7:]
            new_introduction = split_info[8][13:]
        except:
            print('Transfer Data Error!')
            return False
        
        sql = '''insert book (id,name,seil,beforeprice,nowprice,category,storm,images,introduction) 
                    values(%s,%s,%s,%f,%f,%d,%d,%s,%s)'''
        try:
            ret = self.cur.execute(sql,[new_id,new_name,new_seil,new_beforeprice,new_nowprice,new_category,new_storm,new_images,new_introduction])
        except Exception as e:
            print(e)
        print('add book successful')
        return True

    def add_online_order(self,order_info):
        '''这是一个添加订单操作'''
        print('insert order')
        try:
            split_info = order_info.split('&')
            new_id = split_info[0][3:]
            new_bookname = book_info[1][9:]
            new_seil = split_info[2][5:]
            new_seiltel = split_info[3][8:]
            new_buy = split_info[4][4:]
            new_buytel = split_info[5][7:]
            new_num = int(book_info[6][4:])
            new_price = float(split_info[7][6:])
            new_destination = split_info[8][12:]
            new_state = int(split_info[9][5:])
        except:
            print('Transfer Data Error!')
            return False
        
        sql = '''insert book (id,bookname,seil,seiltel,buy,buytel,num,price,destination,state) 
                    values(%s,%s,%s,%s,%s,%s,%d,%f,%s,%d)'''
        try:
            ret = self.cur.execute(sql,[new_id,new_bookname,new_seil,new_seiltel,new_buy,new_buytel,new_num,new_price,new_destination,new_state])
        except Exception as e:
            print(e)
        print('add order successful')
        return True

    def update_online_order(self,order_state,order_id):
        '''这是一个更新订单状态操作'''
        print('update order state')
        try:
            sql = '''update online_order set state = %d where id = %s'''
            ret = self.cur.execute(sql,[order_state,order_id])
        except Exception as e:
            print(e)
            return False
        print('update state successful')
        return True

    def get_online_order(self,user_name):
        '''这是一个遍历个人订单操作'''
        print('show products')
        try:
            sql = '''select * from online_order where buy=%s'''
            ret = self.cur.execute(sql,[user_name,])
            data_str = ''
            if ret:
                rows = self.cur.fetchall()
                for row in rows:
                    for i in row:
                        data_str += str(i)
                        data_str += '&'
                    data_str += '|'
                print(data_str)
            return data_str
        except Exception as e:
            print(e)

if __name__ == '__main__':
    bk = BookMarket()
