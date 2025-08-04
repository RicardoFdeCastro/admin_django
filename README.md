# admin_django

Projeto de exemplo utilizando o Django Admin.

## Sobre

Este projeto demonstra como configurar e utilizar o Django Admin para gerenciar modelos e dados de uma aplicação Django.

## Requisitos

- Python 3.11+
- Django 4.x+
- (Opcional) SQLite3

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/admin_django.git
   cd admin_django
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requiriments.txt
   ```

4. Realize as migrações:
   ```sh
   python manage.py migrate
   ```

5. Crie um superusuário:
   ```sh
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:
   ```sh
   python manage.py runserver
   ```

Acesse o Django Admin em [http://localhost:8000/admin/](http://localhost:8000/admin/).

## Estrutura do Projeto

- `admin_django/` – Configurações do projeto Django.
- `core/` – Aplicação principal, onde ficam os modelos, views e urls.

## Licença

MIT. Veja o arquivo [LICENSE](LICENSE)
