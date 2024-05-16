# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py','utils.py','types_of_exercise.py','body_part_angle.py'],
    pathex=['F:/AImo/Sport-With-AI-main/.venv/Lib/site-packages',
	'F:/AImo/Sport-With-AI-main'],
    binaries=[],
    datas=[("F:/AImo/Sport-With-AI-main/images","images")],
    hiddenimports=["utils","types_of_exercise","ttkbootstrap.constants","body_part_angle","body_part_angle"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AI教练',
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
)
