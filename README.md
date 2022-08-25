
# API Lokasi Indonesia

API Data all Province, Distric, Sub Distric and Urban in Indonesia


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

#### Base URL

```http
    [http://127.0.0.1:8000](https://rend-api.herokuapp.com)
```

| Endpoint                        | Method  | Parameter | Description                                                       |
| :------------------------------ | :------ | :---------- | :----------------------------------------------------------------- |
| `/api/provinsi`                 |  `GET`  |  None           |Show all Provinsi                                                  |
| `/api/kabupaten`                |  `GET`  |             |Show all kabupaten                                                 |
| `/api/kabupaten/{id_provinsi}`  |  `GET`  |  id_provinsi: Integer[0-9]           |Show kabupaten by `id_provinsi` (see `id` from `/api/provinsi`)    |
| `/api/kecamatan`                |  `GET`  |             |Show all Kecamatan                                                 |
| `/api/kecamatan/{id_kabupaten}` |  `GET`  |             |Show Kecamatan by `id_kabupaten` (see `id` from `/api/kabupaten`)  |
| `/api/kelurahan`                |  `GET`  |             |Show all Kelurahan                                                 |
| `/api/kelurahan/{id_kecamatan}` |  `GET`  |             |Show Kelurahan by `id_kecamatan` (see `id` from `/api/kecamatan`)  |
| `/api/search/{type}`            |  `GET`  |             |Search data by keyword
#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

