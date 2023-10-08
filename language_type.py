from strenum import StrEnum

# 支持的多语言  value必须为excel表的第一行对应语言描述冒号后面的部分
class LanguageType(StrEnum):
    # 简体中文 
    zh_hans = 'zh_hans'
    # 繁体中文
    zh_hant = 'zh_hant'
    # 英语
    en = 'en'
    # 西班牙语
    es = 'es'
    # 日语
    ja = 'ja'
    # 韩语
    ko = 'ko'

# 平台类型
class PlatformType(StrEnum):
    # ios
    ios = 'ios'
    # android
    android = 'android'
    # web
    web = 'web'
    