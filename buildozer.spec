[app]

title = Teste
package.name = Teste
package.domain = org.teste.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivymd,requests,gspread,oauth2client
orientation = portrait

osx.python_version = 3
osx.kivy_version = 2.3.0

fullscreen = 1
android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1

[app.android]

android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
android.ndk_api = 21
android.private_storage = True
android.requirements = kivymd,requests,gspread,oauth2client
