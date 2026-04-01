#ifdef _WIN32 // на винде
#include <windows.h>
#define LIB_HANDLE HMODULE
#define LOAD_LIB(x) LoadLibraryA(x)
#define GET_FUNC(x, y) GetProcAddress(x, y)
#define CLOSE_LIB(x) FreeLibrary(x)
#else // на линуксе и макОс
#include <dlfcn.h>
#define LIB_HANDLE void*
#define LOAD_LIB(x) dlopen(x, RTLD_LAZY)
#define GET_FUNC(x, y) dlsym(x, y)
#define CLOSE_LIB(x) dlclose(x)
#endif

int main() {
    LIB_HANDLE lib = LOAD_LIB("code128.dll");  // Windows: code128.dll, Linux: ./libcode128.so

    auto Create = (void* (*)(int, int, int))GET_FUNC(lib, "CreateGenerator");
    auto Generate = (int(*)(void*, const char*, const char*))GET_FUNC(lib, "GenerateBarcode");
    auto Destroy = (void(*)(void*))GET_FUNC(lib, "DestroyGenerator");

    void* gen = Create(3, 100, 30);
    Generate(gen, "HELLOPUPS", "C:\\Users\\Retro\\Desktop\\barcode.png");
    Destroy(gen);
    CLOSE_LIB(lib);
    return 0;
}