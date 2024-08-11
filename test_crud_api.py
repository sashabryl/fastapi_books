def test_root(test_client):
    response = test_client.get("/api/books")
    assert response.status_code == 200


def test_create_book(test_client, book_payload):
    response = test_client.post("/api/books/", json=book_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("title") == "A book"
    assert response_json.get("author") == "Me"
    assert response_json.get("genre") == "Fiction"
    assert response_json.get("publication_year") == 2025


def test_create_book_wrong_publication_year(test_client, book_payload):
    book_payload["publication_year"] = -2025
    response = test_client.post("/api/books/", json=book_payload)
    assert response.status_code == 422

    book_payload["publication_year"] = 0
    response = test_client.post("/api/books/", json=book_payload)
    assert response.status_code == 422


def test_get_book_by_id(test_client, book_payload):
    test_client.post("/api/books/", json=book_payload)
    response = test_client.get("/api/books/1/")
    assert response.status_code == 200
    assert response.json()["author"] == "Me"

    response = test_client.get("/api/books/2/")
    assert response.status_code == 404


def test_get_books(test_client, book_payload):
    test_client.post("/api/books/", json=book_payload)
    book_payload["title"] = "A book 2"
    test_client.post("/api/books/", json=book_payload)

    response = test_client.get("/api/books/")
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) == 2
    assert response_json[0]["title"] == "A book" if response_json[0]["id"] == 1 else "A book 2"
    assert response_json[1]["title"] == "A book 2" if response_json[1]["id"] == 2 else "A book"


def test_updating_books(test_client, book_payload):
    test_client.post("/api/books/", json=book_payload)
    book_payload["title"] = "A novel"

    response = test_client.put("/api/books/1/", json=book_payload)
    assert response.status_code == 200
    assert response.json()["title"] == "A novel"

    response = test_client.put("/api/books/2/", json=book_payload)
    assert response.status_code == 404

    book_payload["publication_year"] = 0
    response = test_client.put("/api/books/1/", json=book_payload)
    assert response.status_code == 422
