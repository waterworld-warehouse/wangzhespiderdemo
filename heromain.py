import herodatacrawl
import herodatadown
import heroskindatacrawl
import heroskindown
def main():
    #爬取英雄数据
    herodatacrawl.main()
    #下载英雄头像
    herodatadown.main()
    #爬取英雄皮肤数据
    heroskindatacrawl.main()
    #下载英雄皮肤
    heroskindown.main()


if __name__ == '__main__':
    main()