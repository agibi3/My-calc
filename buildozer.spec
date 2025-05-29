[app]
title = My Calc
package.name = mycalc
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
osx.python_version = 3

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
android.ndk_api = 21
# Skip Google Play services, signing, or AndroidX stuff for simplicity
requirements = python3,kivy
# Permissions (uncomment if needed)
# android.permissions = INTERNET
