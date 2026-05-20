# Descripcion: Nodos del arbol sintactico abstracto (AST) para el compilador CLite.
# Autor: Estefania, matricula pendiente.
# Fecha de modificacion: 2026-05-19.

from __future__ import annotations

from abc import ABC
from typing import Any


class ASTNode(ABC):
    """Clase base para todos los nodos del AST."""

    def accept(self, visitor):
        """Busca y ejecuta el metodo visit correspondiente en el visitor."""
        method = 'visit' + self.__class__.__name__
        return getattr(visitor, method)(self)


class Program(ASTNode):
    """Representa el programa completo, formado por una lista de funciones."""

    def __init__(self, functions):
        self.functions = functions


class Function(ASTNode):
    """Representa una funcion con tipo de retorno, nombre, parametros y cuerpo."""

    def __init__(self, returnType: str, name: str, parameters, body):
        self.returnType = returnType
        self.name = name
        self.parameters = parameters
        self.body = body


class Parameter(ASTNode):
    """Representa un parametro recibido por una funcion."""

    def __init__(self, type: str, name: str):
        self.type = type
        self.name = name


class Block(ASTNode):
    """Representa un bloque delimitado por llaves con declaraciones y estatutos."""

    def __init__(self, items):
        self.items = items


class Declaration(ASTNode):
    """Representa una declaracion local, opcionalmente con inicializador."""

    def __init__(self, name: str, type: str, initializer=None):
        self.name = name
        self.type = type
        self.initializer = initializer


class Assignment(ASTNode):
    """Representa una asignacion: variable = expresion."""

    def __init__(self, target, source):
        self.target = target
        self.source = source


class EmptyStatement(ASTNode):
    """Representa un estatuto vacio escrito como punto y coma."""

    pass


class IfStatement(ASTNode):
    """Representa una estructura if con rama else opcional."""

    def __init__(self, condition, thenBranch, elseBranch=None):
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch


class WhileStatement(ASTNode):
    """Representa un ciclo while."""

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ForStatement(ASTNode):
    """Representa un ciclo for con inicializacion, condicion, actualizacion y cuerpo."""

    def __init__(self, init, condition, update, body):
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body


class DoWhileStatement(ASTNode):
    """Representa un ciclo do/while, donde el cuerpo se ejecuta antes de evaluar."""

    def __init__(self, body, condition):
        self.body = body
        self.condition = condition


class SwitchStatement(ASTNode):
    """Representa un switch con casos y bloque default opcional."""

    def __init__(self, expression, cases, default):
        self.expression = expression
        self.cases = cases
        self.default = default


class Case(ASTNode):
    """Representa un case dentro de un switch."""

    def __init__(self, value: int, statements):
        self.value = value
        self.statements = statements


class BreakStatement(ASTNode):
    """Representa un break dentro de ciclos o switch."""

    pass


class ReturnStatement(ASTNode):
    """Representa un return con expresion opcional."""

    def __init__(self, expression=None):
        self.expression = expression


class ExpressionStatement(ASTNode):
    """Representa una expresion usada como estatuto, por ejemplo printf(...)."""

    def __init__(self, expression):
        self.expression = expression


class Literal(ASTNode):
    """Representa literales numericos, booleanos y caracteres."""

    def __init__(self, value: Any, type: str):
        self.value = value
        self.type = type


class StringLiteral(ASTNode):
    """Representa una cadena usada principalmente en llamadas a printf."""

    def __init__(self, value: str):
        self.value = value
        self.type = 'string'


class Variable(ASTNode):
    """Representa el uso de una variable por nombre."""

    def __init__(self, name: str):
        self.name = name


class FunctionCall(ASTNode):
    """Representa una llamada de funcion con lista de argumentos."""

    def __init__(self, name: str, arguments):
        self.name = name
        self.arguments = arguments


class UnaryOp(ASTNode):
    """Representa una operacion unaria como -x o !x."""

    def __init__(self, op: str, operand):
        self.op = op
        self.operand = operand


class BinaryOp(ASTNode):
    """Representa una operacion binaria como a + b o a <= b."""

    def __init__(self, op: str, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs


class Visitor(ABC):
    """Clase base para objetos que recorren el AST, como el generador LLVM."""

    pass
