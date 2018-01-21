# Black Hole
A simple Desktop organizer that moves all files and folders from /Desktop to /Downloads/Singularity

## How it works

Using Python's os and shutil modules, we check if the Singularity folder under Downloads already exists. If it doesn't, create it.
Then, for every file or folder on Desktop, we send it into the Singularity.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## References

OS module: https://docs.python.org/3/library/os.html#module-os
SHUTIL module: https://docs.python.org/3/library/shutil.html
