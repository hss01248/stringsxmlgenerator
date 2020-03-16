# stringsxmlgenerator
多国语言文案一键生成strings.xml

Android国际化： 将excel中的内容转化到xml中

# 使用说明:
* 1.将你要改的那些文案拷出来到一个空白的excel表中;

遵循格式: 第一列中文,第2列key(将第三列英文拷过来,略做修改),第3列英文,第4列印尼,第5列马来,第6列越南

* 2.文件名命名为你的模块名,同时将下方modelname = "native_pay"的值改成你的模块名
* 3. 将excel文件拷贝到与python文件同一个目录,点击运行python脚本,将生成文件:modelname-en.xml,modelname-in.xml,modelname-ms.xml,modelname-vn.xml
* 4. 将内容拷贝到项目对应的strings.xml下
*  5.检查: 如果原文案中有xx,xxx,xxxx等,会自动替换成%ss,需要自己手动加上序号,如%1$s