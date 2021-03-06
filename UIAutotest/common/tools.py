#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'laiyu'

import  re
import os


class Tools():
    # def my_strip(self,str1,s_char):
    #     if str1[0:1]==s_char:
    #         str1 = str1[1:]
    #     #print str1
    #     if str1[-1:]==s_char:
    #         str1 = str1[:-1]
    #     return str1

    # # 转换php页面存储的数据
    # def conver_data_from_phppage(self, data):
    #     data =  data.replace('&rsquo;', '"')   # 转换中文单引号 ’为英文的 "
    #     data =  data.replace('&lsquo;', '"')   # 转换中文单引号‘ 为英文的 "
    #     data =  data.replace('&ldquo;', '"')   # 转换中文双引号“ 为英文的 "
    #     data =  data.replace('&rdquo;', '"')   # 转换中文双引号 ” 为英文的 "
    #     data =  data.replace('：', ":")         # 转换中文的冒号 ：为英文的冒号 :
    #     data =  data.replace('，', ',')         # 转换中文的逗号 ，为英文的逗号 ,
    #     data =  data.replace('&quot;', '\"')   # 转换 &quot; 为双引号
    #     data =  data.replace('&#39;', '\'')    # 转换 &#39;  为单引号
    #     data = data.replace('&gt;', '>')
    #
    #     return data

    # 批量创建目录
    def mkdirs_once_many(self, path):
        path = os.path.normpath(path)  # 去掉路径最右侧的 \\ 、/
        path = path.replace('\\', '/') # 将所有的\\转为/，避免出现转义字符串

        head, tail = os.path.split(path)
        new_dir_path = ''  # 反转后的目录路径
        root = ''  #根目录

        if not os.path.isdir(path) and os.path.isfile(path):  # 如果path指向的是文件，则继续分解文件所在目录
            head, tail = os.path.split(head)

        if tail == '':
            return

        while tail:
            new_dir_path = new_dir_path + tail + '/'
            head, tail = os.path.split(head)
            root = head
        else:
            new_dir_path = root + new_dir_path

            # 批量创建目录
            new_dir_path = os.path.normpath(new_dir_path)
            head, tail = os.path.split(new_dir_path)
            temp = ''
            while tail:
                temp = temp + '/' + tail
                dir_path = root + temp
                if not os.path.isdir(dir_path):
                    os.mkdir(dir_path)
                head, tail = os.path.split(head)

    # # 递归获取指定目录下的特征文件
    # def get_filepath_with_specific_feature(self, dirpath, files, feature):
    #     temp_file_list = []
    #     for file in files:
    #         path = os.path.join(dirpath, file)
    #         path = os.path.normcase(path)
    #         if re.search(str(feature), path):
    #             temp_file_list.append(path)
    #     return temp_file_list
    #

