import PyInstaller.__main__
import shutil,os

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '-igodseye.ico'])
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove("main.spec")
shutil.move("dist/main.exe", "G-Builder.exe")
shutil.rmtree("dist")
