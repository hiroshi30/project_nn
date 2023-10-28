add_library(print SHARED)

target_compile_options(print PRIVATE ${COMPILE_OPTIONS})
target_compile_features(print PRIVATE ${COMPILE_FEATURES})

target_sources(print PRIVATE
	src/print.c
)

target_include_directories(print PRIVATE
	core
	src
)

target_include_directories(print PUBLIC
	include
)

target_link_libraries(print PRIVATE
	core
)

set_target_properties(print PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/)
