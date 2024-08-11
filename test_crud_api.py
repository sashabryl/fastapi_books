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
    response = test_client.post("/api/books/", json = book_payload)
    assert response.status_code == 422

    book_payload["publication_year"] = 0
    response = test_client.post("/api/books/", json=book_payload)
    assert response.status_code == 422

