
import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from PIL import Image, ImageTk
from PyQt5.QtWidgets import QApplication
import sys
# from shop import *
# from cart import *
import threading


class Entry():
    def login(self):
        global username
        username = v1.get()
        user_pwd = v2.get()
        if username in user_dic:
            if user_pwd == user_dic[username]:
                tk.messagebox.showinfo(title='welcome', message='欢迎进入')
                root_log.destroy()
                self.custom()
            else:
                tk.messagebox.showerror(title='error', message='密码错误')
        elif username == ''or user_pwd == '':
            tk.messagebox.showerror(title='error', message='用户名或密码为空')
        else:
            signup = tk.messagebox.askyesno(
                title='error', message='您还没有注册，是否现在注册')
            if signup:
                self.signup()


    def signup(self):   # 注册函数
        def signup():
            nname = v3.get()
            npwd = v4.get()
            npwd2 = v5.get()
            ntel = v6.get()
            naddress = v7.get()
            if nname in user_dic:
                tk.messagebox.showerror('错误', '用户名已存在')
            elif nname == '' or npwd == '':
                tk.messagebox.showerror('错误', '用户名或密码为空')
            elif npwd != npwd2:
                tk.messagebox.showerror('错误', '两次密码不一致')
            else:
                user_dic[nname] = npwd
                tk.messagebox.showinfo('成功', '注册成功')
                db.execute("insert into user values (?,?,?,?)",
                           (nname, npwd, ntel, naddress))
                db.commit()
                root_signup.destroy()

        root_signup = tk.Toplevel(root_log)
        root_signup.title('注册界面')
        root_signup.geometry('450x500')
        v3 = tk.StringVar()
        v4 = tk.StringVar()
        v5 = tk.StringVar()
        v6 = tk.StringVar()
        v7 = tk.StringVar()
        ttk.Label(root_signup, text='欢迎进入注册页面！').place(x=50, y=50)
        ttk.Label(root_signup, text='用户名').place(x=30, y=100)
        ttk.Entry(root_signup, textvariable=v3).place(x=150, y=100)
        ttk.Label(root_signup, text='输入密码').place(x=30, y=150)
        ttk.Entry(root_signup, textvariable=v4, show='*').place(x=150, y=150)
        ttk.Label(root_signup, text='再次输入密码').place(x=30, y=200)
        ttk.Entry(root_signup, textvariable=v5, show='*').place(x=150, y=200)
        ttk.Label(root_signup, text='手机号码').place(x=30, y=250)
        ttk.Entry(root_signup, textvariable=v6).place(x=150, y=250)
        ttk.Label(root_signup, text='收货地址').place(x=30, y=300)
        ttk.Entry(root_signup, textvariable=v7).place(x=150, y=300)
        button_sign = ttk.Button(root_signup, text='确认注册', command=signup)
        button_sign.place(x=100, y=400)

    def quit(self):
        root_log.quit()

    def show_error(self):
        tk.messagebox.showerror('error', '请登陆')

    def guide(self):
        mainwindow = tk.Tk()
        mainwindow.title('主界面')
        mainwindow.geometry('500x500')
        ttk.Label(mainwindow, text='欢迎进入购物车系统').place(x=100, y=100)
        command_mall = ttk.Button(
            mainwindow, text='商城', command=self.show_error)
        command_mall.place(x=100, y=150)
        command_cart = ttk.Button(
            mainwindow, text='购物车', command=self.show_error)
        command_cart.place(x=100, y=200)
        command_self = ttk.Button(
            mainwindow,
            text='个人中心',
            command=self.show_error)
        command_self.place(x=100, y=250)
        mainwindow.mainloop()

    def custom(self):
        '''

        :return:
        '''
        mainwindow = tk.Tk()
        mainwindow.title('主界面')
        mainwindow.geometry('500x500')
        ttk.Label(mainwindow, text='欢迎进入购物车系统').place(x=100, y=100)
        command_mall = ttk.Button(mainwindow, text='商城', command=self.shop)
        command_mall.place(x=100, y=150)
        command_cart = ttk.Button(mainwindow, text='购物车', command=self.cart)
        command_cart.place(x=100, y=200)
        command_self = ttk.Button(mainwindow, text='个人中心', command=self.info)
        command_self.place(x=100, y=250)
        mainwindow.mainloop()

    # def shop(self):
    #     shop = Shop(username, db, cursor)
    #     shop.show()

    # def cart(self):
    #     cart = Cart(username, db, cursor)
    #     cart.show()


    def info(self):
        '''

        :return:
        '''
        name = username
        sql = '''SELECT TEL FROM USER WHERE (USERNAME=:username)'''
        cursor.execute(sql, {'username': name})
        db.commit()
        tel = cursor.fetchone()
        sql2 = '''SELECT address from user where (username=:username)'''
        cursor.execute(sql2, {'username': name})
        address = cursor.fetchone()

        def edit_tel():
            def save_tel():
                new_tel = v1.get()
                sql = '''update user set tel=:s_tel where(username=:username)'''
                cursor.execute(sql, {'s_tel': new_tel, 'username': name})
                db.commit()
                tk.messagebox.showinfo(title='HI', message='修改成功！')
            showwindow = tk.Toplevel()
            showwindow.title('编辑电话号码')
            showwindow.geometry('300x200')
            v1 = tk.StringVar()
            #img_open = Image.open('school3.png')
            #photo3 = ImageTk.PhotoImage(img_open)
            #ttk.Label(showwindow, image=photo3).place(x=0, y=0)
            tk.Entry(showwindow, textvariable=v1).place(x=85, y=80)
            tk.Button(
                showwindow,
                text='确认',
                font=(
                    "楷体",
                    10),
                width=5,
                height=2,
                command=save_tel).place(
                x=130,
                y=110)
            showwindow.mainloop()

        def edit_address():
            def save_address():
                new_address = v2.get()
                sql = '''update user set address=:s_address where(username=:username)'''
                cursor.execute(
                    sql, {
                        's_address': new_address, 'username': name})
                db.commit()
                tk.messagebox.showinfo(title='HI', message='修改成功！')
            showwindow = tk.Toplevel()
            showwindow.title('编辑个人地址')
            showwindow.geometry('300x200')
            v2 = tk.StringVar()
            #img_open = Image.open('school3.png')
            #photo2 = ImageTk.PhotoImage(img_open)
            #ttk.Label(showwindow, image=photo2).place(x=0, y=0)
            tk.Entry(showwindow, textvariable=v2).place(x=85, y=80)
            tk.Button(
                showwindow,
                text='确认',
                font=(
                    "楷体",
                    10),
                width=5,
                height=2,
                command=save_address).place(
                x=130,
                y=110)
            showwindow.mainloop()

        window = tk.Toplevel()
        window.geometry('500x300')
        window.title('个人中心')
        # window框
        ttk.Label(
            window,
            text='您的用户名是：',
            font=(
                "楷体",
                13),
            background="lemonchiffon").place(
                x=50,
            y=50)
        ttk.Label(
            window,
            text=username,
            font=(
                "黑体",
                12),
            background="lemonchiffon").place(
                x=210,
            y=50)
        # 用户名及内容
        ttk.Label(
            window,
            text='您的电话号码是：',
            font=(
                "楷体",
                13),
            background="lemonchiffon").place(
                x=50,
            y=130)
        ttk.Label(
            window,
            text=tel,
            font=(
                "黑体",
                12),
            background="lemonchiffon").place(
                x=210,
            y=130)
        # 电话号码及内容
        ttk.Label(
            window,
            text='您的收货地址是：',
            font=(
                "楷体",
                13),
            background="lemonchiffon").place(
                x=50,
            y=210)
        ttk.Label(
            window,
            text=address,
            font=(
                "黑体",
                12),
            background="lemonchiffon").place(
                x=210,
            y=210)

        # 用户地址及内容
        # showwindow框，修改地址和电话号码

        tk.Button(
            window,
            text='编辑电话号码',
            width=12,
            height=1,
            command=edit_tel).place(
            x=320,
            y=130)
        tk.Button(
            window,
            text='编辑收货地址',
            width=12,
            height=1,
            command=edit_address).place(
            x=320,
            y=210)
        window.mainloop()


# Copyright(c)2019 Su Chunyu
if __name__ == '__main__':

    app = QApplication(sys.argv)
    db = sqlite3.connect('shop.db')

    cursor = db.cursor()

    pd_con = pd.read_sql('select username, usercode from user', db)
    print(pd_con)
    user_dic = pd_con.set_index('username').to_dict()['usercode']
    print(user_dic)

    user = Entry()
    root_log = tk.Tk()
    root_log.title("登陆界面")
    root_log.geometry('500x300')
    ttk.Label(root_log, text='欢迎登陆购物车系统').place(x=80, y=50)
    ttk.Label(root_log, text='用户名').place(x=80, y=100)
    ttk.Label(root_log, text='密码').place(x=80, y=150)
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    entry_username = ttk.Entry(root_log, textvariable=v1)
    entry_username.place(x=140, y=100)
    entry_password = ttk.Entry(root_log, textvariable=v2, show='*')
    entry_password.place(x=140, y=150)
    button_confirm = ttk.Button(root_log, text='登陆', command=user.login)
    button_confirm.place(x=280, y=200)
    button_confirm = ttk.Button(root_log, text='游客登陆', command=user.guide)
    button_confirm.place(x=80, y=200)
    button_confirm = ttk.Button(root_log, text='注册', command=user.signup)
    button_confirm.place(x=180, y=200)
    button_confirm = ttk.Button(root_log, text='退出', command=user.quit)
    button_confirm.place(x=380, y=200)
    root_log.mainloop()