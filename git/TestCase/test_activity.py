import os
import time
from time import sleep
from selenium.webdriver.support.ui import Select

from selenium import webdriver
# 代码修改记录：20190622时间控件后添加点击确定按钮

#基本信息
acc_name='活动ZH'+time.strftime('%m%d%H%M',time.localtime(time.time()))#活动名称
print(acc_name)
acc_start_time_row = 3  #tr[5]/td[2]  为20号，一天换一个，  (5为添加星期的行)
acc_start_time_col = 3  #tr[5]/td[2]  为20号，一天换一个，  (2为添加日期控件的列)

driver = webdriver.Chrome()
driver.maximize_window()#最大化
driver.get("http://192.168.109.200:22001/isc_sso/login?service=http://192.168.108.170:20080/web/")
sleep(4)
driver.find_element_by_id('username').send_keys('gwsc14')
driver.find_element_by_id('password').send_keys('PH2019.com')
driver.find_element_by_id('submi').click()
sleep(8)
#####通过双创活动创建活动
# driver.find_element_by_xpath('//*[@id="menu"]/span[5]/a').click()#双创活动
# sleep(4)
# driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/ul/li[3]').click()#赛事支撑
# sleep(4)
# driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/p').click()#发布活动
#############企业中心创建活动
driver.find_element_by_xpath('//*[@id="public-header"]/div[1]/div[2]/ul/li[4]').click()#企业中心
sleep(2)
driver.find_element_by_xpath('//*[@id="informationPage"]/section/aside/div/div[6]/div/span[2]').click()#点击活动
sleep(1)
driver.find_element_by_xpath('//*[@id="informationPage"]/section/aside/div/div[6]/div[2]/div[1]/div/span[2]').click()#点击我发起的活动
sleep(2)
driver.find_element_by_xpath('//*[@id="listactivitieslaunched"]/div[2]/div[3]/button[2]').click()#点击新建
sleep(1)
Select(driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div[2]/p/select')).select_by_visible_text("赛事支撑")#活动类型选择赛事支撑
sleep(1)
driver.find_element_by_xpath('//div[7]/*[@id="model-frame"]/div[3]/button[2]').click()#点击确定
sleep(4)
###############基本信息
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[1]/p/input').send_keys(acc_name)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[3]/p/input').send_keys('活动副标题')
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[7]/div').click()#活动范围的...
sleep(1)
driver.find_element_by_xpath('//*[@id="contact-frame"]/div[2]/div/div[1]/div/div/div/span[2]').click()#活动范围选择全活动
driver.find_element_by_xpath('//*[@id="checkboxName"]').click()#勾选是否含子单位
driver.find_element_by_xpath('//*[@id="contact-frame"]/div[3]/button[2]').click()#点击确定
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[9]/div').click()#主办方的...
sleep(1)
driver.find_element_by_xpath('//div[3]/div[@id="contact-frame"]/div[2]/div[2]/ul/li[1]/span').click()#主办方选择全社会
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[9]/input').send_keys('主办部门')#录入主办部门
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[11]/div/div').click()#承办方的...
sleep(2)
driver.find_element_by_xpath('//div[4]/div[@id="contact-frame"]/div[2]/div[2]/ul/li[1]/span').click()#承办方选择全社会
sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[11]/div/input').send_keys('承办部门')#录入承办部门
sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[14]/div[1]/input').click()#打开活动开始时间控件
sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col)+']').click()#录入开始时间,第五行第二列 20
driver.find_element_by_xpath('/html/body/div[2]/div[2]/button[2]/span').click()#点击确定按钮

driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[14]/div[2]/input').click()#打开活动结束时间控件
sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[3]/table[1]/tbody/tr[7]/td[7]').click()#录入结束时间(当前日期控件可展示的最后一天，非当月最后一天)

driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]/span').click()#点击确定
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[16]/div[2]/textarea').send_keys('活动简介')
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[18]/div[2]/textarea').send_keys('活动要求')
sleep(1)
#活动海报
filepath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# os.path.split(path)[0]获取文件的父级路径
# os.path.dirname(path)获取路径去掉文件名的路径(只要文件夹)
# os.path.abspath(__file__)获取__file__绝对路径
driver.find_element_by_id('FileUpload').send_keys(filepath + "\data\Penguins.jpg")#活动海报上传
sleep(6)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[22]/div/button').click()#点击下一步
sleep(4)
###############活动配置
#######活动报名
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[2]/div[1]/div[1]/input').click()#打开活动报名开始时间控件
sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col)+']').click()#录入活动报名开始时间,第五行第二列 20
driver.find_element_by_xpath('/html/body/div[4]/div[2]/button[2]/span').click()
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[2]/div[1]/div[2]/input').click()#打开活动报名结束时间控件
sleep(1)
if acc_start_time_col == 7:
    # 录入活动报名结束时间(若活动开始时间为日期控件最后一列，则结束日期为下一行的第一列)
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row+1)+']/td[1]').click()
else:
    # 录入活动报名结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col+1)+']').click()
driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[2]/span').click()

sleep(1)
driver.find_element_by_xpath('//*[@id="zizhu"]').click()#活动报名-自主报名
driver.find_element_by_xpath('//*[@id="zihuodong"]').click()#活动报名-子活动上报
sleep(1)
#######题目抽选
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[1]/div[1]/input').click()#打开题目抽选开始时间控件
sleep(1)
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col)+']').click()#录入题目抽选开始时间,与活动报名时间一样
driver.find_element_by_xpath('/html/body/div[6]/div[2]/button[2]/span').click()#点击确定
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[1]/div[2]/input').click()#打开题目抽选结束时间控件
sleep(1)
if acc_start_time_col==7:
    # 录入题目抽选结束时间(若活动开始时间为日期控件最后一列，则结束日期为下一行的第一列)
    driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row+1)+']/td[1]').click()
else:
    # 录入题目抽选结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
    driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col+1)+']').click()
driver.find_element_by_xpath('/html/body/div[7]/div[2]/button[2]/span').click()#点击确定
sleep(1)
driver.find_element_by_xpath('//div[@class="fileW1"]/div[@id="fileUpload_test"]/form/input').send_keys(filepath + "\data\zuopin.zip")#题目抽选上传题目点击上传
sleep(7)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[4]/div[2]/div[3]/button').click()# 点击上传
driver.find_element_by_xpath('//*[@id="suiji"]').click()#抽取规则-随机抽取
# driver.find_element_by_xpath('//*[@id="ziyou"]"]').click()#抽取规则-自由选择

########作品申报
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[6]/div[1]/div[1]/input').click()#打开作品申报开始时间控件
sleep(1)
driver.find_element_by_xpath('/html/body/div[8]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col)+']').click()#录入作品申报开始时间,与活动报名时间一样
driver.find_element_by_xpath('/html/body/div[8]/div[2]/button[2]/span').click()#点击确定
sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[6]/div[1]/div[2]/input').click()#打开作品申报结束时间控件
sleep(2)
if acc_start_time_col == 7:
    # 录入作品申报结束时间(若活动开始时间为日期控件最后一列，则结束日期为下一行的第一列)
    driver.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row+1)+']/td[1]').click()
else:
    # 录入作品申报结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
    driver.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col+1)+']').click()
    # '//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[1]/div[2]/input'
driver.find_element_by_xpath('/html/body/div[9]/div[2]/button[2]/span').click()#点击确定
sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[7]/button').click()#作品申报-申报上限-未设置
sleep(1)
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[2]/input').clear()#作品申报-申报上线限-个人内部项目-清空
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[2]/input').send_keys("100")#作品申报-申报上线限-个人内部项目
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[3]/input').clear()#作品申报-申报上线限-个人外部项目--清空
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[3]/input').send_keys("100")#作品申报-申报上线限-个人外部项目
sleep(1)
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[4]/input').clear()#作品申报-申报上线限-企业内部项目--清空
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[4]/input').clear()#作品申报-申报上线限-企业外部项目--清空
sleep(1)
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[4]/input').send_keys("100")#作品申报-申报上线限-企业内部项目
sleep(1)
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[5]/input').clear()#作品申报-申报上线限-企业外部项目--清空
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[5]/input').clear()#作品申报-申报上线限-企业外部项目--清空
sleep(1)
driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[5]/input').send_keys("100")#作品申报-申报上线限-企业外部项目
sleep(1)
driver.find_element_by_xpath('//*[@id="model-frame"]/div[3]/div/button').click()#作品申报-申报上线限-确定
sleep(1)
driver.find_element_by_xpath('//*[@id="youthGame"]').click()#作品申报-选择申报表-青创赛申请表
# driver.find_element_by_xpath('//*[@id="commonExal"]').click()#作品申报-选择申报表-普通申请表
#########比赛评审
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[9]/div[2]/div[1]/input').click()#打开比赛评审开始时间控件
sleep(1)
if acc_start_time_col >= 6:
    # 录入比赛评审开始时间(若比赛评审时间为作品提交结束时间加一,活动开始时间加二；若活动开始时间列号>=6，行号加一，列号+2-7)
    driver.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row+1)+']/td['+str(acc_start_time_col-5)+']').click()
else:
    sleep(1)
    # 录入比赛评审开始时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
    driver.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col+2)+']').click()
driver.find_element_by_xpath('/html/body/div[10]/div[2]/button[2]/span').click()#点击确定
# sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[9]/div[2]/div[2]/input').click()#打开比赛评审结束时间控件
sleep(1)
if acc_start_time_col >= 5:
    # 录入比赛评审结束时间(比赛评审时间为作品提交结束时间加二,活动开始时间加三；若活动开始时间列号>=5，行号加一，列号+3-7)
    driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row+1)+']/td['+str(acc_start_time_col-4)+']').click()
else:
    # 录入比赛评审开始时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加3)
    driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col+3)+']').click()
driver.find_element_by_xpath('/html/body/div[11]/div[2]/button[2]/span').click()#点击确定
sleep(1)
########获奖公示
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[10]/div[2]/div[1]/div[1]/input').click()#打开获奖公示开始时间控件
sleep(1)
if acc_start_time_col >= 4:
    # 录入获奖公示开始时间(若获奖公示时间为作品提交结束时间加3,活动开始时间加4；若活动开始时间列号>=4，行号加一，列号+5-7)
    driver.find_element_by_xpath('/html/body/div[12]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row+1)+']/td['+str(acc_start_time_col-3)+']').click()

else:
    # 录入获奖公示开始时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加4)
    driver.find_element_by_xpath('/html/body/div[12]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col+4)+']').click()
driver.find_element_by_xpath('/html/body/div[12]/div[2]/button[2]/span').click()#点击确定
sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[10]/div[2]/div[1]/div[2]/input').click()#打开获奖公示结束时间控件
sleep(1)
if acc_start_time_col >= 3:
    # 录入获奖公示结束时间(获奖公示时间为作品提交时间加二,活动开始时间加三；若活动开始时间列号>=5，行号加一，列号+5-7)
    driver.find_element_by_xpath('/html/body/div[13]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row+1)+']/td['+str(acc_start_time_col-2)+']').click()
else:
    # 录入获奖公示结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加3)
    driver.find_element_by_xpath('/html/body/div[13]/div[1]/div/div[3]/table[1]/tbody/tr['+str(acc_start_time_row)+']/td['+str(acc_start_time_col+5)+']').click()
driver.find_element_by_xpath('/html/body/div[13]/div[2]/button[2]/span').click()#点击确定
sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[10]/div[3]/div').click()#获奖公示-通知范围的...
sleep(2)
driver.find_element_by_xpath('//div[5]/div[@id="contact-frame"]/div[2]/div/div[1]/div/div/div[1]/span[2]').click()#获奖公示-通知范围-全社会
sleep(1)
driver.find_element_by_xpath('//div[5]/div/div[2]/div/div[2]/ul/li/span[2]/input[@id="checkboxName"]').click()#勾选是否含子单位
sleep(1)
driver.find_element_by_xpath('//div[5]/*[@id="contact-frame"]/div[3]/button[2]').click()#点击确定
sleep(2)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[11]/input[2]').click()#点击下一步
sleep(1)
driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[4]/div[2]/div/input[2]').click()#点击发起活动
sleep(1)
driver.find_element_by_xpath('//div[1]/div[@id="model-frame"]/div[3]/button[2]').click()#确定发起活动

#################################################进行活动审核

driver.get("http://192.168.109.200:22001/isc_sso/login?service=http://192.168.108.170:20080/admin_web/#/login")
sleep(4)
driver.find_element_by_id('username').send_keys('scywsh3')
driver.find_element_by_id('password').send_keys('PH2020.com')
driver.find_element_by_id('submi').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/li/div/span').click()#点击审核管理
sleep(4)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/li/ul/a[3]/li/span').click()#点击活动审核
sleep(4)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/input').clear()#清空活动名称
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/input').send_keys(acc_name)#查询活动名称
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/button[1]/span').click()#点击查询
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()#勾选活动
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/button[2]/span').click()#点击同意

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]/span').click()#点击确定
sleep(2)
driver.quit()