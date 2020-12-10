criar_ambiente:
	python3.8 -m venv ambiente
	ambiente/bin/pip3 install --upgrade pip
	ambiente/bin/pip3 install -r requirements.txt
atualizar_ambiente:
	ambiente/bin/pip3 install --upgrade pip
	ambiente/bin/pip3 install -r requirements.txt
remover_ambiente:
	rm -r ambiente/
executar_projeto:
	ambiente/bin/python3 manage.py runserver