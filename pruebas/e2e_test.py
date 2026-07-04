import requests
import time
import json
import os

import random

# Rutas a través del API Gateway
AUTH_URL = "http://localhost:3000/api/v1/auth"
CLUSTERING_URL = "http://localhost:3000/api/v1/clustering/integrator"

# Un correo nuevo para probar que el registro y login pasen
EMAIL_NEW_USER = f"test_user_{random.randint(1000, 9999)}@gmail.com"
EMAIL_RECOVERY = "eduartrob@gmail.com" # Tu correo real para que te llegue el PIN
PASSWORD_TEST = "passwordSeguro123"
FCM_TOKEN_TEST = "firebase_fcm_token_mock_999"

def print_step(title):
    print(f"\n{'='*50}\n🚀 PASO: {title}\n{'='*50}")

def test_e2e():
    # 1. Registro
    print_step("Registro en Auth")
    res = requests.post(f"{AUTH_URL}/register", json={
        "email": EMAIL_NEW_USER,
        "password": PASSWORD_TEST,
        "roleName": "ALUMNO",
        "fullName": "Eduart Rob Test",
        "username": EMAIL_NEW_USER.split('@')[0]
    })
    print(res.status_code, res.text)

    # 2. Login con FCM
    print_step("Login con envío de FCM Token (RabbitMQ Event)")
    res = requests.post(f"{AUTH_URL}/login", json={
        "email": EMAIL_NEW_USER,
        "password": PASSWORD_TEST,
        "fcmToken": FCM_TOKEN_TEST
    })
    print(res.status_code, res.text)
    if res.status_code == 200:
        jwt_token = res.json().get("token")
        
    # 3. Recuperar Contraseña
    print_step("Recuperación de Contraseña (RabbitMQ Email Event)")
    res = requests.post(f"{AUTH_URL}/recover-password", json={
        "email": EMAIL_RECOVERY
    })
    print(res.status_code, res.text)
    print(f">>> Revisa tu correo de {EMAIL_RECOVERY} para ver si llegó el PIN.")
    
    # 4. Obtener Nichos (Océanos Azules)
    print_step("Visualizar Nichos / Océanos Azules")
    headers = {"Authorization": f"Bearer {jwt_token}"} if 'jwt_token' in locals() else {}
    res = requests.get(f"{CLUSTERING_URL}/blue-ocean-niches", headers=headers)
    print(res.status_code)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    # 5. Subir Proyecto Innovador
    print_step("Análisis de Proyecto: Océano Azul (innovador.txt)")
    with open("innovador.txt", "rb") as f:
        files = {"file": ("innovador.txt", f, "text/plain")}
        res = requests.post(f"{CLUSTERING_URL}/process-local-project?project_id=test_innovador", files=files, headers=headers)
        print(res.status_code)
        try:
            print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        except:
            print(res.text)

    # 6. Subir Proyecto Copia
    print_step("Análisis de Proyecto: Copia Genérica (copia.txt)")
    with open("copia.txt", "rb") as f:
        files = {"file": ("copia.txt", f, "text/plain")}
        res = requests.post(f"{CLUSTERING_URL}/process-local-project?project_id=test_copia", files=files, headers=headers)
        print(res.status_code)
        try:
            print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        except:
            print(res.text)

if __name__ == "__main__":
    test_e2e()
