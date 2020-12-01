import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="klasifikasi-py",
    version="0.0.2",
    author="Z. E. Sagata",
    author_email="saga@bahasa.ai",
    description="Official Klasifikasi (https://klasifikasi.com) API Client Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bahasa-ai/klasifikasi-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=required,
)
