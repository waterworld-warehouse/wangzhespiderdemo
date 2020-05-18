from selenium import webdriver
import lxml.html
import os
import json
import time
#禁用 urllib3
import urllib3
urllib3.disable_warnings()
def parse_wangzhe_url(http_url):
    #phantomjs安装目录
    pjs_path = r"E:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    browser = webdriver.PhantomJS(pjs_path)
    browser.get(http_url)
    time.sleep(2)
    hero_html_content = browser.page_source
    #print(hero_html_content)
    browser.quit()
    return hero_html_content


def catch_hero_into_list(html_content):
    #提取英雄数据信息
    metree = lxml.html.etree
    #获取etree对象
    parse = metree.HTML(html_content)
    #获取解析器对象
    li_list = parse.xpath("//div[@class='herolist-content']/ul[@class='herolist clearfix']/li")
    #开始解析
    # print(li_list)
    # print(len(li_list))
    hero_info_list = []
    for li_element in li_list:
        hero_item = {}
        #英雄名称
        hero_name = li_element.xpath("./a/text()")[0]
        #print(hero_name)
        hero_item["hero_name"] = hero_name
        #英雄图片地址
        hero_image_url = "https:" + li_element.xpath("./a/img/@src")[0]
        #print(hero_image_url)
        hero_item["hero_image_url"] = hero_image_url
        #详情链接地址
        hero_href_url = "https://pvp.qq.com/web201605/" + li_element.xpath("./a/@href")[0]
        #print(hero_href_url)
        hero_item["hero_href_url"] = hero_href_url
        #print(hero_item)
        hero_info_list.append(hero_item)
    #返回
    return hero_info_list


def save_hero_file(datas):
    #把所有英雄数据保存到文件中
    #先创建一个目录
    hero_path = "./hero"
    if not os.path.exists(hero_path):
        os.makedirs(hero_path)
        print("目录(%s)创建成功！"%hero_path)
    #保存数据
    wangzhefile = open(hero_path + "/hero.json", "w", encoding="utf-8")
    json.dump(datas,wangzhefile,ensure_ascii=False,indent=2)
    print("数据文件保存成功！")


def main():
    #王者荣耀英雄资料网页
    wangzhe_url = "https://pvp.qq.com/web201605/herolist.shtml"
    hero_html_datas = parse_wangzhe_url(wangzhe_url)
    #print(hero_html_datas)
    #print(html_date)
    hero_info_list = catch_hero_into_list(hero_html_datas)
    # #print(hero_info_list)
    # #将python数据存入到json文件中
    save_hero_file(hero_info_list)



if __name__ == '__main__':
    main()