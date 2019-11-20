import os
import win32com.client as win32
import datetime
from readConfig import ReadConfig
import getpathInfo
from common.Log import logger


read_conf = ReadConfig().get_mail()
subject = read_conf["subject"]#从配置文件中读取，邮件主题
app = read_conf["app"]#从配置文件中读取，邮件类型
address = read_conf["address"]#从配置文件中读取，邮件收件人
cc = read_conf["cc"]#从配置文件中读取，邮件抄送人
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
logger = logger

class send_email():
    def foxmail(self):
        fox = win32.Dispatch("%s.Application" % app)
        mail = fox.CreateItem(win32.constants.olMailItem)
        mail.To = addressee # 收件人
        mail.CC = cc # 抄送
        #mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject  #邮件主题
        mail_Subject = subject
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        content = """
                    执行测试中……
                    测试已完成！！
                    生成报告中……
                    报告已生成……
                    报告已邮件发送！！
                    """
        mail.Body = content
        mail.Send()
        print('send email ok!!!!')
        logger.info('send email ok!!!!')


if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
    print(subject)
    send_email().foxmail()
    print("send email ok!!!!!!!!!!")