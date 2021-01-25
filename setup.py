from setuptools import setup, find_packages

setup(
    name='hubmap_cell_id_gen_py',
    version='0.1.0',
    description='Utilities for generating unique ids used by HuBMAP Cells API',
    url='https://github.com/hubmapconsortium/hubmap-cell-id-gen-py',
    author='Sean Donahue',
    author_email='seandona@andrew.cmu.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
)
