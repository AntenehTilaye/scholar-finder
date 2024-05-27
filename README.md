# Author Publications API

This project is a Django-based REST API for retrieving author publications from Google Scholar and Semantic Scholar. The API allows users to search for authors and their publications, filter publications by year, and get combined results from both sources.

## Features

- Retrieve all publications for an author from Google Scholar.
- Retrieve publications for an author filtered by year from Google Scholar.
- Retrieve all publications for an author from Semantic Scholar.
- Retrieve publications for an author filtered by year from Semantic Scholar.
- Retrieve combined publications for an author from both Google Scholar and Semantic Scholar.
- Retrieve combined publications for an author filtered by year from both sources.

## Requirements

- Python 3.8+
- Django 3.2+
- djangorestframework 3.12+
- scholarly 1.4.0+
- requests 2.25+

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AntenehTilaye/scholar-finder.git
    cd scholar-finder
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Django project**:
    - this api does not store the data but if you want can by creating a model
    ```bash
    python manage.py migrate
    python manage.py createsuperuser  # Follow the prompts to create a superuser
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Access the API**:

    Open your browser and go to `http://127.0.0.1:8000/`.

## Endpoints
- 'api' is ppms in this code but you can rename it if you want
### 1. Get Author Publications from Google Scholar

- **URL**: `/api/google-scholar/publications/{name}/`
- **Method**: GET
- **Description**: Retrieves all publications for the specified author from Google Scholar.
- **URL Params**:
  - `name` (string): The name of the author.

### 2. Get Author Publications by Year from Google Scholar

- **URL**: `/api/google-scholar/publications/{name}/{year}/`
- **Method**: GET
- **Description**: Retrieves publications for the specified author from Google Scholar, filtered by the specified year.
- **URL Params**:
  - `name` (string): The name of the author.
  - `year` (integer): The publication year to filter by.

### 3. Get Author Publications from Semantic Scholar

- **URL**: `/api/semantic-scholar/publications/{name}/`
- **Method**: GET
- **Description**: Retrieves all publications for the specified author from Semantic Scholar.
- **URL Params**:
  - `name` (string): The name of the author.

### 4. Get Author Publications by Year from Semantic Scholar

- **URL**: `/api/semantic-scholar/publications/{name}/{year}/`
- **Method**: GET
- **Description**: Retrieves publications for the specified author from Semantic Scholar, filtered by the specified year.
- **URL Params**:
  - `name` (string): The name of the author.
  - `year` (integer): The publication year to filter by.

### 5. Get Combined Author Publications

- **URL**: `/api/both-sources/publications/{name}/`
- **Method**: GET
- **Description**: Retrieves combined publications for the specified author from both Google Scholar and Semantic Scholar.
- **URL Params**:
  - `name` (string): The name of the author.

### 6. Get Combined Author Publications by Year

- **URL**: `/api/both-sources/publications/{name}/{year}/`
- **Method**: GET
- **Description**: Retrieves combined publications for the specified author from both Google Scholar and Semantic Scholar, filtered by the specified year.
- **URL Params**:
  - `name` (string): The name of the author.
  - `year` (integer): The publication year to filter by.

## Example Usage

To retrieve all publications for an author named "John Doe" from Google Scholar:

```sh
curl -X GET http://127.0.0.1:8000/api/google-scholar/publications/john%20doe/
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---
