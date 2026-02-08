# AudioClient

基于 PySide6 的语音客户端，用于连接语音服务器进行实时通话，支持**管制员（ATC）**与**飞行员（Pilot）**两种角色，可与飞行模拟器（FSUIPC）及
ADF 等插件配合使用。

## 功能概览

- **双角色**：管制员多频率收发、飞行员 COM1/COM2 收发
- **语音**：Opus 编解码，麦克风采集与双路输出（耳机 / 扬声器可分别配置），支持按通道选择输出设备
- **PTT**：可配置按键与提示音（按下/松开频率与音量），冲突音检测与音量调节
- **网络**：TCP 信令 + UDP 语音，与语音服务器对接
- **WebSocket**：管制员模式下对外提供 WebSocket 服务，供 ADF 等插件获取状态（连接、频率、PTT 等）
- **FSUIPC**（可选）：读取/同步模拟器 COM 频率与接收标志
- **配置**：YAML 配置、日志级别、音频设备与快捷键等

## 技术栈

| 类别     | 技术                           |
|--------|------------------------------|
| 界面     | PySide6 (Qt6)                |
| 语音编解码  | Opus (opuslib)               |
| 音频 I/O | PyAudio、soxr 重采样             |
| 网络     | 标准 TCP/UDP socket、websockets |
| 配置     | Pydantic、PyYAML              |
| 包管理    | PDM，Python 3.12              |

## 项目结构（简要）

```
AudioClient/
├── main.py              # 入口
├── generate_file.py     # 生成 UI 与资源（运行前需执行）
├── lib/                 # opus.dll、libfsuipc.dll
├── src/
│   ├── core/            # 语音客户端、网络、音频流、FSUIPC、WebSocket 服务
│   ├── ui/              # 登录、连接、管制窗、飞行员窗、配置等
│   ├── config/          # 配置加载与保存
│   ├── model/           # 数据模型与协议
│   ├── signal/          # 全局信号
│   └── utils/           # 日志、HTTP、样式等
├── style/               # QSS 样式
├── docs/                # 文档与打包脚本
└── pyproject.toml
```

## 环境与安装

### 1. 安装 PDM

推荐使用 [pipx](https://pypa.github.io/pipx/) 安装 [PDM](https://pdm-project.org/zh-cn/latest/)：

```bash
pipx install pdm
pdm --version   # 应输出类似 PDM, version x.xx.x
```

### 2. 安装依赖

在项目根目录执行：

```bash
pdm install -G dev
```

### 3. 修改 opuslib（若系统未安装 opus）

opuslib 默认会查找系统是否已安装 opus 动态库。若你本机已安装并可被找到，可跳过本步。

若未安装或希望使用项目自带的 `lib/opus.dll`，请用下面内容**覆写**  
**`.venv/Lib/site-packages/opuslib/api/__init__.py`**（Windows 下路径可能为 `Lib` 或 `lib`，以实际为准）：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""OpusLib Package."""

import ctypes  # type: ignore
from pathlib import Path
from sys import platform

from ctypes.util import find_library  # type: ignore

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'

lib_location = find_library('opus')
root = Path.cwd() / "lib"

if lib_location is None:
    if platform == 'win32':
        lib_location = root / "opus.dll"
    elif platform == 'darwin':
        lib_location = root / "libopus.dylib"
    elif platform == 'linux':
        lib_location = root / "libopus.so"
    else:
        raise OSError("unsupported platform")
    if not lib_location.exists():
        raise FileNotFoundError("libopus not found")

libopus = ctypes.CDLL(str(lib_location))

c_int_pointer = ctypes.POINTER(ctypes.c_int)
c_int16_pointer = ctypes.POINTER(ctypes.c_int16)
c_float_pointer = ctypes.POINTER(ctypes.c_float)
```

覆写后，opuslib 会优先使用项目根目录下 `lib/` 中的 opus 库（Windows: `opus.dll`，macOS: `libopus.dylib`，Linux: `libopus.so`）。

### 4. 生成 UI 与资源

修改过 `.ui`、`.qrc` 后需重新生成：

```bash
pdm run python generate_file.py
```

### 5. 运行

```bash
pdm run python main.py
```

或先激活虚拟环境再运行：

```bash
# Windows CMD
.\.venv\Scripts\activate.bat
# Windows PowerShell
.\.venv\Scripts\activate

python generate_file.py   # 若改过 UI/资源
python main.py
```

## 配置说明

首次运行后会在项目目录下生成配置文件（路径见 `src/constants.py` 中的 `config_file`），YAML 格式。主要可配置项：

- **server**：`voice_endpoint`、`voice_tcp_port`、`voice_udp_port`、`api_endpoint`
- **account**：登录账号与密码
- **audio**：音频驱动、输入/输出设备（含耳机与扬声器）、麦克风增益、PTT 按键与提示音、冲突音音量
- **log**：`level`（TRACE/DEBUG/INFO/WARNING/ERROR）、路径、轮转等

日志等级说明见 [docs/日志等级对照表.md](docs/日志等级对照表.md)。

## 文档

| 文档                                         | 说明                    |
|--------------------------------------------|-----------------------|
| [docs/VoiceClient.md](docs/VoiceClient.md) | VoiceClient 工作原理与使用方法 |
| [docs/日志等级对照表.md](docs/日志等级对照表.md)         | 各等级日志含义与示例            |
| docs/ExePacking.iss、build.bat              | 打包为安装程序的脚本与说明         |

## 打包与开发

- 使用 Nuitka 等打包可参考 `pyproject.toml` 中 `dev` 依赖及项目脚本。
- 推荐安装 [Mypy](https://mypy-lang.org/) 或 IDE 的 mypy 插件做类型检查。

## 开源协议

MIT License  
Copyright © 2025-2026 Half_nothing

无附加条款。

## 贡献者

<a href="https://github.com/FSD-Universe/AudioClient/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=FSD-Universe/AudioClient" alt="贡献者"/>
</a>
