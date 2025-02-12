---
title: SPELL linters in MegaLinter
description: misspell, cspell, proselint, vale are available to analyze SPELL files in MegaLinter
---
<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->
<!-- @generated by .automation/build.py, please don't update manually -->
<!-- Instead, update descriptor file at https://github.com/oxsecurity/megalinter/tree/main/megalinter/descriptors/spell.yml -->
# SPELL

## Linters

| Linter                                                                          | Additional                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**misspell**](spell_misspell.md)<br/>[_SPELL_MISSPELL_](spell_misspell.md)     | ![deprecated](https://shields.io/badge/-deprecated-red) [![GitHub stars](https://img.shields.io/github/stars/client9/misspell?cacheSeconds=3600)](https://github.com/client9/misspell) ![autofix](https://shields.io/badge/-autofix-green) |
| [**cspell**](spell_cspell.md)<br/>[_SPELL_CSPELL_](spell_cspell.md)             | [![GitHub stars](https://img.shields.io/github/stars/streetsidesoftware/cspell?cacheSeconds=3600)](https://github.com/streetsidesoftware/cspell)                                                                                           |
| [**proselint**](spell_proselint.md)<br/>[_SPELL_PROSELINT_](spell_proselint.md) | [![GitHub stars](https://img.shields.io/github/stars/amperser/proselint?cacheSeconds=3600)](https://github.com/amperser/proselint)                                                                                                         |
| [**vale**](spell_vale.md)<br/>[_SPELL_VALE_](spell_vale.md)                     | [![GitHub stars](https://img.shields.io/github/stars/errata-ai/vale?cacheSeconds=3600)](https://github.com/errata-ai/vale)                                                                                                                 |

## Linted files

## Configuration in MegaLinter

| Variable                   | Description                   | Default value |
|----------------------------|-------------------------------|---------------|
| SPELL_FILTER_REGEX_INCLUDE | Custom regex including filter |               |
| SPELL_FILTER_REGEX_EXCLUDE | Custom regex excluding filter |               |

