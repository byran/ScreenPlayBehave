from setuptools import setup

setup(
    name='screenplay_behave',
    version='1.0.0',
    description='Behave support for the Screen play pattern in Python',
    url='https://github.com/byran/ScreenPlayBehave',
    author='Byran Wills-Heath',
    author_email='byran@adgico.co.uk',
    license='MIT',
    packages=[
        'screenplay_behave'
    ],
    zip_safe=False,
    install_requires=[
        'behave >= 1.2.6',
        'ScreenPlay@git+git://github.com/byran/ScreenPlay@master#ogg=ScreenPlay'
    ]
)
