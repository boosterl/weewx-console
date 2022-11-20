# WeeWX Console

A CLI-friendly skin for weewx. Inspired by [wttr.in](https://github.com/chubin/wttr.in).
Using this skin, you can query the status of your weather station using your favorite console HTTP client (curl, httpie, wget...).

![example.png](img/example.png)

## Installation

Clone the repo and run the installer:
```
wee_extension --install weewx-console
```

Restart weewx:
```
sudo systemctl restart weewx
```

## Usage

To access the current weather coniditions, with for example `curl`, just issue:
```
curl http://$WEEWX_INSTANCE/weewx/console/current
```

Statistics per week/month/year can also be fetched:
```
curl http://$WEEWX_INSTANCE/weewx/console/week
curl http://$WEEWX_INSTANCE/weewx/console/month
curl http://$WEEWX_INSTANCE/weewx/console/year
```

Information about the station can be fetched with:
```
curl http://$WEEWX_INSTANCE/weewx/console/about
```
