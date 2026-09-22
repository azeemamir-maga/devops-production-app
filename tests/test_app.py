def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Test"}
    )

    assert response.status_code == 201
