import base64  # Passo 1: Importar a biblioteca base64

# Passo 2: Abrir a imagem no modo binário
with open("icon-7797704_640.png", "rb") as image_file:
    image_data = image_file.read() 

    # Passo 3: Codificar os dados binários para o formato Base64
    base64_string = base64.b64encode(image_data).decode('utf-8')

    # Passo 4: Exibir a string Base64
    print(base64_string)

encoded_string = "SGVsbG8sIEJhc2U2NCE="  # Example Base64 encoded string

