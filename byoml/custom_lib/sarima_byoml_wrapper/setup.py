from distutils.core import setup
setup(
    name='sarima_byoml_wrapper',
    version='1.0',
    py_modules=['sarima_byoml_wrapper'],
    install_requires=[
        'statsmodels==0.13.2',
        'pandas',
        'numpy',
    ]
)