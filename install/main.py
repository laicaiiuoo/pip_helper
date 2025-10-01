import subprocess
import sys

b=True

# 设置 Python 路径（根据你的实际安装位置修改）
python_path=input('请输入python.exe的路径(如C:\\Python39\\python.exe)(注意:请使用双反斜杠或单正斜杠): ')


# 安全读取文件
try:
    with open('install/sj.txt', 'r', encoding='utf-8') as file:
        txt = file.read()
    print(txt)
except FileNotFoundError:
    print("文件 sj.txt 不存在，跳过读取")


# 获取用户输入
read = input("写出想要安装的库(英文): ").strip()
if not read:  # 检查输入是否为空
    print("错误：未输入库名")
    exit(1)


try:
    with open('yuan.txt', 'r', encoding='utf-8') as file:
        txt1 = file.read()
    print('选择下载源：（输入编号）')
    print(txt1)
    c=input()
    if c=='1':
        print('已选择清华源')
        yuan='https://pypi.tuna.tsinghua.edu.cn/simple'
    elif c=='2':
        print('已选择阿里源')
        yuan='https://mirrors.aliyun.com/pypi/simple/'
    elif c=='4':
        print('已选择豆瓣源')
        yuan='https://pypi.doubanio.com/simple/'
    elif c=='3':
        print('已选择中科大源')
        yuan='https://pypi.mirrors.ustc.edu.cn/simple/'
    elif c=='5':
        print('已选择华为源')
        yuan='https://mirrors.huaweicloud.com/repository/pypi/simple'
    else:
        print('输入错误，默认使用清华源')
        yuan='https://pypi.tuna.tsinghua.edu.cn/simple'
except FileNotFoundError:
    print("文件 yuan.txt 不存在，跳过读取")


# 使用安全的 subprocess 调用 pip
try:
    result = subprocess.run(
        [python_path, "-m", "pip", "install", read, "-i",yuan],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60  # 设置超时防止卡死
    )
    print(result.stdout)
    if result.stderr:
        print("错误信息:", result.stderr)
    print("返回码:", result.returncode)
except subprocess.TimeoutExpired:
    print("安装超时，请检查网络或手动安装")
except Exception as e:
    print("发生错误:", str(e))



a = input("回车退出")
sys.exit()