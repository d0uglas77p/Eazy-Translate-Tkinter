# specfile.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['eazy_translate.py'],
             pathex=['C:\\caminho\\para\\seu\\script'],
             binaries=[],
             datas=[],
             codes=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher,
         noarchive=False)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Eazy Translate',
          debug=False,
          bootloader_ignore_signals=False,
          bootloader_includes_py=False,
          bootloader_ignore_msi=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          upx_custom_i386=[],
          upx_custom_x86_64=[],
          upx_custom_arm=[],
          upx_custom_mips=[],
          upx_custom_ppc=[],
          upx_custom_sparc=[],
          upx_custom_alpha=[],
          upx_custom_ia64=[],
          upx_custom_hppa=[],
          upx_custom_hppa64=[],
          upx_custom_m68k=[],
          upx_custom_mips64=[])
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               [],
               [],
               upx=True,
               upx_exclude=[],
               upx_custom_i386=[],
               upx_custom_x86_64=[],
               upx_custom_arm=[],
               upx_custom_mips=[],
               upx_custom_ppc=[],
               upx_custom_sparc=[],
               upx_custom_alpha=[],
               upx_custom_ia64=[],
               upx_custom_hppa=[],
               upx_custom_hppa64=[],
               upx_custom_m68k=[],
               upx_custom_mips64=[])
