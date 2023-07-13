# SOTA FLE template generator

A toy for WU7H.

Pick one or the other and rename to sftg.py.

sftg_1.py example use:

```
$ ./sftg_1.py --help
usage: sftg_1.py [-h] [--mycall MYCALL] [--date DATE] mysota

SOTA FLE template generator

positional arguments:
  mysota           my SOTA summit reference

options:
  -h, --help       show this help message and exit
  --mycall MYCALL  my callsign (default: WU7H)
  --date DATE      date (YYYY-MM-DD) (default: today, 2023-07-13
$ ./sftg_1.py w6/sc-338
mycall WU7H
date 2023-07-13
mysota W6/SC-338
$ ./sftg_1.py w6/sc-338 --mycall w7s
mycall W7S
date 2023-07-13
mysota W6/SC-338
$ ./sftg_1.py w6/sc-338 --date 2023-07-04
mycall WU7H
date 2023-07-04
mysota W6/SC-338
$ ./sftg_1.py w6/sc-338 --date 2023-07-04 --mycall w7s
mycall W7S
date 2023-07-04
mysota W6/SC-338
$ ./sftg_1.py w6/sc-338 --date 2023-07-04 --mycall w7s > template.fle
$
```

sftg_2.py example use:

```
$ ./sftg_2.py --help
usage: sftg_2.py [-h] mysota [date]

SOTA FLE template generator

positional arguments:
  mysota      my SOTA summit reference
  date        date (YYYY-MM-DD) (default: today, 2023-07-13)

options:
  -h, --help  show this help message and exit
$ ./sftg_2.py w6/sc-338
mycall WU7H
date 2023-07-13
mysota W6/SC-338
$ ./sftg_2.py w6/sc-338 2023-07-04
mycall WU7H
date 2023-07-04
mysota W6/SC-338
$ ./sftg_2.py w6/sc-338 2023-07-04 > template.fle
$
```
