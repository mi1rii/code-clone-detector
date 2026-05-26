# Descripcion:
# Definicion de nodos AST y Visitor para CLite.
# Autor(es):
# - Estefania Antonio Villaseca (A01736897)
# - Miranda Eugenia Colorado Arroniz (A01737023)
# - Alejandro Kong Montoya (A01734271)
# - Restituto Lara Larios (A01737216)
# Fecha de modificacion:
# 2026-05-24

"""
Descripcion: Definicion de nodos AST y Visitor para el compilador CLite.
Autor(es): Estefania Antonio Villaseca (A01736897), Miranda Eugenia Colorado Arroniz (A01737023),
Alejandro Kong Montoya (A01734271), Restituto Lara Larios (A01737216).
Fecha de modificacion: 2026-05-24.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ASTNode(ABC):
    """
    Clase base para todos los nodos del AST.

    Sirve para que cualquier nodo del arbol comparta la misma
    forma de ser visitado por un `Visitor`.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        """
        Recibe un visitor y redirige la ejecucion al metodo adecuado.

        Parametros:
            visitor: Objeto que implementa operaciones sobre el AST.
        Retorno:
            None.
        """
        pass


class Program(ASTNode):
    """
    Nodo raiz del AST.

    Guarda todas las funciones del programa CLite.
    """

    def __init__(self, functions: list[Function]) -> None:
        """
        Crea un programa con su lista de funciones.

        Parametros:
            functions: Lista de nodos `Function`.
        Retorno:
            None.
        """
        self.functions = functions

    def accept(self, visitor: Visitor):
        """Ejecuta `visit_program` del visitor sobre este nodo."""
        visitor.visit_program(self)


class Function(ASTNode):
    """
    Representa una funcion completa de CLite.

    Incluye tipo de retorno, nombre, parametros, declaraciones y cuerpo.
    """

    def __init__(
        self,
        return_type: str,
        name: str,
        parameters: list[Parameter],
        decls: Any,
        stmts: ASTNode,
    ) -> None:
        """
        Inicializa todos los campos de una funcion.

        Parametros:
            return_type: Tipo de retorno.
            name: Nombre de la funcion.
            parameters: Parametros formales.
            decls: Declaraciones locales.
            stmts: Bloque de statements.
        Retorno:
            None.
        """
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.decls = decls
        self.stmts = stmts

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar la funcion."""
        visitor.visit_function(self)


class Parameter(ASTNode):
    """Representa un parametro de entrada en una funcion."""

    def __init__(self, param_type: str, name: str) -> None:
        """Inicializa tipo y nombre del parametro."""
        self.param_type = param_type
        self.name = name

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el parametro."""
        visitor.visit_parameter(self)


class Declaration(ASTNode):
    """
    Nodo para declarar una variable.

    Tambien mantiene alias para compatibilidad con versiones anteriores.
    """

    def __init__(self, name: str, var_type: str) -> None:
        """Inicializa nombre y tipo de la variable declarada."""
        self.name = name
        self.var_type = var_type
        # Alias para compatibilidad con codigo previo.
        self.variable = name
        self.type = var_type

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar la declaracion."""
        visitor.visit_declaration(self)


class Declarations(ASTNode):
    """
    Estructura enlazada de declaraciones.

    Se conserva asi para no romper la estructura base del proyecto.
    """

    def __init__(self, decls: Declarations, decl: Declaration) -> None:
        """Inicializa un nodo con declaracion actual y resto de la lista."""
        self.decls = decls
        self.decl = decl

    def accept(self, visitor: Visitor):
        """Acepta un visitor para recorrer declaraciones."""
        visitor.visit_declarations(self)


class Assignment(ASTNode):
    """
    Nodo de asignacion.

    Guarda la variable destino y la expresion origen.
    """

    def __init__(self, target: Variable, source: ASTNode) -> None:
        """Inicializa variable destino y expresion origen."""
        self.target = target
        self.source = source
        # Alias para compatibilidad con codigo previo.
        self.variable = target.name
        self.expression = source

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar la asignacion."""
        visitor.visit_assignment(self)


class Block(ASTNode):
    """
    Agrupa varios statements en un solo nodo.

    Este nodo representa llaves `{ ... }` en el lenguaje.
    """

    def __init__(self, items: list[ASTNode]) -> None:
        """Inicializa lista de statements del bloque."""
        self.items = items

    def accept(self, visitor: Visitor):
        """Acepta un visitor para recorrer el bloque."""
        visitor.visit_block(self)


class EmptyStatement(ASTNode):
    """Representa el statement vacio `;`."""

    def accept(self, visitor: Visitor):
        """Acepta un visitor para el statement vacio."""
        visitor.visit_empty_statement(self)


class Literal(ASTNode):
    """
    Nodo para valores literales.

    Puede guardar enteros, flotantes, chars, bool, etc.
    """

    def __init__(self, value: Any, type: str) -> None:
        """Inicializa valor y tipo del literal."""
        self.value = value
        self.type = type

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el literal."""
        visitor.visit_literal(self)

    def __str__(self):
        """Devuelve representacion corta del literal."""
        return f"[LIT, {self.value}]"


class Variable(ASTNode):
    """
    Referencia a una variable por su identificador.

    El tipo puede ir definido o quedar como `None`.
    """

    def __init__(self, name: str, var_type: str | None = None) -> None:
        """Inicializa nombre de variable y tipo opcional."""
        self.name = name
        self.var_type = var_type
        # Alias para compatibilidad con codigo previo.
        self.type = var_type

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar la variable."""
        visitor.visit_variable(self)


class BinaryOp(ASTNode):
    """
    Operacion binaria entre dos expresiones.

    Ejemplos: suma, resta, comparaciones, operadores logicos.
    """

    def __init__(self, op: str, lhs: ASTNode, rhs: ASTNode) -> None:
        """Inicializa operador y operandos izquierdo/derecho."""
        self.lhs = lhs
        self.rhs = rhs
        self.op = op

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar la operacion binaria."""
        visitor.visit_binary_op(self)

    def __str__(self):
        """Devuelve representacion corta de operacion binaria."""
        return f"[{self.op}, {self.lhs}, {self.rhs}]"


class UnaryOp(ASTNode):
    """
    Operacion unaria sobre una expresion.

    Ejemplos tipicos: negacion aritmetica `-x` y logica `!x`.
    """

    def __init__(self, op: str, operand: ASTNode) -> None:
        """Inicializa operador unario y operando."""
        self.op = op
        self.operand = operand

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar la operacion unaria."""
        visitor.visit_unary_op(self)


class IfStatement(ASTNode):
    """
    Estructura condicional `if` con `else` opcional.
    """

    def __init__(
        self,
        condition: ASTNode,
        then_branch: ASTNode,
        else_branch: ASTNode | None = None,
    ) -> None:
        """Inicializa condicion, rama verdadera y rama opcional falsa."""
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el if."""
        visitor.visit_if_statement(self)


class WhileStatement(ASTNode):
    """Representa un ciclo `while`."""

    def __init__(self, condition: ASTNode, body: ASTNode) -> None:
        """Inicializa condicion de ciclo y cuerpo."""
        self.condition = condition
        self.body = body

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el while."""
        visitor.visit_while_statement(self)


class BreakStatement(ASTNode):
    """Representa la instruccion `break`."""

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar break."""
        visitor.visit_break_statement(self)


class ForStatement(ASTNode):
    """
    Representa un ciclo `for`.

    Sus partes de inicializacion, condicion y actualizacion
    pueden venir vacias.
    """

    def __init__(
        self,
        init: ASTNode | None,
        condition: ASTNode | None,
        update: ASTNode | None,
        body: ASTNode,
    ) -> None:
        """Inicializa inicializacion, condicion, actualizacion y cuerpo."""
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el for."""
        visitor.visit_for_statement(self)


class DoWhileStatement(ASTNode):
    """Representa un ciclo `do ... while`."""

    def __init__(self, body: ASTNode, condition: ASTNode) -> None:
        """Inicializa cuerpo y condicion del ciclo."""
        self.body = body
        self.condition = condition

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el do/while."""
        visitor.visit_do_while_statement(self)


class Case(ASTNode):
    """Representa un `case` dentro de un `switch`."""

    def __init__(self, value: int, statements: list[ASTNode]) -> None:
        """Inicializa valor del case y sus statements."""
        self.value = value
        self.statements = statements

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el case."""
        visitor.visit_case(self)


class SwitchStatement(ASTNode):
    """
    Representa una estructura `switch`.

    Incluye lista de `case` y bloque `default`.
    """

    def __init__(
        self,
        expression: ASTNode,
        cases: list[Case],
        default: list[ASTNode],
    ) -> None:
        """Inicializa expresion base, casos y bloque default."""
        self.expression = expression
        self.cases = cases
        self.default = default

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el switch."""
        visitor.visit_switch_statement(self)


class ReturnStatement(ASTNode):
    """Representa un `return` con expresion opcional."""

    def __init__(self, expression: ASTNode | None = None) -> None:
        """Inicializa la expresion opcional de retorno."""
        self.expression = expression

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el return."""
        visitor.visit_return_statement(self)


class FunctionCall(ASTNode):
    """Representa una llamada a funcion con cero o mas argumentos."""

    def __init__(self, name: str, arguments: list[ASTNode]) -> None:
        """Inicializa nombre de funcion y lista de argumentos."""
        self.name = name
        self.arguments = arguments

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar la llamada."""
        visitor.visit_function_call(self)


class StringLiteral(ASTNode):
    """Representa un literal de tipo cadena (`string`)."""

    def __init__(self, value: str) -> None:
        """Inicializa el texto de la cadena."""
        self.value = value
        self.type = "string"

    def accept(self, visitor: Visitor):
        """Acepta un visitor para procesar el string literal."""
        visitor.visit_string_literal(self)


class Visitor(ABC):
    """
    Interfaz base del patron Visitor.

    Define los metodos que cada visitor concreto debe implementar.
    """

    @abstractmethod
    def visit_program(self, node: Program) -> None:
        """Procesa un nodo Program."""
        pass

    @abstractmethod
    def visit_function(self, node: Function) -> None:
        """Procesa un nodo Function."""
        pass

    @abstractmethod
    def visit_parameter(self, node: Parameter) -> None:
        """Procesa un nodo Parameter."""
        pass

    @abstractmethod
    def visit_literal(self, node: Literal) -> None:
        """Procesa un nodo Literal."""
        pass

    @abstractmethod
    def visit_variable(self, node: Variable) -> None:
        """Procesa un nodo Variable."""
        pass

    @abstractmethod
    def visit_binary_op(self, node: BinaryOp) -> None:
        """Procesa un nodo BinaryOp."""
        pass

    @abstractmethod
    def visit_unary_op(self, node: UnaryOp) -> None:
        """Procesa un nodo UnaryOp."""
        pass

    @abstractmethod
    def visit_if_statement(self, node: IfStatement) -> None:
        """Procesa un nodo IfStatement."""
        pass

    @abstractmethod
    def visit_while_statement(self, node: WhileStatement) -> None:
        """Procesa un nodo WhileStatement."""
        pass

    @abstractmethod
    def visit_break_statement(self, node: BreakStatement) -> None:
        """Procesa un nodo BreakStatement."""
        pass

    @abstractmethod
    def visit_for_statement(self, node: ForStatement) -> None:
        """Procesa un nodo ForStatement."""
        pass

    @abstractmethod
    def visit_do_while_statement(self, node: DoWhileStatement) -> None:
        """Procesa un nodo DoWhileStatement."""
        pass

    @abstractmethod
    def visit_case(self, node: Case) -> None:
        """Procesa un nodo Case."""
        pass

    @abstractmethod
    def visit_switch_statement(self, node: SwitchStatement) -> None:
        """Procesa un nodo SwitchStatement."""
        pass

    @abstractmethod
    def visit_return_statement(self, node: ReturnStatement) -> None:
        """Procesa un nodo ReturnStatement."""
        pass

    @abstractmethod
    def visit_function_call(self, node: FunctionCall) -> None:
        """Procesa un nodo FunctionCall."""
        pass

    @abstractmethod
    def visit_string_literal(self, node: StringLiteral) -> None:
        """Procesa un nodo StringLiteral."""
        pass


class Calculator(Visitor):
    """
    Visitor de evaluacion simple.

    Se usa como apoyo para recorrer y calcular expresiones en memoria,
    sin generar LLVM IR.
    """

    def __init__(self):
        """Inicializa la pila usada durante la evaluacion."""
        self.stack = []

    def visit_literal(self, node: Literal) -> None:
        """Empuja el valor literal a la pila de evaluacion."""
        self.stack.append(node.value)

    def visit_variable(self, node: Variable) -> None:
        """Sin implementacion en el evaluador simple."""
        pass

    def visit_binary_op(self, node: BinaryOp) -> None:
        """
        Evalua una operacion binaria basica.

        Toma dos valores de la pila, aplica el operador y guarda el resultado.
        """
        node.lhs.accept(self)
        node.rhs.accept(self)
        rhs = self.stack.pop()
        lhs = self.stack.pop()
        if node.op == "+":
            self.stack.append(lhs + rhs)
        elif node.op == "-":
            self.stack.append(lhs - rhs)
        elif node.op == "*":
            self.stack.append(lhs * rhs)
        elif node.op == "/":
            self.stack.append(lhs / rhs)
        elif node.op == "%":
            self.stack.append(lhs % rhs)

    def visit_unary_op(self, node: UnaryOp) -> None:
        """
        Evalua una operacion unaria basica.

        Extrae un valor de la pila y aplica `-` o `!`.
        """
        node.operand.accept(self)
        value = self.stack.pop()
        if node.op == "-":
            self.stack.append(-value)
        elif node.op == "!":
            self.stack.append(0 if value else 1)

    def visit_if_statement(self, node: IfStatement) -> None:
        """
        Evalua un `if/else` en el evaluador simple.

        Ejecuta la rama verdadera o falsa segun la condicion.
        """
        node.condition.accept(self)
        cond = self.stack.pop()
        if cond:
            node.then_branch.accept(self)
        elif node.else_branch is not None:
            node.else_branch.accept(self)

    def visit_while_statement(self, node: WhileStatement) -> None:
        """
        Ejecuta un ciclo `while` en el evaluador simple.

        Repite el cuerpo mientras la condicion sea verdadera.
        """
        node.condition.accept(self)
        while self.stack.pop():
            node.body.accept(self)
            node.condition.accept(self)

    def visit_break_statement(self, node: BreakStatement) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_for_statement(self, node: ForStatement) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_do_while_statement(self, node: DoWhileStatement) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_case(self, node: Case) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_switch_statement(self, node: SwitchStatement) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_return_statement(self, node: ReturnStatement) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_function_call(self, node: FunctionCall) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_string_literal(self, node: StringLiteral) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_program(self, node: Program) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_function(self, node: Function) -> None:
        """No aplica en el evaluador simple actual."""
        return

    def visit_parameter(self, node: Parameter) -> None:
        """No aplica en el evaluador simple actual."""
        return
