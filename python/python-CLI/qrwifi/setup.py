from setuptools import setup, find_packages

setup(
    # mandatory
    name="qrwifi",
    # mandatory
    version="0.1",
    # mandatory
    author_email="leoluyi@gmail.com",
    packages=['qrwifi'],
    package_data={},
    install_requires=['pyqrcode', 'numpy', 'click'],
    entry_points={
        'console_scripts': ['qrwifi = qrwifi.cli:qrwifi']
    }
)
