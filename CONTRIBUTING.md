# 贡献指南

Contribution Guidelines


## 安装并配置pdm

1. 安装(Windows)
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"
  ```

2. 查看系统环境变量
  进入电脑环境变量配置，查看环境变量是否被自动配置正确.。如，配置正确应该如下：
  ```
  C:\Users\<用户名>\AppData\Roaming\Python\Scripts
  ```

3. 进入项目根目录，创建虚拟环境，输入：
  ```powershell
  python -m venv ./.venv
  ```

4. 进入虚拟环境：
   ```cmd
   ; cmd
   .\.venv\Scripts\activate.bat
   ```
   ```powershell
   ; powershell
   .\.venv\Scripts\activate
   ```

5. 使用pdm安装库
  ```powershell
  pdm install
  ```
  应显示以下信息：
  ```
  0:XX:XX 🎉 All complete! 36/36
  ```

6. 进入`.venv/lib/site-packages/opuslib/api/__init__.py`，使用以下内容覆写：
  ```
   #!/usr/bin/env python
   # -*- coding: utf-8 -*-
   # pylint: disable=invalid-name
   #
   
   """OpusLib Package."""
   
   import ctypes  # type: ignore
   
   from sys import platform
   from os import getcwd
   from os.path import join
   from ctypes.util import find_library  # type: ignore
   from pathlib import Path
   
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
           raise OSError("unupported platform")
   
       if not lib_location.exists():
           raise FileNotFoundError("libopus not found")
   
   libopus = ctypes.CDLL(lib_location)
   
   c_int_pointer = ctypes.POINTER(ctypes.c_int)
   c_int16_pointer = ctypes.POINTER(ctypes.c_int16)
   c_float_pointer = ctypes.POINTER(ctypes.c_float)
  ```

> [!NOTE]
>
> 这里的更改不会被同步至云端仓库，由于此文件被ignore了。

7. 自行配置Pycharm

8. Enjoy Your Coding!!!