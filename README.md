<!--
 * @Author: robert zhang <robertzhangwenjie@gmail.com>
 * @Date: 2022-11-12 12:05:59
 * @LastEditTime: 2022-11-13 10:57:58
 * @LastEditors: robert zhang
 * @Description: 
-->
# Gitbook2Pdf 
## The project had solved the image display problem

## Usage 
### With Docker
```shell
docker run -it -v `pwd`/output:/app/output zhangwenjie/gitbook2pdf <your url>
```

### With python
```shell
pip install -r requirements.txt
python gitbook.py <url>
```

## Original Project
![gitbook2pdf](https://github.com/fuergaosi233/gitbook2pdf)#