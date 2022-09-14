from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from apps.achievement.models import Academicjournals, Paper, Patent, Achievement
import time

option = webdriver.EdgeOptions()
option.add_argument('headless')
# deiver = webdriver.Edge(options=option)
deiver = webdriver.Edge()
deiver.implicitly_wait(1)
numberlist = range(1, 16)
DBText = ("主题", "篇关摘", "关键词", "篇名", "全文", "作者", "第一作者",
          "通讯作者", "作者单位", "基金", "摘要", "小标题", "参考文献", "分类号",
          "文献来源", "DOI")
DB = zip(DBText, numberlist)
DBDICT = dict(DB)


class Spiders:
    def SearchThing(self, tag, **kwargs):
        author = kwargs.get('作者')
        ankey = kwargs.get('ankey')
        anvalue = kwargs.get('anvalue')
        unit = kwargs.get('unit')
        self.initSearch(self, author, ankey, anvalue, tag,unit)

    def SearchPatent(self, tag, **kwargs):
        author = kwargs.get('发明人')
        anvalue = kwargs.get('anvalue')
        unit = kwargs.get('unit')
        deiver.get('https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS')
        time.sleep(2)
        strs = '// *[contains(text(), "' + tag + '")]//..'
        dbcode = WebDriverWait(deiver, 5).until(
            lambda deiver: deiver.find_element(By.XPATH, strs))
        dbcode.click()
        dl = WebDriverWait(deiver, 5).until(
            lambda deiver: deiver.find_element(By.ID, 'patentgradetxt'))
        sort_list = dl.find_element(By.XPATH, 'dd[2]/div[@class="input-box"]/div/div[@class="sort-list"]')
        deiver.execute_script("arguments[0].style='display: block;'", sort_list)
        AnotherKey = sort_list.find_element(By.XPATH, 'ul/li[12]')
        AnotherKey.click()
        if author != "":
            input_box1 = dl.find_element(By.XPATH, 'dd[2]/div[@class="input-box"]/input')
            input_box1.send_keys(author)
            deiver.execute_script("arguments[0].style='display: none;'", sort_list)
        sort_list = dl.find_element(By.XPATH, 'dd[3]/div[@class="input-box"]/div/div[@class="sort-list"]')
        deiver.execute_script("arguments[0].style='display: block;'", sort_list)
        AnotherKey = sort_list.find_element(By.XPATH, 'ul/li[11]')
        AnotherKey.click()
        if anvalue != "":
            input_box2 = dl.find_element(By.XPATH, 'dd[3]/div[@class="input-box"]/input')
            input_box2.send_keys(anvalue)
            deiver.execute_script("arguments[0].style='display: none;'", sort_list)
        searchBTN = deiver.find_element(By.CLASS_NAME, 'btn-search')
        searchBTN.send_keys(Keys.ENTER)
        time.sleep(2)
        tmp = deiver.find_elements(By.CLASS_NAME, 'fz14')
        if tmp:
            td_list = WebDriverWait(deiver, 5).until(lambda deiver: deiver.find_elements(By.CLASS_NAME, 'fz14'))
            self.Patent(self, td_list,unit)


    def SearchAchievement(self, tag, **kwargs):
        author = kwargs.get('成果完成人')
        anvalue = kwargs.get('anvalue')
        unit= kwargs.get('unit')
        deiver.get('https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS')
        time.sleep(2)
        strs = '// *[contains(text(), "成果")]//..'
        dbcode = WebDriverWait(deiver, 5).until(
            lambda deiver: deiver.find_element(By.XPATH, strs))
        dbcode.click()
        time.sleep(3)
        dl = WebDriverWait(deiver, 5).until(
            lambda deiver: deiver.find_element(By.ID, 'gradetxt'))
        if author != "":
            input_box1 = dl.find_element(By.XPATH, 'dd[2]/div[@class="input-box"]/input')
            input_box1.send_keys(author)
        sort_list = dl.find_element(By.XPATH, 'dd[3]/div[@class="input-box"]/div/div[@class="sort-list"]')
        deiver.execute_script("arguments[0].style='display: block;'", sort_list)
        AnotherKey = sort_list.find_element(By.XPATH, 'ul/li[12]')
        AnotherKey.click()
        deiver.execute_script("arguments[0].style='display: none;'", sort_list)
        if anvalue != "":
            input_box2 = dl.find_element(By.XPATH, 'dd[3]/div[@class="input-box"]/input')
            input_box2.send_keys(anvalue)
        searchBTN = deiver.find_element(By.CLASS_NAME, 'btn-search')
        searchBTN.send_keys(Keys.ENTER)
        time.sleep(2)
        tmp = deiver.find_elements(By.CLASS_NAME, 'fz14')
        if tmp:
            td_list = WebDriverWait(deiver, 5).until(lambda deiver: deiver.find_elements(By.CLASS_NAME, 'fz14'))
            self.Achievement(self, td_list,unit)


    def initSearch(self, author, ankey, anvalue, tag,unit):
        unit = unit
        deiver.get('https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS')
        time.sleep(2)
        dl = WebDriverWait(deiver, 5).until(
            lambda deiver: deiver.find_element(By.ID, 'gradetxt'))
        input_box = dl.find_element(By.XPATH, 'dd[2]/div[@class="input-box"]/input')
        input_box.send_keys(author)
        sort_list = dl.find_element(By.XPATH, 'dd[3]/div[@class="input-box"]/div/div[@class="sort-list"]')
        deiver.execute_script("arguments[0].style='display: block;'", sort_list)
        if ankey != "":
            AnotherKey = sort_list.find_element(By.XPATH, 'ul/li[' + str(DBDICT.get(ankey)) + ']')
            AnotherKey.click()
            input_box = dl.find_element(By.XPATH, 'dd[3]/div[@class="input-box"]/input')
            input_box.send_keys(anvalue)
        searchBTN = deiver.find_element(By.CLASS_NAME, 'btn-search')
        searchBTN.send_keys(Keys.ENTER)
        time.sleep(2)
        strs = '// *[contains(text(), "' + tag + '")]//..'
        dbcode = WebDriverWait(deiver, 5).until(
            lambda deiver: deiver.find_element(By.XPATH, strs))
        dbcode.click()
        time.sleep(2)
        tmp = deiver.find_elements(By.CLASS_NAME, 'fz14')
        if tmp:
            td_list = WebDriverWait(deiver, 5).until(lambda deiver: deiver.find_elements(By.CLASS_NAME, 'fz14'))
            date = deiver.find_elements(By.CLASS_NAME, 'date')
            if tag == "学术期刊":
                self.Journals(self, td_list,unit,date)
            elif tag == "学位论文":
                self.Papers(self, td_list,unit,date)


    def Journals(self, td_list,unit,date):
        unit = unit
        for item,indate in zip(td_list,date):
            title = item.text
            item.click()
            time.sleep(2)
            tdate = indate.text
            deiver.switch_to.window(deiver.window_handles[1])
            authorpart = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.ID, 'authorpart').find_elements(By.XPATH, 'span'))
            part = []
            for tmp in authorpart:
                part.append(tmp.text)
            author = ",".join(part)
            mechanism = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.XPATH, '// *[contains(text(), "学院")]')).text
            abstract = WebDriverWait(deiver, 5).until(lambda deiver: deiver.find_element(By.ID, 'ChDivSummary')).text
            keywords = WebDriverWait(deiver, 5).until(lambda deiver: deiver.find_elements(By.CLASS_NAME, 'keywords'))
            word = []
            for tmp in keywords:
                word.append(tmp.text)
            key_word = "".join(word)
            content = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.ID, 'pdfDown')).get_attribute(
                'href')
            journals = Academicjournals.objects.create(journalsname=title, author=author, mechanism=mechanism,
                                                       abstract=abstract,
                                                       keyword=key_word, content=content,unit=unit,fdate=tdate)
            journals.save()
            deiver.close()
            deiver.switch_to.window(deiver.window_handles[0])

    def Papers(self, td_list,unit,date):
        unit=unit
        for item,indate in zip(td_list,date):
            papername = item.text
            item.click()
            time.sleep(2)
            sdate = indate.text
            deiver.switch_to.window(deiver.window_handles[1])
            author = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.ID, 'authorpart').find_element(By.XPATH, 'span/a')).text
            school = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.XPATH, '// *[contains(text(), "大学")]')).text
            abstract = WebDriverWait(deiver, 5).until(lambda deiver: deiver.find_element(By.ID, 'ChDivSummary')).text
            keywords = WebDriverWait(deiver, 5).until(lambda deiver: deiver.find_elements(By.CLASS_NAME, 'keywords'))
            word = []
            for tmp in keywords:
                word.append(tmp.text)
            key_word = "".join(word)
            tteacher = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.XPATH, '// *[contains(text(), "导师")]//../p')).text
            major = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.XPATH, '// *[contains(text(), "学科专业")]//../p')).text
            content = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.ID, 'cajDown')).get_attribute(
                'href')
            paper = Paper.objects.create(papername=papername, author=author, school=school, abstract=abstract,
                                         keyword=key_word, tteacher=tteacher, major=major, content=content,unit=unit,
                                         fdate=sdate)
            paper.save()
            deiver.close()
            deiver.switch_to.window(deiver.window_handles[0])

    def Patent(self, td_list,unit):
        unit = unit
        for item in td_list:
            patentname = item.text
            item.click()
            time.sleep(2)
            deiver.switch_to.window(deiver.window_handles[1])
            patenttype = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[2]/p')).text
            applicant = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[6]/p')).text
            address = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[7]/p')).text
            inventor = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[8]/p')).text
            album = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[9]/p')).text
            special = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[10]/p')).text
            pages = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[13]/p')).text
            try:
                agency = WebDriverWait(deiver, 5).until(
                    lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH,
                                                                                            'div[14]/div[1]/p')).text
            except:
                agency = "无"
            fdate = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH,
                                                                                        'div[3]/div[2]/p')).text
            abstract = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'abstract-text')).text
            patent = Patent.objects.create(patentname=patentname, patenttype=patenttype,
                                           applicant=applicant, address=address, inventor=inventor,
                                           album=album, special=special, pages=pages, agency=agency,
                                           fdate=fdate, abstract=abstract,unit=unit)
            patent.save()
            deiver.close()
            deiver.switch_to.window(deiver.window_handles[0])

    def Achievement(self, td_list,unit):
        unit = unit
        for item in td_list:
            title = item.text
            item.click()
            time.sleep(2)
            deiver.switch_to.window(deiver.window_handles[1])
            completed = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[2]/p')).text
            first = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[3]/p')).text
            keyword = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[4]/p')).text
            introduction = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[7]/p')).text
            achievementype = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[8]/p')).text
            ydate = WebDriverWait(deiver, 5).until(
                lambda deiver: deiver.find_element(By.CLASS_NAME, 'brief').find_element(By.XPATH, 'div[9]/p')).text

            achievement = Achievement.objects.create(title=title, completed=completed, first=first, keyword=keyword,
                                                     introduction=introduction, achievementype=achievementype,
                                                     ydate=ydate,unit=unit)
            achievement.save()
            deiver.close()
            deiver.switch_to.window(deiver.window_handles[0])
