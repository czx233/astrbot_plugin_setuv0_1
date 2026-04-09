# astrbot_plugin_setuv0_1

一个简单的 AstrBot 涩图插件，使用 waifu.pics API 获取随机动漫图片。

## 功能

- 发送 `/setu` 指令获取随机动漫图片
- 支持多种图片类型（waifu、neko、shinobu 等）

## 使用方法

在聊天中发送：
```
/setu
```

## 安装

1. 将插件放入 AstrBot 的 `data/plugins/` 目录
2. 安装依赖：`pip install aiohttp`
3. 在 AstrBot WebUI 中重载插件

## 依赖

- aiohttp >= 3.8.0

## 相关链接

- [AstrBot 主项目](https://github.com/AstrBotDevs/AstrBot)
- [AstrBot 插件开发文档](https://docs.astrbot.app/dev/star/plugin-new.html)
