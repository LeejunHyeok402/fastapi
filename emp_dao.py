import pymysql
class EmpDao:
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',port=3305, user='root', password='python',
                    db='python', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        self.curs = self.conn.cursor()
            
    def selects(self):
        sql = "select e_id,e_name,sex,addr from emp"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
    
    def select(self,e_id):
        sql = f"""select
                    e_id,
                    e_name,
                    sex,
                    addr 
                from emp 
                where 
                    e_id = '{e_id}'"""
        self.curs.execute(sql)
        row = self.curs.fetchall()
        return row[0]
    
    def insert(self,e_id,e_name,sex,addr):
        sql = f"""INSERT INTO 
                emp(e_id,e_name,sex,addr) 
                VALUES  ('{e_id}','{e_name}','{sex}','{addr}');"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,e_id,e_name,sex,addr):
        sql = f"""update emp
                    set 
                    e_name = '{e_name}', sex='{sex}', addr='{addr}'
                    where e_id='{e_id}'; """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
                DELETE 
                FROM emp 
                WHERE e_id='{e_id}';"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
    