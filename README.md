# CODE128Project
Реализация кроссплатформенной библиотеки для генерации штрихкода типа code128

# Windows:  
mkdir build && cd build
cmake .. -G "Visual Studio 17 2022" -A x64
cmake --build . --config Release

#Linux/macOS:  
mkdir build && cd build
cmake ..
make
