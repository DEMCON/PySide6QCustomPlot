
project(my_wrapper)
cmake_minimum_required(VERSION 3.18)

# Main tuning variables:
set(MY_SITE_PACKAGES_PATH "${CMAKE_CURRENT_SOURCE_DIR}/.venv/Lib/site-packages")
set(MY_PYTHON_INSTALL_PATH "C:/Python38")
set(MY_QT_INSTALL C:/Qt6/6.3.2/msvc2019_64)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_PREFIX_PATH C:/Qt6/6.3.2/msvc2019_64)
set(CMAKE_BUILD_TYPE Release)

message(STATUS "Python3_ROOT_DIR: ${Python3_ROOT_DIR}")
message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
message(STATUS "Python3_FIND_REGISTRY: ${Python3_FIND_REGISTRY}")
message(STATUS "PY_BUILD_CMAKE_MODULE_NAME: ${PY_BUILD_CMAKE_MODULE_NAME}")

find_package(Qt6 REQUIRED COMPONENTS Core Widgets PrintSupport)

qt_standard_project_setup()

set(SHIBOKEN_OUTPUT_FOLDER "${CMAKE_CURRENT_BINARY_DIR}/OUTPUTDIR")

# Do not use a GLOB here, to allow for usage as OUTPUT in custom command
set(SHIBOKEN_GENERATED_SOURCES
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/pyside6qcustomplot_module_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/pyside6qcustomplot_python.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcp_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcp_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpabstractplottable_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpabstractplottable_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpaxis_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpaxis_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpaxisrect_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpaxisrect_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpaxisticker_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpaxisticker_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpdataselection_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpdataselection_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpgraph_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpgraph_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpgraphdata_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpgraphdata_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpgrid_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpgrid_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayer_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayer_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayerable_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayerable_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayout_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayout_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayoutelement_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayoutelement_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayoutgrid_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplayoutgrid_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplegend_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplegend_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplineending_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcplineending_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcppainter_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcppainter_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpplottableinterface1d_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpplottableinterface1d_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcprange_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcprange_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpscatterstyle_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcpscatterstyle_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcustomplot_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot/qcustomplot_wrapper.h"
)

add_custom_command(
    COMMAND shiboken6 
        --generator-set=shiboken
        --output-directory=OUTPUTDIR
        -I${MY_QT_INSTALL}/include -I${MY_QT_INSTALL}/include/QtCore
        --typesystem-paths=${MY_SITE_PACKAGES_PATH}/PySide6/typesystems
        --enable-pyside-extensions
        --avoid-protected-hack
        ${CMAKE_CURRENT_SOURCE_DIR}/src/wrapper.hpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/bindings.xml
    DEPENDS src/bindings.xml src/wrapper.hpp
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    OUTPUT ${SHIBOKEN_GENERATED_SOURCES}
    COMMENT "Running shiboken6 generator for src/bindings.xml"
)

add_library(
    PySide6QCustomPlot
    SHARED
    src/wrapper.hpp
    src/qcustomplot.cpp
    src/qcustomplot.h
    ${SHIBOKEN_GENERATED_SOURCES}
)

# A bit ugly:
# - include paths to python installation
# - include paths to pyside and shiboken6_generator in .venv
target_include_directories(
    PySide6QCustomPlot
    PRIVATE
    "src"
    "${MY_PYTHON_INSTALL_PATH}/include"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtWidgets"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtGui"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtCore"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtPrintSupport"
    "${MY_SITE_PACKAGES_PATH}/shiboken6_generator/include"
)

# Use the python stable ABI3:
# See also https://docs.python.org/3/c-api/stable.html
target_compile_definitions(
    PySide6QCustomPlot    
    PRIVATE
    "-DPy_LIMITED_API=0x03060000"
)

set_target_properties(
    PySide6QCustomPlot
    PROPERTIES
    SUFFIX ".pyd"
)

target_link_directories(
    PySide6QCustomPlot
    PRIVATE
    "${MY_PYTHON_INSTALL_PATH}/libs"
    ${MY_SITE_PACKAGES_PATH}/shiboken6
    ${MY_SITE_PACKAGES_PATH}/PySide6
)

target_link_libraries(
    PySide6QCustomPlot
    PRIVATE
    Qt6::Widgets
    Qt6::Core
    Qt6::PrintSupport
    shiboken6.abi3
    pyside6.abi3
)

install(
    TARGETS PySide6QCustomPlot
    DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}
)
