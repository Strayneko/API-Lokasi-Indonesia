# API Lokasi Indonesia

An API that provides all the names of Province, Districts, Sub Ddistrictsistrics, and Urban in Indonesia

## Getting Started

1.Clone project repository

```bash
    git clone https://github.com/Strayneko/API-Lokasi-Indonesia.git
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

| Endpoint                                                                                              | Method | Parameter      | Type         | Description                                                       |
| :---------------------------------------------------------------------------------------------------- | :----- | :------------- | :----------- | :---------------------------------------------------------------- |
| [`/api/provinsi`](https://strayneko.herokuapp.com/api/provinsi)                                       | `GET`  | None           | None         | Show all Provinsi                                                 |
| [`/api/kabupaten`](https://strayneko.herokuapp.com/api/kabupaten)                                     | `GET`  | None           | None         | Show all kabupaten                                                |
| [`/api/kabupaten/{id_provinsi}`](https://strayneko.herokuapp.com/api/kabupaten/1)                     | `GET`  | id_provinsi    | Integer[0-9] | Show kabupaten by `id_provinsi` (see `id` from `/api/provinsi`)   |
| [`/api/kecamatan?limit=10&offset=0`](https://strayneko.herokuapp.com/api/kecamatan?limit=10&offset=0) | `GET`  | limit & offset | Integer[0-9] | Show all Kecamatan                                                |
| [`/api/kecamatan/{id_kabupaten}`](https://strayneko.herokuapp.com/api/kecamatan/1)                    | `GET`  | id_kabupaten   | Integer[0-9] | Show Kecamatan by `id_kabupaten` (see `id` from `/api/kabupaten`) |
| [`/api/kelurahan?limit=10&offset=0`](https://strayneko.herokuapp.com/api/kelurahan?limit=10&offset=0) | `GET`  | limit & offset | Integer[0-9] | Show all Kelurahan                                                |
| [`/api/kelurahan/{id_kecamatan}`](https://strayneko.herokuapp.com/api/kelurahan/1)                    | `GET`  | id_kecamatan   | Integer[0-9] | Show Kelurahan by `id_kecamatan` (see `id` from `/api/kecamatan`) |
| `/api/search/{type}`                                                                                  | `GET`  |                |              | Search data by keyword                                            |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.
