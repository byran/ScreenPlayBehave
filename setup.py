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
    entry_points={
        "console_scripts": [
            "screenplay2sphinx = screenplay_behave.create_sphinx_feature_file_page:main",
            "screenplay2sphinx-all = screenplay_behave.create_sphinx_feature_file_page:process_files_in_current_directory"
        ]
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'behave >= 1.2.6',
        'ScreenPlay@git+https://github.com/byran/ScreenPlay@master#ogg=ScreenPlay'
    ]
)
