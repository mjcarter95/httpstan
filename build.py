from distutils.extension import Extension

from Cython.Build import cythonize

# when updating library paths, remember to update them in httpstan/models.py
include_dirs = [
    "httpstan",
    "httpstan/lib/stan/src",
    "httpstan/lib/stan/lib/stan_math",
    "httpstan/lib/stan/lib/stan_math/lib/eigen_3.3.3",
    "httpstan/lib/stan/lib/stan_math/lib/boost_1.69.0",
    "httpstan/lib/stan/lib/stan_math/lib/sundials_4.1.0/include",
]
extra_compile_args = [
    "-O3",
    "-std=c++14",
    # MinGW fix, https://github.com/python/cpython/pull/11283
    "-D_hypot=hypot",
]


extensions = [
    Extension(
        "httpstan.stan",
        sources=["httpstan/stan.pyx"],
        include_dirs=include_dirs,
        extra_compile_args=extra_compile_args,
    ),
    Extension(
        "httpstan.compile",
        sources=[
            "httpstan/compile.pyx",
            "httpstan/lib/stan/src/stan/lang/ast_def.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/bare_type_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/block_var_decls_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/expression07_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/expression_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/functions_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/indexes_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/local_var_decls_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/program_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/semantic_actions_def.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/statement_2_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/statement_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/term_grammar_inst.cpp",
            "httpstan/lib/stan/src/stan/lang/grammars/whitespace_grammar_inst.cpp",
        ],
        include_dirs=include_dirs,
        extra_compile_args=extra_compile_args,
        define_macros=[
            ("BOOST_DISABLE_ASSERTS", None),
            ("BOOST_PHOENIX_NO_VARIADIC_EXPRESSION", None),
        ],
    ),
]


def build(setup_kwargs):
    setup_kwargs.update({"ext_modules": cythonize(extensions)})
