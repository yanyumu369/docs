# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.24

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = E:\cmake\bin\cmake.exe

# The command to remove a file.
RM = E:\cmake\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\build

# Include any dependencies generated for this target.
include CMakeFiles/add_item.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/add_item.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/add_item.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/add_item.dir/flags.make

CMakeFiles/add_item.dir/src/add_item.cpp.obj: CMakeFiles/add_item.dir/flags.make
CMakeFiles/add_item.dir/src/add_item.cpp.obj: CMakeFiles/add_item.dir/includes_CXX.rsp
CMakeFiles/add_item.dir/src/add_item.cpp.obj: E:/Desktop/Codefield/Notebook/docs/programme/CodeField/Code_Cpp/cpp_primer/sales_data/src/add_item.cpp
CMakeFiles/add_item.dir/src/add_item.cpp.obj: CMakeFiles/add_item.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/add_item.dir/src/add_item.cpp.obj"
	E:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/add_item.dir/src/add_item.cpp.obj -MF CMakeFiles\add_item.dir\src\add_item.cpp.obj.d -o CMakeFiles\add_item.dir\src\add_item.cpp.obj -c E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\src\add_item.cpp

CMakeFiles/add_item.dir/src/add_item.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/add_item.dir/src/add_item.cpp.i"
	E:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\src\add_item.cpp > CMakeFiles\add_item.dir\src\add_item.cpp.i

CMakeFiles/add_item.dir/src/add_item.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/add_item.dir/src/add_item.cpp.s"
	E:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\src\add_item.cpp -o CMakeFiles\add_item.dir\src\add_item.cpp.s

# Object files for target add_item
add_item_OBJECTS = \
"CMakeFiles/add_item.dir/src/add_item.cpp.obj"

# External object files for target add_item
add_item_EXTERNAL_OBJECTS =

add_item.exe: CMakeFiles/add_item.dir/src/add_item.cpp.obj
add_item.exe: CMakeFiles/add_item.dir/build.make
add_item.exe: libinclude.a
add_item.exe: CMakeFiles/add_item.dir/linklibs.rsp
add_item.exe: CMakeFiles/add_item.dir/objects1.rsp
add_item.exe: CMakeFiles/add_item.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable add_item.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\add_item.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/add_item.dir/build: add_item.exe
.PHONY : CMakeFiles/add_item.dir/build

CMakeFiles/add_item.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\add_item.dir\cmake_clean.cmake
.PHONY : CMakeFiles/add_item.dir/clean

CMakeFiles/add_item.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\build E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\build E:\Desktop\Codefield\Notebook\docs\programme\CodeField\Code_Cpp\cpp_primer\sales_data\build\CMakeFiles\add_item.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/add_item.dir/depend

