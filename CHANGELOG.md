# Flask Reverse Proxy Middleware - Change log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

* Refactored `app.py` to prevent creating an application on import
* Improved versioning support in `setup.py`

## [0.2.1] - 2019-03-02

### Fixed

* Correcting documentation for `REVERSE_PROXY_PATH` config option
* Guarding against missing `REVERSE_PROXY_PATH` config option

## [0.2.0] - 2019-03-02

### Changed

* Wrapping around Flask app rather than a WSGI app
* Incorporating `werkzeug.contrib.fixers.ProxyFix` middleware
* Improved handling of pre-release versions in `setup.py` when running in CI/CD

## [0.1.1] - 2019-03-01

### Fixed

* Correcting prefix value in usage example to include a preceding forward slash

## [0.1.0] - 2019-02-24

### Added

* Initial version based on middleware developed for the BAS People (Sensitive) API
