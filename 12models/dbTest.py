#!D:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/9/26 22:32
# @Author : Su Chunyu
# @File : dbTest.py
# @Software: PyCharm
import pandas as pd
import pymysql

# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='abc123',
#                      database='FraudPreventionSystem',
#                      charset='utf8')
#
#
# # 查询语句
# try:
#     cursor = db.cursor()
#     sql = "show full tables"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for data in result:
#         print(data)
# except Exception:
#     print("查询失败")




if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # db = pymysql.connect('System.db')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='abc123',
                         database='FraudPreventionSystem',
                         charset='utf8')

    cursor = db.cursor()

    pd_con = pd.read_sql('select username, usercode from user', db)
    print(pd_con)
    # user_dic = pd_con.set_index('username').to_dict()['usercode']
    # print(user_dic)
    #
    # user = Entry()
    # root_log = tk.Tk()
    # root_log.title("登陆界面")
    # root_log.geometry('500x300')
    # ttk.Label(root_log, text='欢迎登陆购物车系统').place(x=80, y=50)
    # ttk.Label(root_log, text='用户名').place(x=80, y=100)
    # ttk.Label(root_log, text='密码').place(x=80, y=150)
    # v1 = tk.StringVar()
    # v2 = tk.StringVar()
    # entry_username = ttk.Entry(root_log, textvariable=v1)
    # entry_username.place(x=140, y=100)
    # entry_password = ttk.Entry(root_log, textvariable=v2, show='*')
    # entry_password.place(x=140, y=150)
    # button_confirm = ttk.Button(root_log, text='登陆', command=user.login)
    # button_confirm.place(x=280, y=200)
    # button_confirm = ttk.Button(root_log, text='游客登陆', command=user.guide)
    # button_confirm.place(x=80, y=200)
    # button_confirm = ttk.Button(root_log, text='注册', command=user.signup)
    # button_confirm.place(x=180, y=200)
    # button_confirm = ttk.Button(root_log, text='退出', command=user.quit)
    # button_confirm.place(x=380, y=200)
    # root_log.mainloop()