- 模块【base/apiutil.py】
    - 函数【specification_yaml】
      - 源码：
      cookie = eval(self.replace_load(base_info['cookies']))
      validation = eval(test_case.pop('validation'))
      - 问题
      断言用eval可以理解，为什么cookie需要用eval？
      是不是不支持多文件上传？
    