# Build Process

The system monitoring engine is written in C++ and must be compiled before use.

The project provides an automated build script.

Location:

```
scripts/build.sh
```

Running the script:

```
./scripts/build.sh
```

This script:

1. Creates the `bin` directory if necessary
2. Compiles the C++ monitoring engine
3. Generates the binary `bin/system_monitor`

The build process is automatically executed when a GitHub Codespace environment is created.
