#### 一. 自动将excel翻译文件导出iOS 安卓 web国际化源文件的翻译工具

#### 二. 自动将iOS 安卓 web国际化源文件导出excel翻译文件

##### 使用方法:

- 安装python3
- 安装python的包管理工具 pip
- 安装依赖excel解析库: openpyxl

```
pip install openpyxl
```

- 安装依赖枚举库：StrEnum

```
pip install StrEnum
```

一. 自动将excel翻译文件导出iOS 安卓 web国际化源文件的翻译工具

- 将iOS， android，web各端的excel翻译文件拖入./language_trans/trans_from_excel/input下对应的文件夹中
- 打开终端，cd到 language_trans 目录，执行 trans_from_excel.py

```
python3 trans_from_excel.py
```

- output文件夹下输出各端对应的翻译源文件

二. 自动将iOS 安卓 web国际化源文件导出excel翻译文件

- 将iOS， android，web各端的l翻译源文件(eg: zh-Hans.lproj/Localizable.strings)))拖入./language_trans/trans_to_excel/input下对应的文件夹中
- 打开终端，cd到 language_trans 目录，执行 trans_to_excel.py

  ```
  python3 trans_to_excel.py
  ```
- output文件夹下输出各端对应的excel翻译文件
