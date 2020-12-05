from setuptools import setup, find_packages

with open('README.md') as readme_file:
    long_description = readme_file.read()


if __name__ == "__main__":
    setup(
        name='VSColab',
        version='0.1.1',
        description='SSH into Colab Notebooks and use VSCode for remote development',
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT License',
        packages=find_packages(),
        include_package_data=True,
        author='Anusikh Panda',
        author_email='anusikh2001@gmail.com',
        url = "https://github.com/anusikh/VSColab",
        platforms=["linux", "unix"],
        python_requires=">3.6.0",
        keywords=['VSColab', 'Colab', 'VS']
    )