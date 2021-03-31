# Spec files of mrack dependencies

> Mrack specfile lives at: https://github.com/neoave/mrack/blob/master/mrack.spec

These packages are being built and hosted by COPR: https://copr.fedorainfracloud.org/coprs/g/freeipa/neoave

You can install them, and mrack, by enabling the repo:

```bash
$ dnf copr enable @freeipa/neoave
```
They are available for Fedora since release 32.

Depency tree:
```
mrack
└── python3-AsyncOpenStackClient
    └── python3-simple-rest-client
        ├── python3-json-encoder
        └── python3-status
```

Not required currently:

```
python3-pytest-httpserver
└── python3-typing
```
