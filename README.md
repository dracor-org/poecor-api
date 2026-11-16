# poecor-api

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24274702.svg)](https://doi.org/10.5281/zenodo.24274702)

The API of PoeCor ("Poetry Corpora"): a DraCor-like API to the data of the [POSTDATA](https://postdata.linhd.uned.es) project (Poetry Standardization and Linked Open Data, ERC Starting Grant 2015, grant agreement No. 679528; LINHD, UNED Madrid).

> **Archived.** This repository is no longer maintained. poecor.org was shut down in November 2026.

## Background

PoeCor goes back to a demonstrator developed in [CLS INFRA](https://clsinfra.io) (Horizon 2020, grant agreement No. 101004984), work package 7, and described in section 6.2, "Bridging POSTDATA and DraCor as Programmable Corpora", of the report:

- Börner, Ingo; Trilcke, Peer (2023): *On Programmable Corpora*. CLS INFRA D7.1. Zenodo. https://doi.org/10.5281/zenodo.7664964

This repository is a fork of [dh-network/postdata-2-dracor-api](https://github.com/dh-network/postdata-2-dracor-api), which holds the state described in the report (tag `clsinfra-d71-state`; see there for its Zenodo DOI). After the report, the API was reworked here (Docker setup, configuration through environment variables, camelCase property names in the JSON responses) and deployed together with the [PoeCor frontend](https://github.com/dracor-org/poecor-frontend) at poecor.org.

POSTDATA's data is stored in a [Stardog](https://www.stardog.com/get-started/) triple store (https://postdata.linhd.uned.es). The PoeCor API acts as a middleware that sends SPARQL queries to the backend and exposes a REST API modelled on the [DraCor API](https://dracor.org/doc/api), documented in OpenAPI (`openapi.yaml`):

* List corpora
* List poems
* Get details of poem

SPARQL Queries currently available: https://github.com/linhd-postdata/knowledge-graph-queries
Triple Store: https://github.com/linhd-postdata/postdata-stardog

## Local development

The PoeCor API expects several environment variables, among them the credentials
for the POSTDATA triple store. To set those up copy `dev.env.sample` to
`dev.env` and edit the `PD_USER` and `PD_PASSWORD` variables:

```sh
cp dev.env.sample dev.env
# now edit dev.env
```

`config.local.json` contains only placeholder credentials (Stardog defaults on localhost).

### Docker

Our [docker compose file](compose.yaml) makes it easy to run the service in a
docker container:

```sh
docker compose up
```

Open http://localhost:5000 in a browser.

### Python

```sh
python3 -m venv venv
source venv/bin/activate
pip3 freeze > requirements.txt
```

## See also

The [PoeCor frontend](https://github.com/dracor-org/poecor-frontend) is a web
interface that provides a limited [dracor-like](https://dracor.org) view of
poetic corpora.

## Citation

See `CITATION.cff`. The software is archived on Zenodo: https://doi.org/10.5281/zenodo.24274702 (all versions; the release `2026-11-16-archive` is the archived state). When referring to the work, please also cite the report (DOI above).

## Licence

The code is licensed under the [MIT License](LICENSE).
