# API Lokasi Indonesia

An API that provices the names of Province, Districts, Sub Districts and Urban in Indonesia

## Getting Started

1.Clone project repository

```bash
    git clone https://github.com/RennnD/API-Lokasi-Indonesia.git
```

2.Change directory to repository folder

```bash
    cd API-Lokasi-Indonesia
```

3.Install all dependencies required for this project

```bash
    pip install -r requirements.txt
```

4.Run the local server

- windows

```bash
    python main.py
```

- Mac/Linux

```bash
    python3 main.py
```

## Basic Usage

### Base URL

[`http://127.0.0.1:8000`](https://strayneko.herokuapp.com)

### Endpoint Docs

[`http://127.0.0.1:8000/docs`](https://strayneko.herokuapp.com/docs)

| Endpoint                                                                                                      | Method | Parameter           | Type                                                | Description                                                       |
| :------------------------------------------------------------------------------------------------------------ | :----- | :------------------ | :-------------------------------------------------- | :---------------------------------------------------------------- |
| [`/api/provinsi`](https://strayneko.herokuapp.com/api/provinsi)                                               | `GET`  | None                | None                                                | Show all Provinsi                                                 |
| [`/api/kabupaten`](https://strayneko.herokuapp.com/api/kabupaten)                                             | `GET`  | None                | None                                                | Show all kabupaten                                                |
| [`/api/kabupaten/{id_provinsi}`](https://strayneko.herokuapp.com/api/kabupaten/1)                             | `GET`  | id_provinsi         | Integer 0-9                                         | Show kabupaten by `id_provinsi` (see `id` from `/api/provinsi`)   |
| [`/api/kecamatan?limit=10&offset=0`](https://strayneko.herokuapp.com/api/kecamatan?limit=10&offset=0)         | `GET`  | limit & offset      | Integer 0-9                                         | Show all Kecamatan                                                |
| [`/api/kecamatan/{id_kabupaten}`](https://strayneko.herokuapp.com/api/kecamatan/1)                            | `GET`  | id_kabupaten        | Integer 0-9                                         | Show Kecamatan by `id_kabupaten` (see `id` from `/api/kabupaten`) |
| [`/api/kelurahan?limit=10&offset=0`](https://strayneko.herokuapp.com/api/kelurahan?limit=10&offset=0)         | `GET`  | limit & offset      | Integer 0-9                                         | Show all Kelurahan                                                |
| [`/api/kelurahan/{id_kecamatan}`](https://strayneko.herokuapp.com/api/kelurahan/1)                            | `GET`  | id_kecamatan        | Integer 0-9                                         | Show Kelurahan by `id_kecamatan` (see `id` from `/api/kecamatan`) |
| [`/api/search/{area_type}/{id_area}`](https://strayneko.herokuapp.com/api/search/kelurahan/13)                | `GET`  | area_type & id_area | String provinsi, kabupaten, kelurahan & Integer 0-9 | Filter data by `id_area`                                          |
| [`/api/search/{area_type}/?keyword=`](https://strayneko.herokuapp.com/api/search/kecamatan/?keyword=pemalang) | `GET`  | keyword             | String a-Z                                          | Search data by keyword                                            |

## Public Use

[https://strayneko.herokuapp.com/](https://strayneko.herokuapp.com/)

## License

This project is licensed under the [`Apache License`](https://github.com/Strayneko/API-Lokasi-Indonesia/blob/main/LICENSE), Version 2.0.
