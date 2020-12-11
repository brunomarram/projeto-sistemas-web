instalar_dependencias:
	sudo apt-get install python3-venv
criar_ambiente:
	python3 -m venv ambiente
	ambiente/bin/pip3 install --upgrade pip
	ambiente/bin/pip3 install -r requirements.txt
atualizar_ambiente:
	ambiente/bin/pip3 install --upgrade pip
	ambiente/bin/pip3 install -r requirements.txt
remover_ambiente:
	rm -r ambiente/
criar_bd:
	ambiente/bin/python manage.py migrate
	ambiente/bin/python manage.py makemigrations
executar_projeto:
	ambiente/bin/python3 manage.py runserver