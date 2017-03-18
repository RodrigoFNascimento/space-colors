# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'sprites/*.png', 'sprites' ),
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='game',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
