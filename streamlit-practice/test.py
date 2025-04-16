import os
import subprocess

# Git操作を行うフォルダ
repo_path = r"C:\Users\yoshi\Desktop\test_git"

# カレントディレクトリを移動
os.chdir(repo_path)

# Gitリポジトリの初期化
subprocess.run(["git", "init"], check=True)

# ファイルをステージ
subprocess.run(["git", "add", "."], check=True)