runscript:
	python run.py

runtestserver:
	python __init__.py

runserver:
	gunicorn -w 5 -b 0.0.0.0:8040 --log-level debug --log-file logs/gunicorn.log __init__:app &
