import subprocess
import sys

b=True

# 设置 Python 路径（根据你的实际安装位置修改）
python_path = "C:/Users/someone/AppData/Local/Programs/Python/Python38/python.exe"

# 使用安全的 subprocess 调用 pip
try:
    result = subprocess.run(
        [python_path, "-m", "pip", "list"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60  # 设置超时防止卡死
    )
    print(result.stdout)
    if result.stderr:
        print("错误信息:", result.stderr)
except Exception as e:
    print("发生错误:", str(e))



while b:
    a = input("按q退出")
    if a == "q":
        b=False
sys.exit()