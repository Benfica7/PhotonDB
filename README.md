## Overview

PhotonDB is a simple Python library designed to manage a collection of JSON-like data structures, referred to as "cells", and provides functionalities for loading, querying, and saving these cells. This library is especially useful for scenarios where structured data needs to be efficiently stored, retrieved, and manipulated.

## Features

- **Load and Save Operations**: PhotonDB allows you to easily load cells from a specified file and save them back after any modifications.

- **Querying**: You can perform queries on the cells to retrieve specific subsets that meet certain criteria.

- **Addition and Removal**: It provides methods to add and remove cells from the collection.

- **Autosave**: An optional autosave feature ensures that any changes made are automatically saved back to the file.

## Installation

To use PhotonDB, simply copy the folder of [PhotonDB](https://github.com/Benfica7/PhotonDB/releases/download/1.0.0/photondb.zip) into your project directory and import it into your Python scripts.

```python
from photondb.manager import PhotonDB
```

### Example

```python
# Create a PhotonDB instance
db = PhotonDB('data.json', autosave=True)

# Add a cell
db.add(name='John Doe', age=30, city='New York')

# Query cells
result = db.get(city='New York')

# Remove cells
db.remove(city='New York')

# Save changes (if autosafe is disabled)
db.save()
```

## Advantages

1. Simplicity and Ease of Use: PhotonDB provides a straightforward and intuitive API for managing structured data, making it accessible to both beginners and experienced developers.

2. Efficient Data Management: It allows for efficient loading, querying, and manipulation of JSON-like data structures, known as "cells", providing a convenient way to handle structured data.

3. Querying Capabilities: PhotonDB enables users to perform queries on the cells, allowing for the retrieval of specific subsets that meet certain criteria. This feature is particularly useful for data filtering and extraction.

4. Addition and Removal Operations: The library offers methods for adding new cells to the collection and removing cells based on specified criteria. This makes it easy to update and maintain the data set.

5. Autosave Functionality: The optional autosave feature ensures that any changes made to the data are automatically saved back to the file. This reduces the risk of data loss and simplifies the workflow.

6. Customizable Saving Process: Users have the flexibility to specify a different file path when saving data, allowing for easy management of multiple datasets or versions.

7. Open-Source and Customizable: PhotonDB is open-source, which means that users can modify and adapt it to suit their specific needs or contribute to its development through the GitHub repository.

8. Platform Agnostic: The library is designed to work on various platforms where Python is supported, making it versatile and compatible with different operating systems.

9. No External Dependencies: PhotonDB is a self-contained library and does not rely on any external dependencies, ensuring minimal setup and installation requirements.

## Contributing

If you have any suggestions, bug reports, or would like to contribute to PhotonDB, please open an issue or submit a pull request on the [GitHub repository](https://github.com/Benfica7/PhotonDB).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
