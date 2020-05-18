import json
import requests
import useragentutil
#禁用 urllib3
import urllib3
urllib3.disable_warnings()
def read_hero_skin_file_from_json():
    skin_file = open("./hero/heroskin.json","r",encoding="utf-8")
    skin_result = json.load(skin_file)
    return skin_result


def main():
    #1.从已经获取到的皮肤信息数据中，读取文件，获得数据
    hero_skin_datas = read_hero_skin_file_from_json()
    #2.遍历并获取单个的英雄数据
    i = 0
    while i < len(hero_skin_datas):
        hero = hero_skin_datas[i]
        #print("第%d个英雄，数据信息："%i,hero)
        #3.遍历单个英雄数据，获得单个皮肤名称、网站
        hero_name = hero.get("hero_name")
        #print("英雄名称：",hero_name)
        pic_path_name = "./hero/picture/" + hero_name
        #print(pic_path_name)
        skin_list = hero.get("skin_duixiang")
        #print("皮肤信息：",skin_list)

        #4.下载皮肤图片
        for skin_element in skin_list:
            #print("皮肤数据：",skin_element)
            skin_name = skin_element["skin_name"]
            skin_image_url = skin_element["skin_url"]
            headers_url = useragentutil.get_headers()
            response = requests.get(skin_image_url,verify=False,headers=headers_url)
            skin_image_content = response.content
            image_name = pic_path_name + "/" +  skin_name + ".jpg"
            file = open(image_name,"wb")
            file.write(skin_image_content)
            print("正在下载英雄(%s)的皮肤图片，皮肤名称：%s"%(hero_name,skin_name))
        i += 1
    pass


if __name__ == '__main__':
    main()