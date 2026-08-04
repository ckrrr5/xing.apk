[app]
# ========== 应用基础信息 ==========
title = MyKivyGame
package.name = kivygame
package.domain = org.kivygame

version = 0.1
version.code = 1

# 源码目录，main.py放在这里
source.dir = .

# 需要打进APK的文件后缀，游戏建议加上gif,mp3,wav,txt,json
source.include_exts = py,png,jpg,kv,atlas,gif,mp3,wav,txt,json

# 排除不需要打包的文件夹
source.exclude_dirs = tests, bin, .buildozer

# ========== Python依赖 ==========
# 游戏：python3,kivy；如果用kivymd就写 python3,kivy,kivymd
requirements = python3,kivy

# ========== 屏幕方向 ==========
# portrait竖屏；landscape横屏；all全部；sensorLandscape自动横屏
orientation = portrait

# ========== Android系统配置 ==========
android.api = 33
android.ndk = 25b
android.sdk = 24
android.minapi = 21

# 启用AndroidX，新版本kivy必须开
android.enable_androidx = True

# 调试APK开关
android.debug = True

# 权限，游戏需要网络就加上 INTERNET
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# 全屏游戏（隐藏状态栏）
android.fullscreen = 1

# 启动引导器，kivy固定 sdl2_gradle
android.bootstrap = sdl2_gradle

# 图标（把icon.png放到项目根目录，不需要就注释）
#icon.filename = icon.png

# ========== Buildozer 全局设置 ==========
[buildozer]
# 日志等级 2=debug看详细输出，排错必开
log_level = 2

# root运行警告，CI环境关掉
warn_on_root = 0

# 编译产物输出目录，APK输出到 bin/
#bin_dir = ./bin

# 构建缓存目录
#build_dir = ./.buildozer
