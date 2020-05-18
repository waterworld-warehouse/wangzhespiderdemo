import json
import os
import requests
import useragentutil
#
def read_hero_info_file_from_json():
    #从hero.json中获取信息
    jsonreader = open("./hero/hero.json","r",encoding="utf-8")
    hero_json_message = json.load(jsonreader)
    return hero_json_message


def create_hero_image_save_dirs(datas):
    #获取英雄名称后创建目录
    for hero_element in datas:
        #print(hero_element)
        #path_name = hero_element["hero_name"]
        path_name = hero_element.get("hero_name")
        #print("./hero/picture/" + path_name)
        hero_save_path_dir = "./hero/picture/" + path_name
        #print(hero_save_path_dir)
        if not os.path.exists(hero_save_path_dir):
            os.makedirs(hero_save_path_dir)
            print("目录[%s]已创建成功"%hero_save_path_dir)
    print("所有英雄目录创建成功")



def download_hero_image(datas):
    #下载图片
    #获取英雄名称和下载链接
    for hero_message in datas:
        hero_name = hero_message.get("hero_name")
        hero_image_url = hero_message.get("hero_image_url")
        #print("英雄名称:%s,英雄图片:链接%s"%(hero_name,hero_image_url))
        response = requests.get(hero_image_url,headers=useragentutil.get_headers())
        pic_content = response.content
        #保存到文件中
        pic_path = "./hero/picture/" + hero_name
        hero_image_file = open(pic_path+"/1"+hero_name+".jpg","wb")
        #写入数据
        hero_image_file.write(pic_content)
        #关闭数据
        hero_image_file.close()
        print("正在下载%s英雄的图片"%hero_name)
    print("所有英雄图片下载完毕！")


def main():
    #读取文件数据
    hero_info_list = read_hero_info_file_from_json()
    #print(hero_info_list)
    create_hero_image_save_dirs(hero_info_list)
    download_hero_image(hero_info_list)

if __name__ == '__main__':
    main()