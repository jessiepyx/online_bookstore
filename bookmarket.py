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
        try:
            split_info = user_info.split('&')
            new_name = split_info[0][9:]
            new_password = split_info[1][9:]
            new_email = split_info[2][6:]
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
        print('show products')
        try:
            sql = '''select * from book'''
            ret = self.cur.execute(sql)
            if ret:
                data_str = ''
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
        print('show products')
        try:
            s = data_info.split('&')
            sql = '''select * from book where '''
            sql = sql + s[0];
            for tr in s[1:]:
                sql = sql + ''' and ''' + tr
            ret = self.cur.execute(sql)
            if ret:
                data_str = ''
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
        print('add products')
        try:
            split_info = book_info.split('&')
            new_id = split_info[0][3:]
            new_name = book_info[1][5:]
            new_seilor = split_info[2][6:]
            new_beforeprice = float(split_info[3][11:])
            new_nowprice = float(book_info[4][8:])
            new_category = split_info[5][8:]
            new_introduction = split_info[6][12:]
            new_storm = split_info[7][6:]
        except:
            print('Transfer Data Error!')
            return False
        
        sql = '''insert book (id,name,seilor,beforeprice,nowprice,category,introduction,storm) 
                    values(%s,%s,%s,%f,%f,%s,%s,%s)'''
        try:
            ret = self.cur.execute(sql,[new_id,new_name,new_seilor,new_beforeprice,new_nowprice,new_category,new_introduction,new_storm])
        except Exception as e:
            print(e)
        print('add book successful')
        return True

    def add_online_order(self,order_info):
        '''这是一个添加订单操作'''
        print('add order')
        try:
            split_info = order_info.split('&')
            new_id = split_info[0][3:]
            new_name = book_info[1][5:]
            new_bookmaster = split_info[2][10:]
            new_bookaccept = split_info[3][10:]
            new_num = int(book_info[4][3:])
            new_price = float(split_info[5][6:])
            new_destination = split_info[6][11:]
            new_mastertel = split_info[7][9:]
            new_accepttel = split_info[8][9:]
            new_state = int(split_info[9][5:])
        except:
            print('Transfer Data Error!')
            return False
        
        sql = '''insert book (id,name,bookmaster,bookaccept,num,price,destination,mastertel,accepttel,state) 
                    values(%s,%s,%s,%s,%d,%f,%s,%s,%s,%d)'''
        try:
            ret = self.cur.execute(sql,[new_id,new_name,new_bookmaster,new_bookaccept,new_num,new_price,new_destination,new_mastertel,new_accepttel,new_state])
        except Exception as e:
            print(e)
        print('add order successful')
        return True

    def update_online_order(self,order_state,order_id):
        '''这是一个更新订单状态操作'''
        print('show products')
        try:
            sql = '''update online_order set state = %s where id = %s'''
            ret = self.cur.execute(sql,[order_state,order_id])
        except Exception as e:
            print(e)
            return False
        print('update state successful')
        return True

    def get_online_order(self,order_info):
        '''这是一个遍历个人订单操作'''
        print('show products')
        try:
            sql = '''select * from book where bookaccept=%s'''
            ret = self.cur.execute(sql,[order_info,])
            if ret:
                data_str = ''
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