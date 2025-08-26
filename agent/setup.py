from setuptools import setup, find_packages
setup(
    name="driftsiren-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["driftsiren-agent=ds_agent.client:main"]},
)
