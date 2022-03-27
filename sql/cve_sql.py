# 导入模块 sqlite3
import sqlite3


# 数据库文件
db_file = './sql/cve.db'
# 获取数据库连接
conn = sqlite3.connect(db_file)

# 插入数据
def insert_cve_2022_data(data):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    # insert into + 表名 (列1,列2,列3,...) values(?,?,?,...)
    # sql = 'insert into cve_2022 (id, cveid, status, describe, updateTime) values(?,?,?,?,?)'
    sql = 'replace into cve_2022 (id, cveid, status, describe, updateTime) values(?,?,?,?,?)'
    # data = ('CVE-2022-0000', 1, '2.4.7 之前的 GitHub 存储库 prasathmani/tinyfilemanager 中的路径遍历。', '2022-03-27')
    cur.execute(sql, data)
    # 执行插入时，需要进行显示提交的数据，否则数据无法同步到数据库中
    conn.commit()
    cur.close()

# 删除数据
def delete_cve_2022_data():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    # delete from + 表名 where 列=?
    sql =  'delete from cve_2022 where id=?'
    # 构造元祖数据
    id = (3,)

    cur.execute(sql,id)
    conn.commit()
    cur.close()

# 修改数据，根据条件修改数据
def update_secore_data():
    # 1、获得连接
    conn = sqlite3.connect(db_file)
    # 2、打开游标，执行sql语句
    cur = conn.cursor()
    # 3、修改sql语句
    sql = 'update cve_2022 set math_cve_2022= ?, chinese_cve_2022= ? where id = 2'
    # 元祖数据封装
    data = (99,99,)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()

# 查询数据
def select_cve_2022_all(cveid):
    conn = sqlite3.connect(db_file)
    # 编写数据库语句
    sql = "select * from cve_2022 WHERE cveid = '%s'"%cveid
    # 执行sql语句
    cur = conn.cursor()
    cur.execute(sql)
    # 打印结果
    print(cur.fetchall())
    # 关闭连接,查询不需要commit,不需要同步到数据库
    cur.close()
    conn.close()

# 插入多条数据
cve_2022_list = [('Jack', 80, 90,),('Bob', 75 ,90,),('Rob', 95 ,90,),('Ceb', 78 ,90,),('Barb', 78 ,90,)]
def insert_mult_data():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    sql = 'insert into cve_2022 (stu_name, math_cve_2022, chinese_cve_2022) values(?,?,?)'
    # 需要插入多条语句时，使用的函数是executemany
    cur.executemany(sql, cve_2022_list)
    # 插入时需要调用commit进行同步提交（不然数据在内存中未提交）
    conn.commit()
    cur.close()
    conn.close()
    return cur.rowcount


# insert_cve_2022_data()
# delete_cve_2022_data()
# update_secore_data()
# select_cve_2022_all()
# print(insert_mult_data())
