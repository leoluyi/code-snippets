from setuptools import setup, find_packages

setup(
    # mandatory
    name="qrwifi",
    version="0.1",
    author_email="leoluyi@gmail.com",

    # package settings
    packages=['qrwifi'],
    package_data={},
    install_requires=['pyqrcode', 'numpy', 'click'],
    entry_points={
        'console_scripts': ['qrwifi = qrwifi.cli:qrwifi']
    }
)
