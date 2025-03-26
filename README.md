# buildozer-apk-action-test
Testing different github actions to make kivy apps using bulldozer.

## Test 01

Tested Action :
```yml
on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build APK
        uses: digreatbrian/buildozer-action@v2
        with:
          python-version: 3.8
          buildozer-cmd: buildozer -v android debug

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: ./bin/*.apk
```

