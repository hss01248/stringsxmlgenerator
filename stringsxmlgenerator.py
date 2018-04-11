# Android国际化： 将excel中的内容转化到xml中
# 使用说明:
# 1.将你要改的那些文案拷出来到一个空白的excel表中;
# 遵循格式: 第一列中文,第二列英文,第三列印尼,第四列马来,第五列越南
# 2.文件名命名为你的模块名,同时将下方modelname = "native_pay"的值改成你的模块名
# 3. 将excel文件拷贝到与python文件同一个目录,点击运行python脚本,将生成文件:strings-en.xml,strings-in.xml,strings-ms.xml,strings-vn.xml
# 4. 将内容拷贝到项目对应的strings.xml下
# 5.检查: 如果原文案中有xx,xxx,xxxx等,会自动替换成%$s,需要自己手动加上序号,如%1$s

from xml.dom import minidom
from xlrd import open_workbook
import codecs

modelname = "native_pay"


# 添加字符串
def getkeybyen(en):
    str0 = str.replace(en, ' ', '_')
    str0 = str.replace(str0, ',', '_')
    str0 = str.replace(str0, '!', '_')
    str0 = str.replace(str0, '?', '_')
    str0 = str.replace(str0, '.', '_')
    str0 = str.replace(str0, '/', '_')
    str0 = str.replace(str0, ':', '')
    str0 = str.lower(str0)
    print(str0)
    if len(str0) > 20:
        str0 = str0[0: 19]
    return modelname + '_' + str0


def addelement(docen, resourcesen, key, value):
    text_element = docen.createElement('string')
    text_element.setAttribute('name', key)
    text_element.appendChild(docen.createTextNode(value))
    resourcesen.appendChild(text_element)


def savedoc(filename, doc):
    f = codecs.open(filename, 'w', encoding='utf-8')
    # doc.writexml(f)
    f.write(doc.toprettyxml(indent='    '))
    f.close()


# 打开excel
workbook = open_workbook(modelname + '.xlsx')

# 新建xml
docen = minidom.Document()
# 添加根元素
resourcesen = docen.createElement('resources')
docen.appendChild(resourcesen)

# 印尼
# 新建xml
docin = minidom.Document()
# 添加根元素
resourcesin = docin.createElement('resources')
docin.appendChild(resourcesin)

# 马来
# 新建xml
docms = minidom.Document()
# 添加根元素
resourcesms = docms.createElement('resources')
docms.appendChild(resourcesms)

# 马来
# 新建xml
docvn = minidom.Document()
# 添加根元素
resourcesvn = docvn.createElement('resources')
docvn.appendChild(resourcesvn)


def replacenext(en, idx0):
    idx = en.find('%$s')
    if idx > 0:
        idx1 = idx0 + 1
        restr = '%' + str(idx1) + '$s'
        en2 = str.replace(en, "%$s", restr, 1)
        print(en2)
        replacenext(en2, idx1)
    else:
        return en


def repalcexxxforplaceholder(en):
    en = str.replace(en, "xxxxx", "%$s")
    en = str.replace(en, "xxxx", "%$s")
    en = str.replace(en, "xxx", "%$s")
    en = str.replace(en, "xx", "%$s")

    en = str.replace(en, "XXXXX", "%$s")
    en = str.replace(en, "XXXX", "%$s")
    en = str.replace(en, "XXX", "%$s")
    en = str.replace(en, "XX", "%$s")

    # 给%$s加上序号:有bug

    # en1 = replacenext(en,0)
    return str(en)


for sheet in workbook.sheets():
    for row_index in range(sheet.nrows):
        en = sheet.cell(row_index, 1).value
        if len(en) == 0:
            continue
        key = getkeybyen(en)

        ind = sheet.cell(row_index, 2).value
        ms = sheet.cell(row_index, 3).value
        vn = sheet.cell(row_index, 4).value
        # 过滤xx,xxx,将之替换成占位符%1$s,%2$s的形式
        en = repalcexxxforplaceholder(en)
        ind = repalcexxxforplaceholder(ind)
        ms = repalcexxxforplaceholder(ms)
        vn = repalcexxxforplaceholder(vn)

        # 新建一个文本元素
        addelement(docen, resourcesen, key, en)
        addelement(docin, resourcesin, key, ind)
        addelement(docms, resourcesms, key, ms)
        addelement(docvn, resourcesvn, key, vn)

savedoc("strings-en.xml", docen)
savedoc("strings-in.xml", docin)
savedoc("strings-ms.xml", docms)
savedoc("strings-vn.xml", docvn)
