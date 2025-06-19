import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "pavithra-rao-1"
SRC_REPO = "src/TextSummarizer"
AUTHOR_EMAIL = "pavithrarao2003@example.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "transformers",
        "datasets",
        "sacrebleu",
        "rouge_score",
        "py7zr",
        "pandas",
        "nltk",
        "tqdm",
        "PyYAML",
        "matplotlib",
        "torch",
        "notebook",
        "boto3",
        "mypy-boto3-s3",
        "python-box==6.0.2",
        "ensure==1.0.2",
        "fastapi==0.78.0",
        "uvicorn==0.18.3",
        "Jinja2==3.1.2",
    ],
)