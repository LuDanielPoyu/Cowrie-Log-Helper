# Cowrie Log Classification and Analysis Web Application

## Project Overview

This web application is designed to provide analysis of **cowrie log data** by integrating **pre-trained T5 downstream models** via a Flask API. The project consists of two main sections: "Ask Me" and "Your Help Coach," each offering specific functionalities to classify log data and provide relevant suggestions for cyber attack mitigation.

The frontend is developed using **Django** and interacts with the backend via a **Flask API** to fetch results from a trained T5 model. This README will guide you through the setup, installation, and usage of the project.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  
---

## Features

1. **Classification of Cowrie Logs**:
   - Classifies various parameters from cowrie logs.
   - Provides the type of attack based on input.

2. **Ask Me Function**:
   - Accepts user questions related to cowrie logs and provides answers using a trained T5 model.

3. **Suggestions for Cyber Attack Mitigation**:
   - Offers recommendations based on classified attack types.

4. **User Authentication**:
   - Supports user registration and login for accessing personalized features.

---

## Tech Stack

- **Backend**:
  - **Flask**: Serves the pre-trained T5 model API.
  - **T5 Model**: Used for classification and question answering.

- **Frontend**:
  - **Django**: Provides the web framework for the user interface.
  - **HTML/CSS**: For structuring and styling the web pages.
  - **AJAX**: For handling asynchronous requests between the frontend and backend.

---

## Setup Instructions

### Prerequisites

Make sure you have the following installed:
- Python 3.8+
- Django 4.x
- Flask
- Virtual environment tools (like `venv` or `virtualenv`)
