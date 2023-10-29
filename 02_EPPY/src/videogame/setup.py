from setuptools import setup

setup(
    name="shmup",
    version="0.0.1",
    packages=["shmup"],
    entry_points={
        "console_scripts": ["shmup = shmup.__main__:main"]
    },
    install_requires=["pygame"]
)