add_executable(svm)

target_compile_options(svm PRIVATE ${COMPILE_OPTIONS} -static-libgcc)
target_compile_features(svm PRIVATE ${COMPILE_FEATURES})

target_sources(svm PRIVATE
	src/main.c
)

target_include_directories(svm PRIVATE
	include
    core
    external/SDL/include
)

target_link_directories(svm PRIVATE
    external/SDL/lib
)

target_link_libraries(svm
    core

    mingw32
    SDL2main
    SDL2

    #m
    #dinput8
    #dxguid
    #dxerr8
    #user32

    version
    uuid
    shell32

    gdi32
    winmm
    imm32
    ole32
    oleaut32
    setupapi
)

set_target_properties(svm PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/)