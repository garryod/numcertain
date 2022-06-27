from typing import Protocol, overload

class _UncertainOp(Protocol):
    @overload
    def __call__(self, other: bool, /) -> uncertain: ...
    @overload
    def __call__(self, other: int, /) -> uncertain: ...
    @overload
    def __call__(self, other: float, /) -> uncertain: ...
    @overload
    def __call__(self, other: uncertain, /) -> uncertain: ...

class uncertain:
    def __init__(self, nominal, uncertainity) -> None: ...
    __add__: _UncertainOp
    __radd__: _UncertainOp
    __sub__: _UncertainOp
    __rsub__: _UncertainOp
    __mul__: _UncertainOp
    __rmul__: _UncertainOp
    __truediv__: _UncertainOp
    __rtruediv__: _UncertainOp
