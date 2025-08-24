import os
import datetime
import sys

# 取得當前日期與時間，並格式化為 'YYYY-MM-DD-HHmm'
now = datetime.datetime.now()
date_time_string = now.strftime('%Y-%m-%d-%H%M')

# 取得使用者桌面路徑 (這段保持不變，或使用上述方法修正)
desktop_path = '/var/jenkins_home/demo_logs'

# 組合完整的檔案路徑與名稱
file_name = f'log_{date_time_string}' + '_03_git' +'.txt'
full_path = os.path.join(desktop_path, file_name)

# 創建檔案
try:
    with open(full_path, 'w') as f:
        print(f"檔案 '{full_path}' 已成功創建。")
except IOError as e:
    print(f"創建檔案時發生錯誤: {e}")



sys.exit(0)