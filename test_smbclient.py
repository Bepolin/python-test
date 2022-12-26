import os
from datetime import datetime
import platform
from smb.SMBConnection import SMBConnection

# path
# WIN: '\\{remote_host}\{service_name}\{remote_path}'
# ex) \\TABLET-2QRA0CVH\Documents\shere\hoge.txt

# datetime
# mysql: 'YYYY-MM-DD'

username = 'xxx'
password = 'ppp'
local_host = platform.uname().node # なんでも
remote_host = 'hoge.huga.jp' # WINのマシンネーム
remote_ip = '192.168.XX.X' # IPv4 アドレス
remote_port = 139


if __name__ == '__main__':

    # 設定１
    conn = SMBConnection(
        username,
        password,
        local_host,
        remote_host
    )
    conn.connect(remote_ip, remote_port)

    # remote_dir下をlocal_dir下にコピーする
    local_dir = 'share' # users = os.environ.get("github_username")とかでとれる？
    remote_dir = 'hoge/huga/share'
    # 条件を満たすファイル
    service_name= 'Documents'
    date = '2022-10-10'
    dt = datetime.strptime(date, '%Y-%m-%d')

    year_list = []
    for item in conn.listPath(service_name, remote_dir):
        if item.filename == "." or item.filename == "..":
            continue
        if item.isDirectory:
            year_list.append(item.filename)
    
    for year in year_list:
        for item in conn.listPath(service_name, remote_dir+'/'+year, pattern='*.txt'):
            last_write_time = datetime.fromtimestamp(int(item.last_write_time))
            if dt <= last_write_time:
                try:
                    os.makedirs(local_dir+'/'+year)
                except FileExistsError:
                    pass
                local_path = os.path.join(local_dir+'/'+year, item.filename)
                remote_path = os.path.join(remote_dir+'/'+year, item.filename)
                print(local_path)
                print(remote_path)
                with open(local_path, 'wb') as f:
                    conn.retrieveFile(service_name, remote_path, f)

    conn.close()