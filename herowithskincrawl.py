import json
def read_hero_skin_file():
    skin_file = open("./hero/heroskin.json","r",encoding="utf-8")
    skin_result = json.load(skin_file)
    return skin_result


def main():
    #读取文件
    hero_skin_datas = read_hero_skin_file()
    #print(hero_skin_datas)
    #字典
    hero_item = {}
    #列表
    hero_list = []
    skin_length_list = []
    #处理
    for hero_element in hero_skin_datas:
        #名称
        hero_name = hero_element["hero_name"]
        #个数
        skin_length = len(hero_element["skin_duixiang"])
        #print("英雄：%s,皮肤个数：%d"%(hero_name,skin_length))
        hero_list.append(hero_name)
        skin_length_list.append(skin_length)
    hero_item["hero_x"] = hero_list
    hero_item["skin_length_y"]=skin_length_list
    #保存
    json.dump(hero_item,
              open("./hero/data.json","w",encoding="utf-8"),
              ensure_ascii=False)
    print("所有英雄数据已处理并保存成功！")



if __name__ == '__main__':
    main()