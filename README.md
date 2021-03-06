This repository contains the Odonto Referral Management System prototype.

![](odonto.screenshot.png)

### Installation

The Odonto RMS prototype is built using [Opal](https://github.com/openhealthcare/opal).

To get started, run the following commands:

```
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata rms/data/clinic_locations.json
    python manage.py create_personas
    python manage.py runserver
```

One color scheme: http://paletton.com/#uid=13C0u0klwCFblS4gZKppQwtuErR

The demo application comes with 3 basic personas.

Linda (username: linda, password: linda1)
is the professional who makes a referral

Mary (username: mary, password: mary1)
is the professional who triages that referral

Matt (username: matt, password: matt1)
is the professional who oversees Mary's response

![supported_by_apperta_lores.png](https://github.com/AppertaFoundation/apperta-image-assets/blob/master/supported_by_apperta_lores.png)
