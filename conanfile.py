#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os

class GlmConan(ConanFile):
    name = "glm"
    version = "0.9.8.5"
    description = "OpenGL Mathematics (GLM)"
    url = "https://github.com/bincrafters/conan-glm"
    homepage = "https://github.com/g-truc/glm"
    author = "Bincrafters <bincrafters@gmail.com>"
    topics = ("conan", "glm", "math", "opengl", "mathematics")
    license = "MIT"
    exports_sources = "0001-gcc7.patch"
    exports = ["LICENSE.md"]
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
        tools.patch(base_path=self._source_subfolder, patch_file="0001-gcc7.patch")

    def package(self):
        for pattern in ["*.h", "*.hpp", "*.inl"]:
            self.copy(pattern, src=os.path.join(self._source_subfolder, "glm"), dst=os.path.join("include", "glm"))
        self.copy("copying.txt", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
