from setuptools import setup

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import ParallelCompile, Pybind11Extension, build_ext

__version__ = "1.0.0"

ext_modules = [
    Pybind11Extension(
        "predictor",
        sources=["predictor/src/predictor.cpp", "predictor.cpp"],
        cxx_std=17,
        define_macros=[("VERSION_INFO", __version__)],
        extra_compile_args=["-O3"],
        include_dirs=["predictor/src"],
    ),
]

# Optional multithreaded build
ParallelCompile("NPY_NUM_BUILD_JOBS").install()

setup(
    name="predictor",
    version=__version__,
    author="tomohxx",
    description="Predictor",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
