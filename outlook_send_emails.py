import os.path
import time

import netsuite_clean_case
import win32com
from win32com.client import Dispatch, constants
from datetime import datetime
import pythoncom


class SendEmails:

    def send_amy_log(self):
        pythoncom.CoInitialize()
        # try:
        outlook = win32com.client.Dispatch('Outlook.Application')
        # except:
        #     outlook = win32com.client.GetActiveObject('Outlook.Application')
        # 创建一个item
        mail = outlook.CreateItem(0)
        # 接收人
        mail.To = "amy.xu@truecommerce.com"
        # 抄送人
        # mail.CC =  "***@outlook.com;***@outlook.com"
        # 主题
        mail.Subject = "Script closed cases log " + datetime.now().strftime("%m.%d.%Y")
        # Body
        mail.Body = "Attached is the log of noise cases closed by script today."
        # 添加附件
        filename = "./clean_list_log/" + datetime.today().strftime("%b_%d_%Y") + "_clean_list_log.txt"
        if os.path.exists(filename):
            mail.Attachments.Add(os.path.abspath(filename))
        filename = datetime.now().strftime("%b_%d_%Y") + "_resend_log.txt"
        if os.path.exists(filename):
            mail.Attachments.Add(os.path.abspath(filename))
        # 可添加多个附件
        # mail.Attachments.Add("这里是要添加附件的位置")
        # 最后发送邮件
        mail.Send()
        #
        # test1 = netsuite_clean_all_case.CleanAllCase()
        # test1.change_criteria("is not empty", "Hello")
