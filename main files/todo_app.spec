# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['todo_app.py'],
    pathex=[],
    binaries=[],
    datas=[('tasks.json', '.'), ('settings.json', '.'), ('back29.png', '.'), ('button_back.png', '.'), ('button_back1.png', '.'), ('button_back2.png', '.'), ('button_back3.png', '.'), ('icon.ico', '.'), ('icon1.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='todo_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
