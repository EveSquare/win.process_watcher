#       ::::::::::    :::     :::       ::::::::::       ::::::::       ::::::::      :::    :::           :::        :::::::::       ::::::::::
#      :+:           :+:     :+:       :+:             :+:    :+:     :+:    :+:     :+:    :+:         :+: :+:      :+:    :+:      :+:
#     +:+           +:+     +:+       +:+             +:+            +:+    +:+     +:+    +:+        +:+   +:+     +:+    +:+      +:+
#    +#++:++#      +#+     +:+       +#++:++#        +#++:++#++     +#+    +:+     +#+    +:+       +#++:++#++:    +#++:++#:       +#++:++#
#   +#+            +#+   +#+        +#+                    +#+     +#+    +#+     +#+    +#+       +#+     +#+    +#+    +#+      +#+
#  #+#             #+#+#+#         #+#             #+#    #+#     #+#    #+#     #+#    #+#       #+#     #+#    #+#    #+#      #+#
# ##########        ###           ##########       ########       ###########    ########        ###     ###    ###    ###      ##########

import subprocess
import time
# import joblib
import msvcrt
import sys

count_minute = 0

task_name = 'msedge'#Microsoft Edge

def watch():
    proc = subprocess.Popen('tasklist', shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if not str(line).find(task_name) == -1:
            print('active!')
            return True

    return False

try:

    while True:
        if watch():
            count_minute += 1
        else:
            print("not activated")

        time.sleep(60)
except KeyboardInterrupt:
    sys.exit(0)
