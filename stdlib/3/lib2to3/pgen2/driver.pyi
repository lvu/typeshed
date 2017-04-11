# Stubs for lib2to3.pgen2.driver (Python 3.6)

from typing import Any, Callable, IO, Iterable, List, Optional, Text, Tuple

from logging import Logger
from lib2to3.pytree import _Context, _NL
from lib2to3.pgen2.grammar import Grammar

_RawNode = Tuple[int, Text, _Context, List[_NL]]
_Convert = Callable[[Grammar, _RawNode], _NL]


class Driver:
    grammar: Grammar
    logger: Logger
    convert: _Convert
    def __init__(self, grammar: Grammar, convert: Optional[_Convert] = ..., logger: Optional[Any] = ...) -> None: ...
    def parse_tokens(self, tokens: Iterable[Any], debug: bool = ...) -> _NL: ...
    def parse_stream_raw(self, stream: IO[Text], debug: bool = ...) -> _NL: ...
    def parse_stream(self, stream: IO[Text], debug: bool = ...) -> _NL: ...
    def parse_file(self, filename: Text, encoding: Optional[Text] = ..., debug: bool = ...) -> _NL: ...
    def parse_string(self, text: Text, debug: bool = ...) -> _NL: ...

def load_grammar(gt: Text = ..., gp: Optional[Text] = ..., save: bool = ..., force: bool = ..., logger: Optional[Logger] = ...) -> Grammar: ...
