# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'sprites', 'sprites' ),
         ( 'music', 'music' ),
         ( 'Heavitas.ttf', '.'),
         ( 'Roboto-Light.ttf', '.'),
         ( 'high scores.csv', '.')
         ]


a = Analysis(['game.py'],
             pathex=['C:\\Users\\rodri\\Documents\\Code\\The Color That Fell From The Sky'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='The Color That Fell From The Sky',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='C:\\Users\\rodri\\Documents\\Code\\The Color That Fell From The Sky\\icon.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='game')
for d in a.datas:                  #remove redundant paths to pyconfig.h.
   if 'pyconfig' in d[0]:         # This is a workaround to fix a bug
       a.datas.remove(d)          # in PyInstaller
       break
