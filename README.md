<!--
 * @Author: robert zhang <robertzhangwenjie@gmail.com>
 * @Date: 2022-11-12 12:05:59
 * @LastEditTime: 2023-02-27 22:05:44
 * @LastEditors: robert zhang
 * @Description: 
-->
# Gitbook2Pdf 
一键抓取由 GitBook 框架生成的网站

## Usage 
### With Docker
```shell
docker run -it -v `pwd`/output:/app/output zhangwenjie/gitbook2pdf <your url> <filename.pdf>
```

### With python
```shell
pip install -r requirements.txt
python gitbook.py <url> <filename.pdf>
```

## Original Project
[original project url](https://github.com/fuergaosi233/gitbook2pdf)
