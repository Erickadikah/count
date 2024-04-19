from setuptools import setup, find_packages

setup(
    name='rent_counter',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['countdown'],
    description='A Python library for managing rent expiration countdowns',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Erick Adikah',
    author_email='your.email@example.com',
    license='MIT',
    url='https://github.com/Erickadikah/count',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        
    ],
)
