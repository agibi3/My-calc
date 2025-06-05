[app]
# (1) App metadata
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
version = 0.1

# (2) Source inclusion
#    - All your .py and .kv files live at the repo root.
#    - If you have images or other assets in an "assets/" folder, include them below.
source.dir = .
source.include_exts = py,kv,png,jpg,atlas,ttf,wav,ogg,json,csv
# If your assets are under a subfolder, you can explicitly add:
# source.include_patterns = assets/*

# (3) Orientation / window settings
orientation = portrait
fullscreen = 0

# (4) No INTERNET required for an offline app, so leave blank
android.permissions =

# (5) Android API / NDK / architectures
android.minapi = 21
android.api = 31
android.ndk_api = 21

# Starting mid-2025, "android.archs" is the correct key (not "android.arch").
android.archs = armeabi-v7a, arm64-v8a

# (6) Requirements
#    - Use python3 (defaults to 3.10 on most p4a installations)
#    - Pin Kivy to a version that works (2.1.0 or 2.3.0)
#    - Cython is automatically pulled in if needed, but you can specify a version.
requirements = python3,kivy==2.1.0,cython==0.29.36

# (7) Logging level (2 = DEBUG)
log_level = 2

# (8) Icons & Presplash (optional paths under your repo)
# icon.filename = %(source.dir)s/assets/icon.png
# presplash.filename = %(source.dir)s/assets/presplash.png

# (9) If you need to bundle additional JARs/AARs, list them here:
# android.add_jars = libs/some-library.jar

# (10) If you need custom Java sources, point here:
# android.add_src = src/android/java

# (11) (Optional) If you have your own keystore for signing release APKs:
# android.release_keystore = ~/.android/myrelease.keystore
# android.release_keyalias = mykeyalias
# android.release_keystore_pw = mypassword
# android.release_keyalias_pw = mypassword

# (12) Split APK by ABI if you want smaller per-architecture APKs:
# android.split_apk = true
