[app]

title = Viikon ruokalista
package.name = viikonruokalista
package.domain = org.vlad

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# icon.filename = %(source.dir)s/icon.png
# (розкоментуйте і додайте свій icon.png у корінь проєкту, якщо хочете власну іконку)

android.permissions =

android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
