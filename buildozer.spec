[app]
package.name = kivygame
package.domain = org.kivygame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

android.ndk = 25b
android.sdk = 24
android.api = 33
android.enable_androidx = True
requirements = python3,kivy
android.debug = True

[buildozer]
log_level = 1
warn_on_root = 1
android.copy_python_tests = False
