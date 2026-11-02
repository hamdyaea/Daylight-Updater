# Daylight Updater

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A Python 3 maintenance GUI and CLI for Debian-based systems. The new version defaults to a **non-destructive preview** and does not automatically chain upgrades, full upgrades, or autoremove.

```sh
python3 DaylightUpdater.py
python3 DaylightUpdater.py upgrade
python3 DaylightUpdater.py upgrade --apply
python3 -m unittest discover -s tests -v
```

Actual changes require root privileges and explicit confirmation. The `--yes` option is intended for deliberately automated administration only. The GUI requires Tkinter. **Do not run on Arch/Manjaro/CachyOS**: it targets APT only. Never use a production server as a test target.

The historical version is preserved on the [old branch](https://github.com/hamdyaea/Daylight-Updater/tree/old).
