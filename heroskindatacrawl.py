import json
from selenium import webdriver

#获取json数据
def read_hero_into_file_json():
    hero_file = open("./hero/hero.json","r",encoding="utf-8")
    hero_result = json.load(hero_file)
    return hero_result


def catch_hero_skin_href_url(url):
    #动态提取
    pjs_path = r"E:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe"   #phantomjs安装目录
    browser = webdriver.PhantomJS(pjs_path)
    browser.maximize_window()
    #发送请求
    browser.get(url)
    #提取数据
    li_list = browser.find_elements_by_xpath("//div[@class='pic-pf']/ul/li")
    #print(len(li_list))
    skin_duixiang = []
    #遍历
    for li_element in li_list:
        skin_zidian = {}
        skin_name = li_element.find_element_by_xpath("./p").text
        #print(skin_name)
        skin_zidian["skin_name"] = skin_name
        skin_url = "https:" + li_element.find_element_by_xpath("./i/img").get_attribute("data-imgname")
        #print(skin_url)
        skin_zidian["skin_url"] = skin_url
        #print(skin_zidian)
        skin_duixiang.append(skin_zidian)
    #关闭
    browser.quit()
    return skin_duixiang

def save_hero_skin_file(datas):
    skin_file = open("./hero/heroskin.json","w",encoding="utf-8")
    json.dump(datas,
              skin_file,
              ensure_ascii=False,
              indent=2)

def main():
    hero_list = read_hero_into_file_json()
    #print(hero_list)
    #英雄列表
    hero_info_list = []
    for hero_element in hero_list:
        hero_item = {}
        hero_name = hero_element["hero_name"]
        hero_item["hero_name"] = hero_name
        #获取链接地址
        skin_href_url = hero_element["hero_href_url"]
        #print(skin_href_url)
        #对链接发送请求
        skin_duixiang = catch_hero_skin_href_url(skin_href_url)
        hero_item["skin_duixiang"] = skin_duixiang
        #print("正在输出%s英雄的皮肤"%hero_name,skin_duixiang)
        #print(hero_item)
        hero_info_list.append(hero_item)
        #print(hero_info_list)
        save_hero_skin_file(hero_info_list)
        print("正在保存英雄%s的皮肤数据信息，请稍候。。。"%hero_name)
    print("您好，所以英雄皮肤数据已经保存成功。")

if __name__ == '__main__':
    main()



