[app]
title = Dexter Shot
package.name = dextershot
package.domain = org.dexter
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.12.7, hostpython3==3.12.7, kivy==2.3.0, pyjnius
orientation = portrait
fullscreen = 0
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
