# Archivo Makefile

test::
	@echo Running UnitTest ....
	@coverage run --omit="fann/*,**/migrations/*,manage.py,**/test*"\  manage.py test

report:
	@coverage report

report_html: test
	@coverage html -d .html_coverage
	@nohup firefox .html_coverage/index.html > /dev/null &

clean:
	@rm -r .coverage .html_coverage
