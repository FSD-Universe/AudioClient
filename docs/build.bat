@echo off

set NUITKA_CACHE_DIR_CCACHE=D:\WorkSpace\python\AudioClient\build\cache\gcc
set NUITKA_CACHE_DIR_CLCACHE=D:\WorkSpace\python\AudioClient\build\cache\msvc
set NUITKA_CACHE_DIR_DOWNLOADS=D:\WorkSpace\python\AudioClient\build\cache\download
set NUITKA_CACHE_DIR_BYTECODE=D:\WorkSpace\python\AudioClient\build\cache\byte
set NUITKA_CACHE_DIR_DLL_DEPENDENCIES=D:\WorkSpace\python\AudioClient\build\cache\dll

python -m nuitka --standalone --mingw64 --lto=yes --show-modules --include-raw-dir=./lib=./lib --enable-plugin=pyside6 ^
--enable-plugin=upx --onefile-no-compression --include-qt-plugins=platforms,styles --remove-output ^
--follow-imports --nofollow-import-to=PySide6.QtWebEngine --nofollow-import-to=PySide6.Qt3D ^
--nofollow-import-to=PySide6.QtBluetooth --nofollow-import-to=PySide6.QtSql --nofollow-import-to=mypy ^
--nofollow-import-to=nuitka --nofollow-import-to=types-pyyaml --nofollow-import-to=types-pyaudio ^
--include-package=websockets --include-module=src --output-dir=dist --output-filename=AudioClient ^
--windows-console-mode=disable --windows-icon-from-ico=./icon/logo.ico main.py
