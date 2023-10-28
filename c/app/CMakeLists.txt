add_executable(app)

target_compile_options(app PRIVATE ${COMPILE_OPTIONS} -static-libgcc)
target_compile_features(app PRIVATE ${COMPILE_FEATURES})

target_sources(app PRIVATE
	src/main.c
)

target_include_directories(app PRIVATE
    ${CMAKE_SOURCE_DIR}/external/SDL/include
    core
    print
)

target_link_directories(app PRIVATE
    ${CMAKE_SOURCE_DIR}/external/SDL/lib
)

target_link_libraries(app PRIVATE
    core
    print

    mingw32
    SDL2main
    SDL2

    m
    dinput8
    dxguid
    dxerr8
    user32

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

set_target_properties(app PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/)