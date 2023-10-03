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

# How to update a package

E.g. when `python-asyncopenctackclient` was updated to `0.9.0`. In the
package repository:

1. Bump version and add changelog entry:
   `vim AsyncOpenStackClient.spec`

2. Download new sources (tarball):
   `spectool -g -R AsyncOpenStackClient.spec`

3. Create srpm:
   `fedpkg srpm`

4. Check files in srpm (optional):
   `rpmls python-AsyncOpenStackClient-0.9.0-1.fc40.src.rpm`

5. Create a new build via COPR CLI (requires token in `~/.config/copr`, see https://copr.fedorainfracloud.org/api/):
   `copr build @freeipa/neoave ./python-AsyncOpenStackClient-0.9.0-1.fc40.src.rpm`
