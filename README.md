
<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="300" alt="logo"></a>
</div>

<div align="center">

## ✨ *基于 Nonebot2 的 FinalShell 激活码生成插件* ✨

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/YourGitHubName/nonebot-plugin-fuckfinalshell.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-fuckfinalshell">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-fuckfinalshell.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<img src="https://img.shields.io/badge/adapter-universal-blueviolet" alt="adapter">
<a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
</a>
</div>

</div>

## 📖 介绍

一个简单的 NoneBot2 插件，用于生成 FinalShell 的激活码。本插件基于公开的算法实现，可以根据用户提供的机器码，计算并返回适用于多个 FinalShell 版本的激活码。

本插件为纯文本交互，理论上支持所有适配器。

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 NoneBot2 项目的根目录下打开命令行，输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-fuckfinalshell
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 NoneBot2 项目的插件目录下（或项目根目录），打开命令行，根据你使用的包管理器，输入相应的安装命令：

<details open>
<summary>uv</summary>

```bash
uv add nonebot-plugin-fuckfinalshell
```
安装仓库 main 分支：

```bash
uv add git+https://github.com/006lp/nonebot-plugin-fuckfinalshell@main
```
</details>

<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-fuckfinalshell
```
安装仓库 main 分支：

```bash
pdm add git+https://github.com/006lp/nonebot-plugin-fuckfinalshell@main
```
</details>

<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-fuckfinalshell
```
安装仓库 main 分支：

```bash
poetry add git+https://github.com/006lp/nonebot-plugin-fuckfinalshell@main
```
</details>

<br/>

然后，**手动或使用 `nb` 命令**将插件加载到你的 NoneBot2 项目中。
如果使用 `pyproject.toml` 管理插件，请确保在 `[tool.nonebot]` 部分添加了插件名：

```toml
[tool.nonebot]
# ... 其他配置 ...
plugins = ["nonebot_plugin_fuckfinalshell"]
# ... 其他插件 ...
```

</details>

## ⚙️ 配置

本插件无需任何额外配置即可使用。

## 🎉 使用

### 指令表

| 指令              |      别名       |  权限  | 需要@ |   范围    | 说明                               |
| :---------------- | :-------------: | :----: | :---: | :-------: | :--------------------------------- |
| `/fskey <机器码>` | `finalshellkey` | 任何人 |  否   | 群聊/私聊 | 根据机器码生成 FinalShell 激活码。 |

### 说明

*   **`<机器码>`**: 你的 FinalShell 软件中显示的机器码。
*   **无参数**: 如果直接发送 `/fskey`，机器人会返回使用帮助。

### 🎨 返回示例

*查询成功示例:*
```
为机器码 1a2b3c4d5e 生成的激活码如下：

FinalShell < 3.9.6
🟡 高级版: a1b2c3d4e5f6a1b2
🟢 专业版: b2c3d4e5f6a1b2c3

FinalShell ≥ 3.9.6
🟡 高级版: c3d4e5f6a1b2c3d4
🟢 专业版: d4e5f6a1b2c3d4e5

FinalShell 4.5
🟡 高级版: e5f6a1b2c3d4e5f6
🟢 专业版: f6a1b2c3d4e5f6a1

FinalShell 4.6
🟡 高级版: a1b2c3d4e5f6a1b2
🟢 专业版: b2c3d4e5f6a1b2c3
```

*无参数或格式错误示例:*
```
使用方法：
/fskey <你的机器码>
例如：
/fskey ABCDEFG
```

## ⚠️ 使用警告

*   **仅供学习与技术交流！** 本项目旨在研究其加密算法，请勿用于商业和非法用途。
*   **请支持正版！** 如果您喜欢 FinalShell，请考虑购买正版授权以支持开发者的持续创作。
*   用户应对自己的使用行为负责，开发者不承担任何因使用此插件造成的直接或间接责任。

## 📃 许可证

本项目采用 [AGPL v3](./LICENSE) 许可证。

## 🙏 致谢

*   **NoneBot2**: 插件开发框架。
*   **PyCryptodome**: 提供加密算法库。
*   **互联网上公开算法的研究者**: 为本项目提供了算法基础。