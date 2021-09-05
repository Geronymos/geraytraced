cmake_minimum_required(VERSION 3.16)

# from https://dev.to/callumspeirs/create-sfml-project-with-cmake-43oc

project(BoilerPlate VERSION 1.0.0.0)

# Windows specific config
IF (WIN32)
    # Include local sfml cmake config
    set(SFML_DIR "${CMAKE_CURRENT_SOURCE_DIR}/SFML-2.5.1/lib/cmake/SFML")
    # Link sfml statically
    set(SFML_STATIC_LIBRARIES TRUE)
ENDIF()

# Find SFML shared libraries
find_package(SFML 2.5.1 COMPONENTS graphics audio REQUIRED)

FILE(
  GLOB
  SOURCES
  "raycaster.cpp"
)

# Compile executable
add_executable(BoilerPlate ${SOURCES})

# Link executable to required SFML modules
target_link_libraries(BoilerPlate sfml-graphics sfml-audio)
