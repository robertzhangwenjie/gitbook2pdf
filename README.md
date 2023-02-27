<!--
 * @Author: robert zhang <robertzhangwenjie@gmail.com>
 * @Date: 2022-11-12 12:05:59
 * @LastEditTime: 2023-02-27 22:05:44
 * @LastEditors: robert zhang
 * @Description: 
-->
# Gitbook2Pdf 
## This project has solved the image display problem   
- 原因分析  
  当页面图片的地址为相对地址时，因为拼接的baseUrl为传入的url，因此当gitbook存在多个子章节时，子章节中的img url拼接错误  
- 解决方案  
  再爬取每个章节的内容后，将内容中的所有img标签中的属性scr进行替换，使用urllib.parse.urljoin替换为当前章节的所有img属性src的值


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