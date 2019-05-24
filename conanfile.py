#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, CMake
import os


class GlmConan(ConanFile):
    name = "glm"
    version = "0.9.9.5"
    description = "OpenGL Mathematics (GLM)"
    topics = ("conan", "glm", "opengl", "mathematics")
    url = "https://github.com/bincrafters/conan-glm"
    homepage = "https://github.com/g-truc/glm"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    generators = "cmake"

    exports = ["LICENSE.md"]
    exports_sources = [
        "CMakeLists.txt",
        "0001-Remove-architecture-check-from-CMake-package.patch"
    ]

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        sha256 = "5e33b6131cea6a904339734b015110d4342b7dc02d995164fdb86332d28a5aa4"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = "glm-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["GLM_TEST_ENABLE"] = False
        cmake.definitions["BUILD_SHARED_LIBS"] = False
        cmake.definitions["BUILD_STATIC_LIBS"] = False
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        tools.patch(base_path=self._source_subfolder, patch_file="0001-Remove-architecture-check-from-CMake-package.patch")
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="copying.txt", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        self.info.header_only()
