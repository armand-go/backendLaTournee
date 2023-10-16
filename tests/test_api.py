from fastapi.testclient import TestClient
from app import serve


client = TestClient(serve)


def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "."


def test_get_coca_cola_33():
    id = "coca-cola-33"
    response = client.get(f"/data/{id}")

    assert response.status_code == 200
    assert response.json() == {
        "sku": "coca-cola-33",
        "brand": "Coca-Cola",
        "packing": 24,
        "deposit": 0.2,
        "preparation_in_crate": True,
    }


def test_raise_not_found():
    id = "coca-cola-404"
    response = client.get(f"/data/{id}")

    assert response.status_code == 404
    assert response.json() == {"detail": "DATA: not found"}


def test_order_dispatch():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "coca-cola-33", "UnitCount": 3}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 0, "Slot20": 1, "Slot6": 0, "Supplier": 0}


def test_order_dispatch_supplier():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "coca-cola-33", "UnitCount": 24}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 0, "Slot20": 0, "Slot6": 0, "Supplier": 1}


def test_order_dispatch_supplier_plus_20():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "coca-cola-33", "UnitCount": 25}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 0, "Slot20": 1, "Slot6": 0, "Supplier": 1}


def test_order_dispatch_two_suppliers():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "coca-cola-33", "UnitCount": 23}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 0, "Slot20": 2, "Slot6": 0, "Supplier": 0}


def test_order_dispatch_orangina_count_equals_packing():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "orangina-25", "UnitCount": 39}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 2, "Slot20": 0, "Slot6": 0, "Supplier": 0}


def test_order_dispatch_orangina_12():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "orangina-25", "UnitCount": 12}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 0, "Slot20": 0, "Slot6": 1, "Supplier": 0}


def test_order_dispatch_orangina_24():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "orangina-25", "UnitCount": 24}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 1, "Slot20": 0, "Slot6": 0, "Supplier": 0}


def test_order_dispatch_orangina_26():
    payload = [{"ID": "1", "OrderID": "abc", "SKU": "orangina-25", "UnitCount": 26}]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 1, "Slot20": 0, "Slot6": 1, "Supplier": 0}


def test_order_dispatch_several_products():
    payload = [
        {"ID": "1", "OrderID": "abc", "SKU": "orangina-25", "UnitCount": 39},
        {"ID": "2", "OrderID": "abc", "SKU": "coca-cola-33", "UnitCount": 23},
    ]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 2, "Slot20": 2, "Slot6": 0, "Supplier": 0}


def test_order_dispatch_several_more_products():
    payload = [
        {"ID": "1", "OrderID": "abc", "SKU": "orangina-25", "UnitCount": 39},
        {"ID": "2", "OrderID": "abc", "SKU": "coca-cola-33", "UnitCount": 23},
        {"ID": "2", "OrderID": "abc", "SKU": "la-tournee-yaourt-vanille-350", "UnitCount": 14},
    ]

    response = client.post("/orders/dispatch", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Slot12": 3, "Slot20": 2, "Slot6": 1, "Supplier": 0}
