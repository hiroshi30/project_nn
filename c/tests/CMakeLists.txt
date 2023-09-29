add_executable(test_math)
target_compile_options(test_math PRIVATE ${COMPILE_OPTIONS})
target_compile_features(test_math PRIVATE ${COMPILE_FEATURES})

target_sources(test_math PRIVATE
	src/test_math.c
)

target_include_directories(test_math PRIVATE
	include
	${CMAKE_SOURCE_DIR}/core/include
)

target_link_libraries(test_math
	core
)

add_custom_command(
    TARGET test_math POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_BINARY_DIR}/tests/test_math.exe
    ${CMAKE_SOURCE_DIR}/test_math.exe
)
message("   test_math.exe copied")



add_executable(test_fc)
target_compile_options(test_fc PRIVATE ${COMPILE_OPTIONS})
target_compile_features(test_fc PRIVATE ${COMPILE_FEATURES})

target_sources(test_fc PRIVATE
	src/test_fc.c
)

target_include_directories(test_fc PRIVATE
	include
	${CMAKE_SOURCE_DIR}/core/include
)

target_link_libraries(test_fc
	core
)

add_custom_command(
    TARGET test_fc POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_BINARY_DIR}/tests/test_fc.exe
    ${CMAKE_SOURCE_DIR}/test_fc.exe
)
message("   test_math.exe copied")