# FODA Role Classifier

This script reads a FODA (SWOT) analysis from a DOCX file and classifies a team member's role based on the presence of specific keywords. It uses the `python-docx` library to extract text from the DOCX file and determines the most suitable roles for the team member.

## Features

- Reads FODA analysis from a DOCX file.
- Classifies a team member into the top 3 most suitable roles based on keyword matching.
- Supports roles such as CEO, CTO, Backend Developer, Frontend Developer, QA/Analyst, Service Integrator, UI/UX Designer, Technical Support, and Marketing/Communication.

## Requirements

- Python 3.x
- [`python-docx`](https://python-docx.readthedocs.io/en/latest/)

Install dependencies with:

```sh
pip install python-docx