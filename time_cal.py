#s24001
#カレンダーを表示する
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y年%m月%d日 %H:%M:%S"))

import calendar as cal
print(cal.month(2024,6))
