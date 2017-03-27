try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Python skelet',
	'author': 'Laura Burticioaia',
	'author_email': 'lburticioaia@luxoft.com',
	'version': '0.1',
	'name': 'Python Project'
	'url': 'https://github.com/Lamabu/skeleton',
	'download_url':'https://github.com/Lamabu/skeleton/archive/0.1.tar.gz'
}

setup(
	scripts=['bin/scapy_task.py']
)	
