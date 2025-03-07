# Game Grub Point of Sale System

## Overview

Game Grub is a point-of-sale (POS) system designed for a restaurant. This repository contains two implementations:

- A **GUI-based POS system** built with Tkinter in Python.
- A **dynamic webpage** powered by Flask, using RESTful API.

Both implementations reside within the `src` directory under separate packages.

There are test packages in the `test` directory that test all data, data functions, as well as gui functions.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.10**
- **tox** (`pip install tox`)

### Running the Flask Application

To start the Flask web application, navigate to the project directory and run:

```sh
python3 -m flask run
```

This will launch the website with a home page, about page, .

### Running the Tkinter GUI

To launch the desktop GUI application, use the following command:

```sh
python3 -m src
```

## Contributing

Feel free to fork this repository and submit pull requests to improve the system.

## License

This project is licensed under the **MIT License**.
