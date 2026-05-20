# Descripcion: Analizador lexico/sintactico y generador LLVM IR para CLite extendido.
# Autor: Estefania, matricula pendiente.
# Fecha de modificacion: 2026-05-19.

# Se usa para interpretar de forma segura literales de strings y chars.
import ast as pyAst

# Permite recibir el archivo fuente por linea de comandos.
import sys

# Facilita leer archivos .clite desde disco.
from pathlib import Path

# PLY Lex construye el analizador lexico.
import ply.lex as lex

# PLY Yacc construye el analizador sintactico.
import ply.yacc as yacc

# Nodos del AST que el parser construye y que el generador LLVM recorre.
from arbol import (
    Assignment,
    BinaryOp,
    Block,
    BreakStatement,
    Case,
    Declaration,
    DoWhileStatement,
    EmptyStatement,
    ExpressionStatement,
    ForStatement,
    Function,
    FunctionCall,
    IfStatement,
    Literal,
    Parameter,
    Program,
    ReturnStatement,
    StringLiteral,
    SwitchStatement,
    UnaryOp,
    Variable,
    Visitor,
    WhileStatement,
)


# Palabras reservadas del lenguaje. Si el lexer lee alguno de estos textos,
# cambia el token de ID al token especial correspondiente.
KEYWORDS = {
    'int': 'INT',
    'bool': 'BOOL',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'return': 'RETURN',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'true': 'TRUE',
    'false': 'FALSE',
    'main': 'MAIN',
    'printf': 'PRINTF',
}

# Tokens con nombre. Los caracteres simples como '+', '-', '{' se manejan
# mediante la variable literals.
tokens = [
    'ID',
    'INTLIT',
    'FLOATLIT',
    'CHARLIT',
    'STRINGLIT',
    'LE',
    'GE',
    'EQ',
    'NEQ',
    'AND',
    'OR',
] + list(KEYWORDS.values())

# Expresiones regulares de operadores de mas de un caracter.
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NEQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'

# Espacios, tabs y retornos de carro se ignoran.
t_ignore = ' \t\r'

# Simbolos de un solo caracter que pueden aparecer en la gramatica.
literals = '+-*/%(){};=<>!,:'


# Ignora comentarios de una linea y comentarios de bloque.
def t_COMMENT(t):
    r'//[^\n]*|/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Reconoce cadenas entre comillas dobles para printf.
def t_STRINGLIT(t):
    r'"([^\\\n]|(\\.))*?"'
    t.value = pyAst.literal_eval(t.value)
    return t


# Reconoce literales de caracter como 'a' y los guarda como codigo ASCII.
def t_CHARLIT(t):
    r"'([^\\\n]|(\\.))'"
    t.value = ord(pyAst.literal_eval(t.value))
    return t


# Reconoce numeros con punto decimal.
def t_FLOATLIT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t


# Reconoce enteros.
def t_INTLIT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


# Reconoce identificadores y palabras reservadas.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = KEYWORDS.get(t.value, 'ID')
    return t


# Actualiza el numero de linea cuando aparecen saltos.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Reporta caracteres que no pertenecen al lenguaje.
def t_error(t):
    raise SyntaxError(f"Illegal character {t.value[0]!r} at line {t.lineno}")


# Construye el lexer con todas las reglas t_ definidas arriba.
lexer = lex.lex()

precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
)


# Regla auxiliar para representar producciones vacias.
def p_empty(p):
    """
    Empty :
    """
    p[0] = None


# Regla inicial: un programa es una lista de funciones.
def p_program(p):
    """
    Program : FunctionList
    """
    p[0] = Program(p[1])


# Construye la lista de funciones del programa.
def p_function_list(p):
    """
    FunctionList : Function
                 | FunctionList Function
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


# Reconoce una funcion completa: tipo, nombre, parametros y bloque.
def p_function(p):
    """
    Function : ReturnType FunctionName '(' ParametersOpt ')' Block
    """
    p[0] = Function(p[1], p[2], p[4], p[6])


# Permite usar nombres normales o main como nombre de funcion.
def p_function_name(p):
    """
    FunctionName : ID
                 | MAIN
    """
    p[0] = p[1]


# El tipo de retorno puede ser un tipo normal o void.
def p_return_type(p):
    """
    ReturnType : Type
               | VOID
    """
    p[0] = p[1]


# Tipos primitivos soportados por CLite.
def p_type(p):
    """
    Type : INT
         | BOOL
         | FLOAT
         | CHAR
    """
    p[0] = p[1]


# Lista de parametros opcional para permitir funciones sin parametros.
def p_parameters_opt(p):
    """
    ParametersOpt : Empty
                  | Parameters
    """
    p[0] = [] if p[1] is None else p[1]


# Construye una lista de parametros separados por coma.
def p_parameters(p):
    """
    Parameters : Parameter
               | Parameters ',' Parameter
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


# Reconoce un parametro individual: tipo y nombre.
def p_parameter(p):
    """
    Parameter : Type ID
    """
    p[0] = Parameter(p[1], p[2])


# Reconoce un bloque delimitado por llaves.
def p_block(p):
    """
    Block : '{' BlockItems '}'
    """
    p[0] = Block(p[2])


# Un bloque puede estar vacio o contener declaraciones/estatutos.
def p_block_items(p):
    """
    BlockItems : Empty
               | BlockItems BlockItem
    """
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]


# Un elemento de bloque puede ser declaracion o estatuto.
def p_block_item(p):
    """
    BlockItem : Declaration
              | Statement
    """
    p[0] = p[1]


# Reconoce declaraciones con inicializador opcional.
def p_declaration(p):
    """
    Declaration : Type ID ';'
                | Type ID '=' Expression ';'
    """
    initializer = None if len(p) == 4 else p[4]
    p[0] = Declaration(p[2], p[1], initializer)


# Reconoce todos los estatutos soportados por la actividad.
def p_statement(p):
    """
    Statement : ';'
              | Block
              | Assignment ';'
              | FunctionCall ';'
              | IfStatement
              | WhileStatement
              | ForStatement
              | DoWhileStatement
              | SwitchStatement
              | ReturnStatement
              | BreakStatement
    """
    if p.slice[1].type == ';':
        p[0] = EmptyStatement()
    elif len(p) == 3 and isinstance(p[1], FunctionCall):
        p[0] = ExpressionStatement(p[1])
    else:
        p[0] = p[1]


# Reconoce una asignacion sin el punto y coma final.
def p_assignment(p):
    """
    Assignment : ID '=' Expression
    """
    p[0] = Assignment(Variable(p[1]), p[3])


# Reconoce if con else opcional.
def p_if_statement(p):
    """
    IfStatement : IF '(' Expression ')' Statement ElsePart
    """
    p[0] = IfStatement(p[3], p[5], p[6])


# El else es opcional; IFX resuelve el dangling else.
def p_else_part(p):
    """
    ElsePart : Empty %prec IFX
             | ELSE Statement
    """
    p[0] = None if p[1] is None else p[2]


# Reconoce ciclo while.
def p_while_statement(p):
    """
    WhileStatement : WHILE '(' Expression ')' Statement
    """
    p[0] = WhileStatement(p[3], p[5])


# Reconoce ciclo for con inicializacion, condicion y actualizacion opcionales.
def p_for_statement(p):
    """
    ForStatement : FOR '(' ForInitOpt ';' ExpressionOpt ';' ForUpdateOpt ')' Statement
    """
    p[0] = ForStatement(p[3], p[5], p[7], p[9])


# Inicializacion opcional del for: nada, asignacion o declaracion con valor.
def p_for_init_opt(p):
    """
    ForInitOpt : Empty
               | Assignment
               | Type ID '=' Expression
    """
    if len(p) == 2:
        p[0] = None
    elif len(p) == 5:
        p[0] = Declaration(p[2], p[1], p[4])
    else:
        p[0] = p[1]


# Actualizacion opcional del for.
def p_for_update_opt(p):
    """
    ForUpdateOpt : Empty
                 | Assignment
    """
    p[0] = p[1]


# Expresion opcional usada por la condicion del for.
def p_expression_opt(p):
    """
    ExpressionOpt : Empty
                  | Expression
    """
    p[0] = p[1]


# Reconoce do/while, donde el cuerpo se ejecuta al menos una vez.
def p_do_while_statement(p):
    """
    DoWhileStatement : DO Statement WHILE '(' Expression ')' ';'
    """
    p[0] = DoWhileStatement(p[2], p[5])


# Reconoce switch con cases y default opcional.
def p_switch_statement(p):
    """
    SwitchStatement : SWITCH '(' Expression ')' '{' Cases DefaultOpt '}'
    """
    p[0] = SwitchStatement(p[3], p[6], p[7])


# Construye la lista de cases dentro de switch.
def p_cases(p):
    """
    Cases : Empty
          | Cases Case
    """
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]


# Reconoce un case con literal entero.
def p_case(p):
    """
    Case : CASE INTLIT ':' BlockItems
    """
    p[0] = Case(p[2], p[4])


# Default opcional dentro de switch.
def p_default_opt(p):
    """
    DefaultOpt : Empty
               | DEFAULT ':' BlockItems
    """
    p[0] = [] if len(p) == 2 else p[3]


# Reconoce return con o sin expresion.
def p_return_statement(p):
    """
    ReturnStatement : RETURN ';'
                    | RETURN Expression ';'
    """
    p[0] = ReturnStatement(None if len(p) == 3 else p[2])


# Reconoce break dentro de ciclos o switch.
def p_break_statement(p):
    """
    BreakStatement : BREAK ';'
    """
    p[0] = BreakStatement()


# Nivel mas bajo de precedencia: OR logico.
def p_expression(p):
    """
    Expression : Conjunction
               | Expression OR Conjunction
    """
    p[0] = p[1] if len(p) == 2 else BinaryOp(p[2], p[1], p[3])


# Segundo nivel de precedencia: AND logico.
def p_conjunction(p):
    """
    Conjunction : Equality
                | Conjunction AND Equality
    """
    p[0] = p[1] if len(p) == 2 else BinaryOp(p[2], p[1], p[3])


# Comparaciones de igualdad y desigualdad.
def p_equality(p):
    """
    Equality : Relation
             | Relation EquOp Relation
    """
    p[0] = p[1] if len(p) == 2 else BinaryOp(p[2], p[1], p[3])


# Operadores de igualdad.
def p_equ_op(p):
    """
    EquOp : EQ
          | NEQ
    """
    p[0] = p[1]


# Comparaciones relacionales.
def p_relation(p):
    """
    Relation : Addition
             | Addition RelOp Addition
    """
    p[0] = p[1] if len(p) == 2 else BinaryOp(p[2], p[1], p[3])


# Operadores relacionales.
def p_rel_op(p):
    """
    RelOp : '<'
          | LE
          | '>'
          | GE
    """
    p[0] = p[1]


# Suma y resta.
def p_addition(p):
    """
    Addition : Term
             | Addition AddOp Term
    """
    p[0] = p[1] if len(p) == 2 else BinaryOp(p[2], p[1], p[3])


# Operadores aditivos.
def p_add_op(p):
    """
    AddOp : '+'
          | '-'
    """
    p[0] = p[1]


# Multiplicacion, division y modulo.
def p_term(p):
    """
    Term : Factor
         | Term MulOp Factor
    """
    p[0] = p[1] if len(p) == 2 else BinaryOp(p[2], p[1], p[3])


# Operadores multiplicativos.
def p_mul_op(p):
    """
    MulOp : '*'
          | '/'
          | '%'
    """
    p[0] = p[1]


# Factor puede ser primario o primario con operador unario.
def p_factor(p):
    """
    Factor : Primary
           | UnaryOp Primary
    """
    p[0] = p[1] if len(p) == 2 else UnaryOp(p[1], p[2])


# Operadores unarios soportados.
def p_unary_op(p):
    """
    UnaryOp : '-'
            | '!'
    """
    p[0] = p[1]


# Elementos basicos de una expresion: variables, literales, llamadas o parentesis.
def p_primary(p):
    """
    Primary : ID
            | INTLIT
            | FLOATLIT
            | CHARLIT
            | TRUE
            | FALSE
            | STRINGLIT
            | FunctionCall
            | '(' Expression ')'
    """
    if len(p) == 2:
        token_type = p.slice[1].type
        if token_type == 'ID':
            p[0] = Variable(p[1])
        elif token_type == 'INTLIT':
            p[0] = Literal(p[1], 'int')
        elif token_type == 'FLOATLIT':
            p[0] = Literal(p[1], 'float')
        elif token_type == 'CHARLIT':
            p[0] = Literal(p[1], 'char')
        elif token_type == 'TRUE':
            p[0] = Literal(1, 'bool')
        elif token_type == 'FALSE':
            p[0] = Literal(0, 'bool')
        elif token_type == 'STRINGLIT':
            p[0] = StringLiteral(p[1])
        else:
            p[0] = p[1]
    else:
        p[0] = p[2]


# Reconoce una llamada de funcion y sus argumentos.
def p_function_call(p):
    """
    FunctionCall : CallName '(' ArgumentsOpt ')'
    """
    p[0] = FunctionCall(p[1], p[3])


# printf se trata como nombre de llamada especial, ademas de IDs normales.
def p_call_name(p):
    """
    CallName : ID
             | PRINTF
    """
    p[0] = p[1]


# Lista de argumentos opcional para permitir llamadas sin parametros.
def p_arguments_opt(p):
    """
    ArgumentsOpt : Empty
                 | Arguments
    """
    p[0] = [] if p[1] is None else p[1]


# Construye lista de argumentos separados por coma.
def p_arguments(p):
    """
    Arguments : Expression
              | Arguments ',' Expression
    """
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]


# Reporta errores de sintaxis con informacion del token.
def p_error(p):
    if p is None:
        raise SyntaxError("Unexpected end of input")
    raise SyntaxError(f"Syntax error at token {p.type} ({p.value!r}) line {p.lineno}")


# Construye el parser. write_tables=False evita generar parsetab.py nuevo.
parser = yacc.yacc(start='Program', write_tables=False, debug=False)


# llvmlite es necesario solo para generar LLVM IR; el parser puede existir sin el.
try:
    import llvmlite.binding as llvm
    import llvmlite.ir as ir
except ModuleNotFoundError:
    llvm = None
    ir = None


class IRGenerator(Visitor):
    """Recorre el AST y genera LLVM IR equivalente."""

    def __init__(self):
        """Inicializa modulo LLVM, tipos primitivos, tablas y printf."""
        if ir is None:
            raise RuntimeError("llvmlite no esta instalado. Ejecuta: pip install llvmlite")
        self.module = ir.Module(name="clite")
        self.i32 = ir.IntType(32)
        self.i8 = ir.IntType(8)
        self.i1 = ir.IntType(1)
        self.double = ir.DoubleType()
        self.void = ir.VoidType()
        self.voidptr = self.i8.as_pointer()
        self.functions = {}
        self.functionTypes = {}
        self.builder = None
        self.currentFunction = None
        self.currentReturnType = None
        self.scopes = []
        self.breakTargets = []
        self.stringCounter = 0
        self.ensurePrintf()

    def ensurePrintf(self):
        """Declara printf como funcion externa vararg, siguiendo el gist dado."""
        printf_ty = ir.FunctionType(self.i32, [self.voidptr], var_arg=True)
        self.functions['printf'] = ir.Function(self.module, printf_ty, name='printf')
        self.functionTypes['printf'] = ('int', None)

    def llvmType(self, typeName):
        """Convierte un tipo de CLite a su tipo equivalente en LLVM."""
        if typeName == 'void':
            return self.void
        if typeName == 'bool':
            return self.i1
        if typeName == 'char':
            return self.i8
        if typeName == 'float':
            return self.double
        return self.i32

    def lookup(self, name):
        """Busca una variable desde el scope mas interno hacia afuera."""
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(f"Variable no declarada: {name}")

    def currentScope(self):
        """Devuelve el scope activo para registrar variables locales."""
        return self.scopes[-1]

    def defaultValue(self, typeName):
        """Crea un valor cero apropiado para el tipo recibido."""
        if typeName == 'void':
            return None
        if typeName == 'float':
            return ir.Constant(self.double, 0.0)
        return ir.Constant(self.llvmType(typeName), 0)

    def cast(self, value, targetType):
        """Aplica conversion implicita basica entre bool, char, int y float."""
        target = self.llvmType(targetType) if isinstance(targetType, str) else targetType
        if value.type == target:
            return value
        if target == self.double:
            if value.type == self.i1:
                value = self.builder.zext(value, self.i32)
            return self.builder.sitofp(value, self.double)
        if value.type == self.double:
            if target == self.i1:
                zero = ir.Constant(self.double, 0.0)
                return self.builder.fcmp_ordered('!=', value, zero)
            return self.builder.fptosi(value, target)
        if target == self.i1:
            return self.toBool(value)
        if value.type.width < target.width:
            return self.builder.zext(value, target)
        if value.type.width > target.width:
            return self.builder.trunc(value, target)
        return value

    def toBool(self, value):
        """Convierte cualquier valor numerico soportado a condicion i1."""
        if value.type == self.i1:
            return value
        if value.type == self.double:
            return self.builder.fcmp_ordered('!=', value, ir.Constant(self.double, 0.0))
        return self.builder.icmp_signed('!=', value, ir.Constant(value.type, 0))

    def createString(self, value):
        """Crea una cadena global y regresa un i8* compatible con printf."""
        raw = value.encode('utf8') + b'\0'
        const = ir.Constant(ir.ArrayType(self.i8, len(raw)), bytearray(raw))
        name = f"str.{self.stringCounter}"
        self.stringCounter += 1
        global_str = ir.GlobalVariable(self.module, const.type, name=name)
        global_str.linkage = 'internal'
        global_str.global_constant = True
        global_str.initializer = const
        return self.builder.bitcast(global_str, self.voidptr)

    def generate(self, program):
        """Declara todas las funciones y despues genera el cuerpo de cada una."""
        for function in program.functions:
            self.declareFunction(function)
        for function in program.functions:
            function.accept(self)
        return self.module

    def declareFunction(self, node):
        """Registra la firma LLVM de una funcion antes de compilar cuerpos."""
        returnType = self.llvmType(node.returnType)
        paramTypes = [self.llvmType(param.type) for param in node.parameters]
        functionTy = ir.FunctionType(returnType, paramTypes)
        function = ir.Function(self.module, functionTy, name=node.name)
        for llvmArg, param in zip(function.args, node.parameters):
            llvmArg.name = param.name
        self.functions[node.name] = function
        self.functionTypes[node.name] = (node.returnType, [p.type for p in node.parameters])

    def visitProgram(self, node):
        """Punto de entrada del visitor para un programa completo."""
        return self.generate(node)

    def visitFunction(self, node):
        """Genera el bloque entry, parametros locales y cuerpo de una funcion."""
        self.currentFunction = self.functions[node.name]
        self.currentReturnType = node.returnType
        entry = self.currentFunction.append_basic_block('entry')
        self.builder = ir.IRBuilder(entry)
        self.scopes = [{}]
        self.breakTargets = []

        for arg, param in zip(self.currentFunction.args, node.parameters):
            ptr = self.builder.alloca(arg.type, name=param.name)
            self.builder.store(arg, ptr)
            self.currentScope()[param.name] = (ptr, param.type)

        node.body.accept(self)

        if not self.builder.block.is_terminated:
            if node.returnType == 'void':
                self.builder.ret_void()
            else:
                self.builder.ret(self.defaultValue(node.returnType))

    def visitBlock(self, node):
        """Genera los elementos de un bloque con un scope local."""
        self.scopes.append({})
        for item in node.items:
            if not self.builder.block.is_terminated:
                item.accept(self)
        self.scopes.pop()

    def visitDeclaration(self, node):
        """Genera alloca para una variable local e inicializa si corresponde."""
        typeRef = self.llvmType(node.type)
        ptr = self.builder.alloca(typeRef, name=node.name)
        self.currentScope()[node.name] = (ptr, node.type)
        if node.initializer is not None:
            value = node.initializer.accept(self)
            self.builder.store(self.cast(value, node.type), ptr)

    def visitAssignment(self, node):
        """Genera store para guardar el valor de una expresion en una variable."""
        ptr, varType = self.lookup(node.target.name)
        value = node.source.accept(self)
        value = self.cast(value, varType)
        self.builder.store(value, ptr)
        return value

    def visitEmptyStatement(self, node):
        """No genera codigo; representa un punto y coma aislado."""
        return None

    def visitExpressionStatement(self, node):
        """Genera una expresion usada como estatuto, por ejemplo printf."""
        return node.expression.accept(self)

    def visitIfStatement(self, node):
        """Genera bloques if-then, if-else opcional e if-exit."""
        condition = self.toBool(node.condition.accept(self))
        thenBlock = self.currentFunction.append_basic_block('if-then')
        elseBlock = self.currentFunction.append_basic_block('if-else') if node.elseBranch else None
        exitBlock = self.currentFunction.append_basic_block('if-exit')

        self.builder.cbranch(condition, thenBlock, elseBlock if elseBlock is not None else exitBlock)

        self.builder.position_at_end(thenBlock)
        node.thenBranch.accept(self)
        if not self.builder.block.is_terminated:
            self.builder.branch(exitBlock)

        if elseBlock is not None:
            self.builder.position_at_end(elseBlock)
            node.elseBranch.accept(self)
            if not self.builder.block.is_terminated:
                self.builder.branch(exitBlock)

        self.builder.position_at_end(exitBlock)

    def visitWhileStatement(self, node):
        """Genera while-head, while-body y while-exit."""
        head = self.currentFunction.append_basic_block('while-head')
        body = self.currentFunction.append_basic_block('while-body')
        exitBlock = self.currentFunction.append_basic_block('while-exit')
        self.builder.branch(head)
        self.builder.position_at_end(head)
        self.builder.cbranch(self.toBool(node.condition.accept(self)), body, exitBlock)
        self.builder.position_at_end(body)
        self.breakTargets.append(exitBlock)
        node.body.accept(self)
        self.breakTargets.pop()
        if not self.builder.block.is_terminated:
            self.builder.branch(head)
        self.builder.position_at_end(exitBlock)

    def visitForStatement(self, node):
        """Genera un ciclo for usando bloques head, body, step y exit."""
        if node.init is not None:
            node.init.accept(self)
        head = self.currentFunction.append_basic_block('for-head')
        body = self.currentFunction.append_basic_block('for-body')
        step = self.currentFunction.append_basic_block('for-step')
        exitBlock = self.currentFunction.append_basic_block('for-exit')
        self.builder.branch(head)
        self.builder.position_at_end(head)
        condition = self.i1(1) if node.condition is None else self.toBool(node.condition.accept(self))
        self.builder.cbranch(condition, body, exitBlock)
        self.builder.position_at_end(body)
        self.breakTargets.append(exitBlock)
        node.body.accept(self)
        self.breakTargets.pop()
        if not self.builder.block.is_terminated:
            self.builder.branch(step)
        self.builder.position_at_end(step)
        if node.update is not None:
            node.update.accept(self)
        self.builder.branch(head)
        self.builder.position_at_end(exitBlock)

    def visitDoWhileStatement(self, node):
        """Genera do/while; primero ejecuta body y luego evalua condicion."""
        body = self.currentFunction.append_basic_block('do-body')
        head = self.currentFunction.append_basic_block('do-head')
        exitBlock = self.currentFunction.append_basic_block('do-exit')
        self.builder.branch(body)
        self.builder.position_at_end(body)
        self.breakTargets.append(exitBlock)
        node.body.accept(self)
        self.breakTargets.pop()
        if not self.builder.block.is_terminated:
            self.builder.branch(head)
        self.builder.position_at_end(head)
        self.builder.cbranch(self.toBool(node.condition.accept(self)), body, exitBlock)
        self.builder.position_at_end(exitBlock)

    def visitSwitchStatement(self, node):
        """Genera switch LLVM con casos enteros y bloque default."""
        value = node.expression.accept(self)
        exitBlock = self.currentFunction.append_basic_block('switch-exit')
        defaultBlock = self.currentFunction.append_basic_block('switch-default')
        switch = self.builder.switch(value, defaultBlock)
        caseBlocks = []
        for case in node.cases:
            block = self.currentFunction.append_basic_block(f'switch-case-{case.value}')
            switch.add_case(ir.Constant(value.type, case.value), block)
            caseBlocks.append((block, case))

        self.breakTargets.append(exitBlock)
        for block, case in caseBlocks:
            self.builder.position_at_end(block)
            for statement in case.statements:
                if not self.builder.block.is_terminated:
                    statement.accept(self)
            if not self.builder.block.is_terminated:
                self.builder.branch(exitBlock)

        self.builder.position_at_end(defaultBlock)
        for statement in node.default:
            if not self.builder.block.is_terminated:
                statement.accept(self)
        if not self.builder.block.is_terminated:
            self.builder.branch(exitBlock)
        self.breakTargets.pop()
        self.builder.position_at_end(exitBlock)

    def visitBreakStatement(self, node):
        """Salta al bloque de salida del ciclo o switch activo."""
        if not self.breakTargets:
            raise SyntaxError("break fuera de ciclo o switch")
        self.builder.branch(self.breakTargets[-1])

    def visitReturnStatement(self, node):
        """Genera ret o ret_void segun el tipo de retorno de la funcion."""
        if self.currentReturnType == 'void':
            self.builder.ret_void()
            return
        value = self.defaultValue(self.currentReturnType) if node.expression is None else node.expression.accept(self)
        self.builder.ret(self.cast(value, self.currentReturnType))

    def visitLiteral(self, node):
        """Convierte literales CLite a constantes LLVM."""
        if node.type == 'float':
            return ir.Constant(self.double, node.value)
        if node.type == 'bool':
            return ir.Constant(self.i1, int(node.value))
        if node.type == 'char':
            return ir.Constant(self.i8, int(node.value))
        return ir.Constant(self.i32, int(node.value))

    def visitStringLiteral(self, node):
        """Genera una cadena global para llamadas a printf."""
        return self.createString(node.value)

    def visitVariable(self, node):
        """Genera load para leer el valor actual de una variable."""
        ptr, _ = self.lookup(node.name)
        return self.builder.load(ptr, name=node.name)

    def visitFunctionCall(self, node):
        """Genera call; printf usa argumentos variables."""
        function = self.functions[node.name]
        _, paramTypes = self.functionTypes[node.name]
        args = [arg.accept(self) for arg in node.arguments]
        if paramTypes is not None:
            args = [self.cast(arg, paramType) for arg, paramType in zip(args, paramTypes)]
        else:
            args = [self.cast(arg, 'int') if arg.type in (self.i1, self.i8) else arg for arg in args]
        return self.builder.call(function, args)

    def visitUnaryOp(self, node):
        """Genera operaciones unarias como negacion numerica o logica."""
        value = node.operand.accept(self)
        if node.op == '-':
            return self.builder.fneg(value) if value.type == self.double else self.builder.neg(value)
        if node.op == '!':
            return self.builder.not_(self.toBool(value))
        return value

    def visitBinaryOp(self, node):
        """Genera operaciones binarias aritmeticas, relacionales y logicas."""
        lhs = node.lhs.accept(self)
        rhs = node.rhs.accept(self)

        if lhs.type == self.double or rhs.type == self.double:
            lhs = self.cast(lhs, 'float')
            rhs = self.cast(rhs, 'float')
            if node.op == '+':
                return self.builder.fadd(lhs, rhs)
            if node.op == '-':
                return self.builder.fsub(lhs, rhs)
            if node.op == '*':
                return self.builder.fmul(lhs, rhs)
            if node.op == '/':
                return self.builder.fdiv(lhs, rhs)
            if node.op in ('<', '<=', '>', '>=', '==', '!='):
                return self.builder.fcmp_ordered(node.op, lhs, rhs)

        if node.op == '+':
            return self.builder.add(lhs, rhs)
        if node.op == '-':
            return self.builder.sub(lhs, rhs)
        if node.op == '*':
            return self.builder.mul(lhs, rhs)
        if node.op == '/':
            return self.builder.sdiv(lhs, rhs)
        if node.op == '%':
            return self.builder.srem(lhs, rhs)
        if node.op in ('<', '<=', '>', '>=', '==', '!='):
            return self.builder.icmp_signed(node.op, lhs, rhs)
        if node.op == '&&':
            return self.builder.and_(self.toBool(lhs), self.toBool(rhs))
        if node.op == '||':
            return self.builder.or_(self.toBool(lhs), self.toBool(rhs))
        raise NotImplementedError(f"Operador no soportado: {node.op}")


def parseSource(source: str):
    """Parsea codigo fuente CLite y devuelve la raiz del AST."""
    return parser.parse(source, lexer=lexer.clone())


def generateIr(source: str):
    """Parsea codigo CLite y genera el modulo LLVM IR correspondiente."""
    ast = parseSource(source)
    generator = IRGenerator()
    return generator.generate(ast)


def compileFile(path):
    """Lee un archivo .clite y genera su modulo LLVM IR."""
    source = Path(path).read_text(encoding='utf-8')
    return generateIr(source)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(compileFile(sys.argv[1]))
    else:
        demo = """
        int factorial(int n) {
            if (n <= 1) return 1;
            return n * factorial(n - 1);
        }

        int main() {
            int r;
            r = factorial(5);
            printf("factorial(5) = %d\\n", r);
            return r;
        }
        """
        print(generateIr(demo))
