import json
import re
import shutil
from os import replace

from commons.recordlog import logs
from conftest import conf

class allureUtil:
    def __init__(self):
        self.title = conf.get_section_ALLURE_REPORT_CUSTOM("title")
        self.LogoFile = conf.get_section_ALLURE_REPORT_CUSTOM("LogoFile")
        self.reportFilePath = conf.get_section_ALLURE_REPORT_CUSTOM("reportFilePath")
        self.logoText = conf.get_section_ALLURE_REPORT_CUSTOM("logoText")
        self.reportContentTitle = conf.get_section_ALLURE_REPORT_CUSTOM("reportContentTitle")

    def doAllureCustom(self):
        self.replaceWebSiteTitle()
        self.replaceReportContentPageTitle()
        self.replaceFavicon()
        self.replaceLogosvg()
        self.replacelogoText()

    def replacelogoText(self):
        #图标右侧的展示文案
        # 获取CSS文件的路径
        Css_filepath = self.reportFilePath + r"/plugins/custom-logo/styles.css"
        try:
            file = open(Css_filepath, 'r', encoding="utf-8")
            content = file.read()

            oldText = re.search('content: "(.*?)";', content)
            if oldText is None:
                file.close()
                with open(Css_filepath, 'a',encoding="UTF-8") as file:
                    file.write('\n')
                    file.write(".side-nav__brand span{\n")
                    file.write("  display: none;\n")
                    file.write("}\n")
                    file.write(".side-nav__brand:after{\n")
                    file.write("  content: \"" + self.logoText + "\";\n")
                    file.write("  margin-left: 20px;\n")
                    file.write("}\n")
                file.close()
            else:
                oldText = oldText.group(1)
                content = content.replace(f"content: \"" + oldText, f"content: \"" + self.logoText)
                file.close()

                file = open(Css_filepath, 'w', encoding="utf-8")
                file.write(content)
        except Exception as e:
            logs.error(f'获取【{Css_filepath}】文件数据时出现未知错误: {str(e)}')
        finally:
            file.close()

    def replaceFavicon(self):
        # 定义源文件和目标目录
        target_Favicon_filepath = self.reportFilePath + r"/"
        source_Favicon_filepath = "./imgs/favicon.ico"
        # 使用shutil.copy2()函数复制文件到目标目录并覆盖已存在的文件
        shutil.copy2(source_Favicon_filepath, target_Favicon_filepath)

    def replaceLogosvg(self):
        # 定义源文件和目标目录
        target_Logosvg_filepath = self.reportFilePath + r"/plugins/custom-logo/"
        source_Logosvg_filepath = r"./imgs/custom-logo.svg"
        # 使用shutil.copy2()函数复制文件到目标目录并覆盖已存在的文件
        shutil.copy2(source_Logosvg_filepath, target_Logosvg_filepath)

    def replaceReportContentPageTitle(self):
        # 获取文件的路径
        report_filepath = self.reportFilePath + r"/widgets/summary.json"
        try:
            file = open(report_filepath, 'r', encoding="utf-8")
            content = file.read()
            contentJson = json.loads(content)
            contentJson["reportName"] = self.reportContentTitle
            file.close()

            content = json.dumps(contentJson, ensure_ascii=False)
            file = open(report_filepath, 'w', encoding="utf-8")
            file.write(content)
        except Exception as e:
            logs.error(f'获取【{report_filepath}】文件数据时出现未知错误: {str(e)}')
        finally:
            file.close()

    def replaceWebSiteTitle(self):
        #获取HTML测试报告的路径
        report_filepath = self.reportFilePath + r"/index.html"
        try:
            file = open(report_filepath,'r',encoding="utf-8")
            content = file.read()
            #替换web页面的标题
            oldTitle = re.search("<title>(.*?)</title>", content)
            oldTitle = oldTitle.group(1)
            content = content.replace(f"<title>" + oldTitle,f"<title>" + self.title)
            file.close()

            file = open(report_filepath, 'w', encoding="utf-8")
            file.write(content)
        except Exception as e:
            logs.error(f'获取【{report_filepath}】文件数据时出现未知错误: {str(e)}')
        finally:
            file.close()
