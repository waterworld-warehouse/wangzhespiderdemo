from matplotlib import pyplot
import json


#读取文件
def read_heroskin_data_file():
    skin_file = open("./hero/data.json","r",encoding="utf-8")
    skin_result = json.load(skin_file)
    #print(skin_result)
    hero_x = skin_result["hero_x"]
    skin_length_y = skin_result["skin_length_y"]
    # print(hero_x)
    # print(skin_length_y)
    return hero_x,skin_length_y

def main():
    x_list,y_list = read_heroskin_data_file()
    # print(x_list)
    # print(y_list)

    pyplot.figure(figsize=(24,8),dpi=100)   #绘制画布
    pyplot.rcParams["font.sans-serif"] = ["SimHei"]     #解决乱码问题
    pyplot.grid(alpha=0.6)      #添加网格
    pyplot.title("王者荣耀英雄皮肤数量分析图")   #设置标题
    pyplot.xlabel("英雄名称")          #x轴标题
    pyplot.ylabel("皮肤数量(单位：个)")     #y轴标题
    x = [i for i in range(1,len(x_list)+1)]     #设置x轴
    pyplot.bar(x,y_list)    #条形图
    pyplot.xlim(0,len(x_list)+1)    #设置最大最小值
    pyplot.xticks(x,x_list,rotation=270)     #绘制刻度
    pyplot.show()



if __name__ == '__main__':
    main()