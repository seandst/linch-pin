from setuptools import setup, find_packages
from pip.req import parse_requirements
import os

# reading requirements from requirements.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
reqs_file = 'requirements.txt'.format(dir_path)
with open(reqs_file) as f:
    required = f.read().splitlines()

ignore_dir = ['.git']

setup(
    name='linchpin',
    version='1.0.0a1',
    description = 'Ansible based multi cloud orchestrator',
    author = 'samvaran kashyap rallabandi',
    author_email = 'samvaran.kashyap@gmail.com',
    url = 'http://linch-pin.readthedocs.io/',
    setup_requires=required,
    install_requires=required,
    entry_points='''
        [console_scripts]
        linchpin=linchpin:cli
    ''',
    extras_require = {
        'krbV': ["python-krbV"],
        'beaker':  ['beaker-client==23.3'],
        'docs': ["docutils","sphinx","sphinx_rtd_theme"],
        'tests': ["nose","mock","coverage"],
        'libvirt': ["libvirt-python>=3.0.0", "lxml"],
    },
    dependency_links = ['https://github.com/eevee/camel/archive/v0.1.tar.gz#egg=camel-99.1'],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    scripts=['scripts/linchpin_complete.sh']
)
