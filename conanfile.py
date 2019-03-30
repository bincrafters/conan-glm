#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class GlmConan(ConanFile):
    name = "glm"
    version = "0.9.9.4"
    description = "OpenGL Mathematics (GLM)"
    topics = ("conan", "glm", "opengl", "mathematics")
    url = "https://github.com/bincrafters/conan-glm"
    homepage = "https://github.com/g-truc/glm"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    no_copy_source = True

    exports = ["FindGLM.cmake", "LICENSE.md"]
    exports_sources = "platform.h.patch"

    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256="3a073eb8f3be07cee74481db0e1f78eda553b554941e405c863ab64de6a2e954")
        extracted_dir = "glm-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy("FindGLM.cmake")
        self.copy("*", src=os.path.join(self._source_subfolder, "glm"), dst=os.path.join("include", "glm"))
        self.copy("copying.txt", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
