from setuptools import setup, find_packages

# with open("README.md") as f:
#     long_description = f.read()

setup(
    name='jeta',
    version='1.0.2',
    description='Modules supporting JWST engineering telemetry archive.',
    license='BSD 3-Clause',
    long_description="",
    author='David Kauffman',
    author_email='dkauffman@stsci.edu',
    url='https://github.com/spacetelescope/jeta',
    packages=find_packages(include=[
        'jeta',
        'jeta.archive',
        'jeta.archive.derived',
        'jeta.config',
        'jeta.core',
        'jeta.ingest',
        'jeta.tests',
        ]),
    py_modules=['jeta.archive.version'],
    scripts=[
        'scripts/sql/create.archive.meta.sql'
    ],
    classifiers=[
        'Development Status :: v1.0.2',
        'License :: BSD 3-Clause',
    ]
)
