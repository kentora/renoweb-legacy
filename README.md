# Renoweb_Legacy

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
# [![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

# [![Discord][discord-shield]][discord]
# [![Community Forum][forum-shield]][forum]

**Dette plugin er i stor stil inspireret af [Briis/RenoWeb](https://github.com/briis/renoweb).**

Derudover er det mit første HACS plugin, og noget af det første jeg skriver i Python. Gør mig gerne opmærksom på bad practices og ting der kan gøres smartere.

Henter informationer om næste tømningsdag fra RenoWeb Legacy løsninger, det vil sige løsninger der ikke understøttes af Briis/RenoWeb (Tror jeg).

**This component will set up the following platforms.**

| Platform        | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| `sensor`        | Show info from Renoweb_Legacy API.                                        |

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `renoweb_legacy`.
4. Download _all_ the files from the `custom_components/renoweb_legacy/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Renoweb_Legacy"

## Configuration is done in the UI
Indtast først host til RenoWeb, eks. `https://faxe.renoweb.dk`, herefter dit adrid, som findes ved at søge efter din adresse, mens du kigger efter i netværksfanen i dit debug tool. Her skal du bruge "value" værdien fra din adresse.

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/kentora
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/kentora/renoweb-legacy.svg?style=for-the-badge
[commits]: https://github.com/kentora/renoweb-legacy/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/kentora/renoweb-legacy.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40kentora-blue.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/kentora/renoweb-legacy.svg?style=for-the-badge
[releases]: https://github.com/kentora/renoweb-legacy/releases
[user_profile]: https://github.com/kentora
