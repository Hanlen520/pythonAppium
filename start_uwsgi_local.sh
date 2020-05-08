#!/bin/bash

# 本地 单个 执行命令
# uwsgi --ini /Users/micllo/Documents/works/GitHub/pythonSelenium/vassals_local/app_uwsgi_local.ini

# 本地 批量 执行命令 emperor：
# 1.批量启动 vassals_local 目录下的 uwsgi 项目
# 2.监视 vassals 目录下的 ini 配置文件
# --uid centos ：让 centos 用户 有权限管理
# --gid centos ：让 centos 组 有权限管理
nohup uwsgi --master --emperor /Users/micllo/Documents/works/GitHub/pythonSelenium/vassals_local --die-on-term --logto /Users/micllo/Documents/works/GitHub/pythonSelenium/Logs/emperor.log > /dev/null 2>&1 &


# 查看 uwsgi 进程ID
# ps -ef | grep -v "grep" | grep uwsgi

# 杀死 uwsgi 进程
# ps aux | grep -v 'grep' | grep uwsgi | awk '{print $2}' | xargs kill -9


ps aux | grep -v 'grep' | grep xcodebuild | awk '{print $2}' | xargs kill -9