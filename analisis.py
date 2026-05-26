# Descripcion:
# Analizador lexico/sintactico y generador de LLVM IR para CLite.
# Autor(es):
# - Estefania Antonio Villaseca (A01736897)
# - Miranda Eugenia Colorado Arroniz (A01737023)
# - Alejandro Kong Montoya (A01734271)
# - Restituto Lara Larios (A01737216)
# Fecha de modificacion:
# 2026-05-24

"""
Descripcion: Analizador lexico/sintactico y generador de LLVM IR para CLite.
Autor(es): Estefania Antonio Villaseca (A01736897), Miranda Eugenia Colorado Arroniz (A01737023),
Alejandro Kong Montoya (A01734271), Restituto Lara Larios (A01737216).
Fecha de modificacion: 2026-05-24.
"""

import ast as pyAst
import sys
from pathlib import Path

import ply.lex as lex
import ply.yacc as yacc
from arbol import (
    Assignment,
    BinaryOp,
    Block,
    BreakStatement,
    Case,
    Declaration,
    Declarations,
    DoWhileStatement,
    EmptyStatement,
    Function,
    FunctionCall,
    ForStatement,
    IfStatement,
    Literal,
    Parameter,
    Program,
    ReturnStatement,
    StringLiteral,
    SwitchStatement,
    UnaryOp,
    Variable,
    WhileStatement,
)

# Tabla de palabras reservadas:
# Convierte texto como "if", "while" o "return" en tokens especiales
# para que el parser las trate como estructuras del lenguaje y no como IDs.
KEYWORDS = {
    'int': 'INT',
    'bool': 'BOOL',
    'float': 'FLOAT',
    'char': 'CHAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'printf': 'PRINTF',
    'return': 'RETURN',
    'break': 'BREAK',
    'main': 'MAIN',
}

tokens = [
    'ID',
    'INTLIT',
    'FLOATLIT',
    'CHARLIT',
    'STRINGLIT',
    'COMMENT',
    'LE',
    'GE',
    'EQ',
    'NEQ',
    'AND',
    'OR',
    'INT',
    'BOOL',
    'FLOAT',
    'CHAR',
    'TRUE',
    'FALSE',
    'IF',
    'ELSE',
    'WHILE',
    'DO',
    'FOR',
    'SWITCH',
    'CASE',
    'DEFAULT',
    'PRINTF',
    'RETURN',
    'BREAK',
    'MAIN',
]

# Precedencia minima usada para resolver el caso clasico de dangling else.
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
)

t_ignore  = ' \t'
literals = '+-*/%(){},;=<>!:'

t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NEQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'

def t_ID(t):
    # Proposito:
    # Lee nombres de variables/funciones y tambien palabras reservadas.
    # Parametros:
    # t = token que PLY esta construyendo.
    # Retorno:
    # El mismo token, con tipo "ID" o el tipo reservado correspondiente.
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = KEYWORDS.get(t.value, "ID")
    return t

def t_FLOATLIT(t):
    # Proposito:
    # Reconocer numeros con punto decimal, por ejemplo 3.14.
    # Parametros:
    # t = token que contiene el texto detectado.
    # Retorno:
    # Token con el valor convertido a float de Python.
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INTLIT(t):
    # Proposito:
    # Reconocer literales enteros, por ejemplo 0, 12 o 245.
    # Parametros:
    # t = token que contiene el literal.
    # Retorno:
    # Token con valor convertido a int.
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CHARLIT(t):
    # Proposito:
    # Reconocer caracteres entre comillas simples, por ejemplo 'a' o '\n'.
    # Parametros:
    # t = token leido por el lexer.
    # Retorno:
    # Token con el codigo entero del caracter (ASCII/Unicode code point).
    r"'([^\\\n]|(\\.))'"
    t.value = ord(pyAst.literal_eval(t.value))
    return t

def t_STRINGLIT(t):
    # Proposito:
    # Reconocer cadenas entre comillas dobles.
    # Parametros:
    # t = token leido por el lexer.
    # Retorno:
    # Token con la cadena ya interpretada (escapes incluidos).
    r'"([^\\\n]|(\\.))*?"'
    t.value = pyAst.literal_eval(t.value)
    return t


def t_COMMENT(t):
    # Proposito:
    # Ignorar comentarios de linea (//) y de bloque (/* ... */).
    # Parametros:
    # t = token que corresponde al comentario completo.
    # Retorno:
    # None, porque el comentario no participa en el parser.
    r"//[^\n]*|/\*(.|\n)*?\*/"
    t.lexer.lineno += t.value.count("\n")


def t_newline(t):
    # Proposito:
    # Llevar conteo de lineas para reportar errores con mejor ubicacion.
    # Parametros:
    # t = token de saltos de linea.
    # Retorno:
    # None.
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    """
    Maneja caracteres no validos del lexer.

    Parametros:
        t: Token invalido.

    Retorno:
        None.
    """
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def p_Program(p):
    # Proposito:
    # Construir el nodo raiz del AST para todo el programa.
    # Parametros:
    # p = estructura de produccion que usa PLY para intercambiar valores.
    # Retorno:
    # None (PLY deja el resultado sintetizado en p[0]).
    """
    Program : FunctionList
    """
    p[0] = Program(p[1])

def p_FunctionList(p):
    # Proposito:
    # Aplicar la regla gramatical de 'FunctionList' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    FunctionList : FunctionDef
                 | FunctionList FunctionDef
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_FunctionDef(p):
    # Proposito:
    # Aplicar la regla gramatical de 'FunctionDef' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    FunctionDef : ReturnType FunctionName '(' ParametersOpt ')' '{' DeclarationsOpt Statements '}'
    """
    p[0] = Function(p[1], p[2], p[4], p[7], p[8])

def p_DeclarationsOpt(p):
    # Proposito:
    # Aplicar la regla gramatical de 'DeclarationsOpt' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    DeclarationsOpt :
                    | Declarations
    """
    p[0] = p[1] if len(p) == 2 else None

def p_ReturnType(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ReturnType' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ReturnType : Type
    """
    p[0] = p[1]

def p_FunctionName(p):
    # Proposito:
    # Aplicar la regla gramatical de 'FunctionName' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    FunctionName : ID
                 | MAIN
    """
    p[0] = p[1]

def p_ParametersOpt(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ParametersOpt' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ParametersOpt :
                  | Parameters
    """
    p[0] = [] if len(p) == 1 else p[1]

def p_Parameters(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Parameters' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Parameters : ParameterDef
               | Parameters ',' ParameterDef
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_ParameterDef(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ParameterDef' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ParameterDef : Type ID
    """
    p[0] = Parameter(p[1], p[2])

def p_Declarations(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Declarations' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Declarations : Declarations Declaration
                 | Declaration
    """
    if len(p) == 2:
        p[0] = Declarations(None, p[1])
    else:
        p[0] = Declarations(p[1], p[2])


def p_Declaration(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Declaration' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Declaration : Type ID ';'
    """
    p[0] = Declaration(p[2], p[1])

def p_Type(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Type' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Type : INT
         | BOOL
         | FLOAT
         | CHAR
    """
    p[0] = p[1]

def p_Statements(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Statements' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Statements : Statements Statement
               | Statement
    """
    if len(p) == 2:
        p[0] = Block([p[1]])
    else:
        p[1].items.append(p[2])
        p[0] = p[1]

def p_Statement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Statement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Statement : ';'
              | Assignment
              | Block
              | IfStatement
              | WhileStatement
              | DoWhileStatement
              | ForStatement
              | SwitchStatement
              | ReturnStatement
              | FunctionCall ';'
              | BreakStatement
    """
    if p.slice[1].type == ';':
        p[0] = EmptyStatement()
    else:
        p[0] = p[1]

def p_Block(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Block' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Block : '{' Statements '}'
    """
    p[0] = Block(p[2].items)

def p_Assignment(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Assignment' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Assignment : ID '=' Expression ';'
    """
    p[0] = Assignment(Variable(p[1]), p[3])

def p_AssignmentNoSemicolon(p):
    # Proposito:
    # Aplicar la regla gramatical de 'AssignmentNoSemicolon' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    AssignmentNoSemicolon : ID '=' Expression
    """
    p[0] = Assignment(Variable(p[1]), p[3])

def p_IfStatement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'IfStatement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    IfStatement : IF '(' Expression ')' Statement ElsePart
    """
    p[0] = IfStatement(p[3], p[5], p[6])

def p_ElsePart(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ElsePart' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ElsePart : %prec IFX
             | ELSE Statement
    """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = p[2]

def p_WhileStatement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'WhileStatement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    WhileStatement : WHILE '(' Expression ')' Statement
    """
    p[0] = WhileStatement(p[3], p[5])

def p_DoWhileStatement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'DoWhileStatement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    DoWhileStatement : DO Statement WHILE '(' Expression ')' ';'
    """
    p[0] = DoWhileStatement(p[2], p[5])

def p_SwitchStatement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'SwitchStatement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    SwitchStatement : SWITCH '(' Expression ')' '{' Cases DefaultOpt '}'
    """
    p[0] = SwitchStatement(p[3], p[6], p[7])

def p_Cases(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Cases' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Cases :
          | Cases Case
    """
    if len(p) == 1:
        p[0] = []
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_Case(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Case' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Case : CASE INTLIT ':' Statements
    """
    p[0] = Case(p[2], p[4].items)

def p_DefaultOpt(p):
    # Proposito:
    # Aplicar la regla gramatical de 'DefaultOpt' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    DefaultOpt :
               | DEFAULT ':' Statements
    """
    if len(p) == 1:
        p[0] = []
    else:
        p[0] = p[3].items

def p_BreakStatement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'BreakStatement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    BreakStatement : BREAK ';'
    """
    p[0] = BreakStatement()

def p_ReturnStatement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ReturnStatement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ReturnStatement : RETURN ';'
                    | RETURN Expression ';'
    """
    p[0] = ReturnStatement(None if len(p) == 3 else p[2])

def p_ForStatement(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ForStatement' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ForStatement : FOR '(' ForInitOpt ';' ExpressionOpt ';' ForUpdateOpt ')' Statement
    """
    p[0] = ForStatement(p[3], p[5], p[7], p[9])

def p_ForInitOpt(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ForInitOpt' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ForInitOpt :
               | AssignmentNoSemicolon
               | Type ID '=' Expression
    """
    if len(p) == 1:
        p[0] = None
    elif len(p) == 5:
        p[0] = Declaration(p[2], p[1])
        p[0].initializer = p[4]
    else:
        p[0] = p[1]

def p_ForUpdateOpt(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ForUpdateOpt' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ForUpdateOpt :
                 | AssignmentNoSemicolon
    """
    p[0] = None if len(p) == 1 else p[1]

def p_ExpressionOpt(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ExpressionOpt' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ExpressionOpt :
                  | Expression
    """
    p[0] = None if len(p) == 1 else p[1]

def p_Expression(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Expression' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Expression : Conjunction
               | Expression OR Conjunction
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOp(p[2], p[1], p[3])

def p_Conjunction(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Conjunction' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Conjunction : Equality
                | Conjunction AND Equality
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOp(p[2], p[1], p[3])

def p_Equality(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Equality' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Equality : Relation
             | Relation EquOp Relation
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOp(p[2], p[1], p[3])

def p_EquOp(p):
    # Proposito:
    # Aplicar la regla gramatical de 'EquOp' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    EquOp : EQ
          | NEQ
    """
    p[0] = p[1]

def p_Relation(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Relation' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Relation : Addition
             | Addition RelOp Addition
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOp(p[2], p[1], p[3])

def p_RelOp(p):
    # Proposito:
    # Aplicar la regla gramatical de 'RelOp' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    RelOp : '<'
          | LE
          | '>'
          | GE
    """
    p[0] = p[1]


def p_Addition(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Addition' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Addition : Addition '+' Term
             | Addition '-' Term
             | Term
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOp(p[2], p[1], p[3])


def p_Term(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Term' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Term : Term '*' Factor
         | Term '/' Factor
         | Term '%' Factor
         | Factor
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOp(p[2], p[1], p[3])

def p_Factor(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Factor' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    '''
    Factor : Primary
           | UnaryOp Primary
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = UnaryOp(p[1], p[2])

def p_UnaryOp(p):
    # Proposito:
    # Aplicar la regla gramatical de 'UnaryOp' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    UnaryOp : '-'
            | '!'
    """
    p[0] = p[1]

def p_Primary(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Primary' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    '''
    Primary : INTLIT 
            | FLOATLIT
            | CHARLIT
            | STRINGLIT
            | TRUE
            | FALSE
            | ID
            | FunctionCall
            | '(' Expression ')'
    '''
    if len(p) == 2:
        token_type = p.slice[1].type
        if token_type == 'INTLIT':
            p[0] = Literal(p[1], 'int')
        elif token_type == 'FLOATLIT':
            p[0] = Literal(p[1], 'float')
        elif token_type == 'CHARLIT':
            p[0] = Literal(p[1], 'char')
        elif token_type == 'STRINGLIT':
            p[0] = StringLiteral(p[1])
        elif token_type == 'TRUE':
            p[0] = Literal(1, 'bool')
        elif token_type == 'FALSE':
            p[0] = Literal(0, 'bool')
        elif token_type == 'FunctionCall':
            p[0] = p[1]
        else:
            p[0] = Variable(p[1])
    else:
        p[0] = p[2]

def p_FunctionCall(p):
    # Proposito:
    # Aplicar la regla gramatical de 'FunctionCall' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    FunctionCall : CallName '(' ArgumentsOpt ')'
    """
    p[0] = FunctionCall(p[1], p[3])

def p_CallName(p):
    # Proposito:
    # Aplicar la regla gramatical de 'CallName' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    CallName : ID
             | PRINTF
    """
    p[0] = p[1]

def p_ArgumentsOpt(p):
    # Proposito:
    # Aplicar la regla gramatical de 'ArgumentsOpt' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    ArgumentsOpt :
                 | Arguments
    """
    p[0] = [] if len(p) == 1 else p[1]

def p_Arguments(p):
    # Proposito:
    # Aplicar la regla gramatical de 'Arguments' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Arguments : Expression
              | Arguments ',' Expression
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
        
def p_error(p):
    # Proposito:
    # Aplicar la regla gramatical de 'error' y construir/propagar el nodo AST correspondiente.
    # Parametros:
    # p = estructura de produccion de PLY usada para leer simbolos y guardar el resultado en p[0].
    # Retorno:
    # None. PLY toma el resultado sintetizado desde p[0].
    """
    Maneja errores de sintaxis del parser.

    Parametros:
        p: Token problematico.

    Retorno:
        None.
    """
    print("Syntax error in input!", p)


from arbol import Visitor
from llvmlite import ir

module = ir.Module(name="prog")
builder = None
current_func = None

class IRGenerator(Visitor):
    def __init__(self):
        """
        Prepara todas las estructuras internas para generar LLVM IR.

        Parametros:
            None.

        Retorno:
            None.
        """
        self.stack = []
        self.symbol_table = {}
        self.break_targets = []
        self.functions = {}
        self.function_signatures = {}
        self.current_return_type = None
        self.string_counter = 0
        self.i32 = ir.IntType(32)
        self.i8 = ir.IntType(8)
        self.i1 = ir.IntType(1)
        self.double = ir.DoubleType()
        self.voidptr = self.i8.as_pointer()
        self.ensure_printf()

    def ensure_printf(self):
        """
        Declara `printf` como funcion externa variadica en el modulo LLVM.

        Esto permite generar llamadas tipo C:
        printf("valor = %d\n", x)

        Parametros:
            None.

        Retorno:
            None.
        """
        printf_ty = ir.FunctionType(self.i32, [self.voidptr], var_arg=True)
        self.functions['printf'] = ir.Function(module, printf_ty, name='printf')
        self.function_signatures['printf'] = ('int', None)

    def create_string(self, value: str):
        """
        Crea una cadena global en LLVM a partir de un texto Python.

        La cadena se guarda como constante global y se regresa
        como puntero `i8*`, que es el formato esperado por `printf`.

        Parametros:
            value: Texto a almacenar en memoria global.

        Retorno:
            Puntero i8* a la cadena global.
        """
        raw = value.encode('utf8') + b'\0'
        const = ir.Constant(ir.ArrayType(self.i8, len(raw)), bytearray(raw))
        name = f"str.{self.string_counter}"
        self.string_counter += 1
        global_str = ir.GlobalVariable(module, const.type, name=name)
        global_str.linkage = 'internal'
        global_str.global_constant = True
        global_str.initializer = const
        return builder.bitcast(global_str, self.voidptr)

    def llvm_type(self, type_name: str):
        """
        Traduce un tipo de CLite a su tipo equivalente en LLVM.

        Parametros:
            type_name: Nombre de tipo en CLite.

        Retorno:
            Tipo LLVM equivalente.
        """
        if type_name == 'bool':
            return self.i1
        if type_name == 'char':
            return self.i8
        if type_name == 'float':
            return self.double
        return self.i32

    def cast(self, value, target_type):
        """
        Aplica conversiones implicitas basicas entre tipos soportados.

        Se usa para hacer compatibles expresiones y asignaciones
        cuando mezclan tipos distintos.

        Parametros:
            value: Valor LLVM de origen.
            target_type: Tipo destino CLite o tipo LLVM.

        Retorno:
            Valor convertido al tipo destino.
        """
        target = self.llvm_type(target_type) if isinstance(target_type, str) else target_type
        if value.type == target:
            return value

        if target == self.double:
            return builder.sitofp(value, self.double)

        if target == self.i1:
            if value.type == self.double:
                return builder.fcmp_ordered('!=', value, ir.Constant(self.double, 0.0))
            return builder.icmp_signed('!=', value, ir.Constant(value.type, 0))

        if value.type == self.double:
            return builder.fptosi(value, target)

        if value.type.width < target.width:
            return builder.zext(value, target)
        if value.type.width > target.width:
            return builder.trunc(value, target)
        return value

    def align_int_operands(self, lhs, rhs):
        """
        Alinea dos operandos enteros al mismo ancho de bits.

        Esto evita errores de tipo en operaciones binarias LLVM
        cuando cada lado tiene un tipo entero diferente.

        Parametros:
            lhs: Operando izquierdo.
            rhs: Operando derecho.

        Retorno:
            Par de operandos casteados al mismo tipo entero.
        """
        width = max(lhs.type.width, rhs.type.width, 32)
        target = ir.IntType(width)
        return self.cast(lhs, target), self.cast(rhs, target)

    def to_bool(self, value):
        """
        Convierte un valor LLVM a condicion booleana `i1`.

        En LLVM, los saltos condicionales requieren un i1.
        Este metodo normaliza enteros o flotantes a ese formato.

        Parametros:
            value: Valor LLVM origen.

        Retorno:
            Valor i1 utilizable en ramas condicionales.
        """
        if value.type == self.i1:
            return value
        if value.type == self.double:
            return builder.fcmp_ordered('!=', value, ir.Constant(self.double, 0.0))
        return builder.icmp_signed('!=', value, ir.Constant(value.type, 0))

    def declare_function(self, node: Function):
        """
        Registra la firma LLVM de una funcion antes de compilar su cuerpo.

        Este paso previo permite soportar llamadas entre funciones,
        incluyendo casos recursivos.

        Parametros:
            node: Nodo Function del AST.

        Retorno:
            None.
        """
        if node.name == 'printf':
            return
        param_types = [self.llvm_type(param.param_type) for param in node.parameters]
        fn_type = ir.FunctionType(self.llvm_type(node.return_type), param_types)
        fn = ir.Function(module, fn_type, name=node.name)
        for llvm_arg, param in zip(fn.args, node.parameters):
            llvm_arg.name = param.name
        self.functions[node.name] = fn
        self.function_signatures[node.name] = (node.return_type, [p.param_type for p in node.parameters])

    def default_return_value(self, type_name: str):
        """
        Construye un valor de retorno por defecto segun el tipo.

        Se usa cuando una funcion termina sin `return` explicito.

        Parametros:
            type_name: Tipo CLite de retorno.

        Retorno:
            Constante LLVM por defecto del tipo indicado.
        """
        if type_name == 'float':
            return ir.Constant(self.double, 0.0)
        if type_name == 'bool':
            return ir.Constant(self.i1, 0)
        if type_name == 'char':
            return ir.Constant(self.i8, 0)
        return ir.Constant(self.i32, 0)

    def visit_declarations(self, node: Declarations) -> None:
        """
        Recorre la lista enlazada de declaraciones locales.

        Va procesando declaracion por declaracion en orden.
        """
        node.decl.accept(self)
        if node.decls is not None:
            node.decls.accept(self)

    def visit_declaration(self, node: Declaration) -> None:
        """
        Reserva memoria local para una variable y la inicializa si aplica.
        """
        llvm_var_type = self.llvm_type(node.var_type)
        ptr = builder.alloca(llvm_var_type, name=node.name)
        self.symbol_table[node.name] = (ptr, node.var_type)
        if hasattr(node, 'initializer') and node.initializer is not None:
            node.initializer.accept(self)
            init_value = self.stack.pop()
            builder.store(self.cast(init_value, node.var_type), ptr)

    def visit_literal(self, node: Literal) -> None:
        """
        Convierte un literal del AST en una constante LLVM.
        """
        if node.type == 'float':
            self.stack.append(ir.Constant(self.double, node.value))
        elif node.type == 'bool':
            self.stack.append(ir.Constant(self.i1, int(node.value)))
        elif node.type == 'char':
            self.stack.append(ir.Constant(self.i8, int(node.value)))
        else:
            self.stack.append(ir.Constant(self.i32, int(node.value)))

    def visit_program(self, node: Program) -> None:
        """
        Compila el programa completo en dos pasadas.

        1) Primero declara firmas.
        2) Luego genera los cuerpos de funciones.
        """
        for function in node.functions:
            self.declare_function(function)
        for function in node.functions:
            function.accept(self)

    def visit_function(self, node: Function) -> None:
        """
        Compila una funcion completa.

        Crea bloque de entrada, registra parametros, compila declaraciones
        y statements, y agrega retorno por defecto si hace falta.
        """
        global builder, current_func
        current_func = self.functions[node.name]
        self.current_return_type = node.return_type
        self.symbol_table = {}
        self.break_targets = []
        self.stack = []

        entry = current_func.append_basic_block('entry')
        builder = ir.IRBuilder(entry)

        for arg, param in zip(current_func.args, node.parameters):
            ptr = builder.alloca(arg.type, name=param.name)
            builder.store(arg, ptr)
            self.symbol_table[param.name] = (ptr, param.param_type)

        if node.decls is not None:
            node.decls.accept(self)
        node.stmts.accept(self)

        if not builder.block.is_terminated:
            builder.ret(self.default_return_value(node.return_type))

    def visit_parameter(self, node: Parameter) -> None:
        """Metodo de compatibilidad del visitor para parametros."""
        return

    def visit_block(self, node: Block) -> None:
        """Compila, en orden, todos los statements de un bloque."""
        for statement in node.items:
            statement.accept(self)

    def visit_empty_statement(self, node: EmptyStatement) -> None:
        """No genera instrucciones para statement vacio."""
        return

    def visit_assignment(self, node: Assignment) ->  None:
        """
        Compila una asignacion de expresion a variable.

        Evalua la expresion, realiza cast si es necesario y guarda el valor.
        """
        node.source.accept(self)
        value = self.stack.pop()
        if node.target.name not in self.symbol_table:
            raise
        else:
            ptr, var_type = self.symbol_table[node.target.name]
            builder.store(self.cast(value, var_type), ptr)

    def visit_if_statement(self, node: IfStatement) -> None:
        """
        Compila un `if` (con o sin `else`) usando bloques LLVM.
        """
        cond_value = self.to_bool(self.eval_expr(node.condition))
        then_block = current_func.append_basic_block('if-then')
        else_block = current_func.append_basic_block('if-else') if node.else_branch is not None else None
        exit_block = current_func.append_basic_block('if-exit')

        builder.cbranch(cond_value, then_block, else_block if else_block is not None else exit_block)

        builder.position_at_end(then_block)
        node.then_branch.accept(self)
        if not builder.block.is_terminated:
            builder.branch(exit_block)

        if else_block is not None:
            builder.position_at_end(else_block)
            node.else_branch.accept(self)
            if not builder.block.is_terminated:
                builder.branch(exit_block)

        builder.position_at_end(exit_block)

    def visit_while_statement(self, node: WhileStatement) -> None:
        """Compila un ciclo `while` con bloques head/body/exit."""
        head_block = current_func.append_basic_block('while-head')
        body_block = current_func.append_basic_block('while-body')
        exit_block = current_func.append_basic_block('while-exit')

        builder.branch(head_block)
        builder.position_at_end(head_block)
        cond_value = self.to_bool(self.eval_expr(node.condition))
        builder.cbranch(cond_value, body_block, exit_block)

        builder.position_at_end(body_block)
        self.break_targets.append(exit_block)
        node.body.accept(self)
        self.break_targets.pop()
        if not builder.block.is_terminated:
            builder.branch(head_block)

        builder.position_at_end(exit_block)

    def visit_break_statement(self, node: BreakStatement) -> None:
        """
        Compila `break` saltando al bloque de salida del ciclo/switch actual.
        """
        if not self.break_targets:
            raise SyntaxError("break fuera de ciclo")
        builder.branch(self.break_targets[-1])

    def visit_return_statement(self, node: ReturnStatement) -> None:
        """Compila un `return` explicito o el retorno por defecto."""
        if node.expression is None:
            builder.ret(self.default_return_value(self.current_return_type))
            return
        value = self.eval_expr(node.expression)
        builder.ret(self.cast(value, self.current_return_type))

    def visit_function_call(self, node: FunctionCall) -> None:
        """
        Compila una llamada a funcion.

        Tambien ajusta tipos de argumentos para que coincidan con la firma.
        """
        if node.name not in self.functions:
            raise NameError(f"Funcion no declarada: {node.name}")
        fn = self.functions[node.name]
        _, param_types = self.function_signatures[node.name]
        args = [self.eval_expr(arg) for arg in node.arguments]
        if param_types is None:
            casted_args = [self.cast(arg, 'int') if arg.type in (self.i1, self.i8) else arg for arg in args]
        else:
            casted_args = [self.cast(arg, param_type) for arg, param_type in zip(args, param_types)]
        call_result = builder.call(fn, casted_args)
        self.stack.append(call_result)

    def visit_string_literal(self, node: StringLiteral) -> None:
        """Compila literal string a puntero global i8*."""
        self.stack.append(self.create_string(node.value))

    def visit_for_statement(self, node: ForStatement) -> None:
        """Compila un ciclo `for` usando bloques head/body/step/exit."""
        if node.init is not None:
            node.init.accept(self)

        head_block = current_func.append_basic_block('for-head')
        body_block = current_func.append_basic_block('for-body')
        step_block = current_func.append_basic_block('for-step')
        exit_block = current_func.append_basic_block('for-exit')

        builder.branch(head_block)
        builder.position_at_end(head_block)
        if node.condition is None:
            cond_value = ir.Constant(self.i1, 1)
        else:
            cond_value = self.to_bool(self.eval_expr(node.condition))
        builder.cbranch(cond_value, body_block, exit_block)

        builder.position_at_end(body_block)
        self.break_targets.append(exit_block)
        node.body.accept(self)
        self.break_targets.pop()
        if not builder.block.is_terminated:
            builder.branch(step_block)

        builder.position_at_end(step_block)
        if node.update is not None:
            node.update.accept(self)
        if not builder.block.is_terminated:
            builder.branch(head_block)

        builder.position_at_end(exit_block)

    def visit_do_while_statement(self, node: DoWhileStatement) -> None:
        """Compila un ciclo `do/while` usando bloques body/head/exit."""
        body_block = current_func.append_basic_block('do-body')
        head_block = current_func.append_basic_block('do-head')
        exit_block = current_func.append_basic_block('do-exit')

        builder.branch(body_block)
        builder.position_at_end(body_block)
        self.break_targets.append(exit_block)
        node.body.accept(self)
        self.break_targets.pop()
        if not builder.block.is_terminated:
            builder.branch(head_block)

        builder.position_at_end(head_block)
        cond_value = self.to_bool(self.eval_expr(node.condition))
        builder.cbranch(cond_value, body_block, exit_block)

        builder.position_at_end(exit_block)

    def visit_switch_statement(self, node: SwitchStatement) -> None:
        """
        Compila `switch/case/default` con la instruccion `switch` de LLVM.
        """
        switch_value = self.eval_expr(node.expression)
        switch_value = self.cast(switch_value, 'int')
        exit_block = current_func.append_basic_block('switch-exit')
        default_block = current_func.append_basic_block('switch-default')
        switch_inst = builder.switch(switch_value, default_block)

        case_blocks = []
        for case in node.cases:
            case_block = current_func.append_basic_block(f'switch-case-{case.value}')
            switch_inst.add_case(ir.Constant(switch_value.type, case.value), case_block)
            case_blocks.append((case_block, case))

        self.break_targets.append(exit_block)
        for case_block, case in case_blocks:
            builder.position_at_end(case_block)
            for statement in case.statements:
                if not builder.block.is_terminated:
                    statement.accept(self)
            if not builder.block.is_terminated:
                builder.branch(exit_block)

        builder.position_at_end(default_block)
        for statement in node.default:
            if not builder.block.is_terminated:
                statement.accept(self)
        if not builder.block.is_terminated:
            builder.branch(exit_block)

        self.break_targets.pop()
        builder.position_at_end(exit_block)

    def visit_case(self, node: Case) -> None:
        """Metodo de compatibilidad del visitor para Case."""
        return

    def eval_expr(self, node):
        """
        Evalua un nodo de expresion y regresa el valor LLVM producido.
        """
        node.accept(self)
        return self.stack.pop()

    def visit_variable(self, node: Variable) -> None:
        """
        Carga desde memoria el valor actual de una variable declarada.
        """
        if node.name not in self.symbol_table:
            raise NameError(f"Variable no declarada: {node.name}")
        ptr, _ = self.symbol_table[node.name]
        self.stack.append(
            builder.load(ptr, name=node.name)
        )

    def visit_binary_op(self, node: BinaryOp) -> None:
        """
        Compila operaciones binarias aritmeticas, logicas y relacionales.
        """
        node.lhs.accept(self)
        node.rhs.accept(self)
        rhs = self.stack.pop()
        lhs = self.stack.pop()

        if lhs.type == self.double or rhs.type == self.double:
            lhs = self.cast(lhs, 'float')
            rhs = self.cast(rhs, 'float')
            if node.op == '+':
                self.stack.append(builder.fadd(lhs, rhs))
            elif node.op == '-':
                self.stack.append(builder.fsub(lhs, rhs))
            elif node.op == '*':
                self.stack.append(builder.fmul(lhs, rhs))
            elif node.op == '/':
                self.stack.append(builder.fdiv(lhs, rhs))
            elif node.op == '%':
                self.stack.append(builder.frem(lhs, rhs))
            elif node.op in ('<', '<=', '>', '>=', '==', '!='):
                self.stack.append(builder.fcmp_ordered(node.op, lhs, rhs))
            elif node.op == '&&':
                self.stack.append(builder.and_(self.to_bool(lhs), self.to_bool(rhs)))
            elif node.op == '||':
                self.stack.append(builder.or_(self.to_bool(lhs), self.to_bool(rhs)))
            return

        lhs, rhs = self.align_int_operands(lhs, rhs)
        if node.op == '+':
            self.stack.append(
                builder.add(lhs, rhs)
            )
        elif node.op == '-':
            self.stack.append(
                builder.sub(lhs, rhs)
            )
        elif node.op == '*':
            self.stack.append(
                builder.mul(lhs, rhs)
            )
        elif node.op == '/':
            self.stack.append(
                builder.sdiv(lhs, rhs)
            )
        elif node.op == '%':
            self.stack.append(
                builder.srem(lhs, rhs)
            )
        elif node.op in ('<', '<=', '>', '>=', '==', '!='):
            self.stack.append(
                builder.icmp_signed(node.op, lhs, rhs)
            )
        elif node.op == '&&':
            self.stack.append(
                builder.and_(self.to_bool(lhs), self.to_bool(rhs))
            )
        elif node.op == '||':
            self.stack.append(
                builder.or_(self.to_bool(lhs), self.to_bool(rhs))
            )

    def visit_unary_op(self, node: UnaryOp) -> None:
        """Compila operaciones unarias (`-` y `!`)."""
        node.operand.accept(self)
        value = self.stack.pop()
        if node.op == '-':
            if value.type == self.double:
                self.stack.append(builder.fneg(value))
            else:
                self.stack.append(builder.neg(value))
        elif node.op == '!':
            self.stack.append(builder.not_(self.to_bool(value)))

# Punto de entrada utilitario:
# Este archivo se ejecuta en modo script para compilar un archivo fuente.
def parseSource(source: str):
    """
    Toma codigo fuente CLite y construye su AST.

    Parametros:
        source: Texto completo del programa fuente.

    Retorno:
        Nodo raiz del AST (o `None` si hay error de sintaxis).
    """
    lexer = lex.lex()
    parser = yacc.yacc()
    return parser.parse(source, lexer=lexer)


def generateIr(source: str):
    """
    Compila codigo CLite y genera un modulo LLVM IR listo para imprimirse.

    Parametros:
        source: Texto con codigo fuente CLite.

    Retorno:
        Modulo LLVM IR generado para el fuente recibido.
    """
    global module
    module = ir.Module(name="prog")
    root = parseSource(source)
    irgen = IRGenerator()
    root.accept(irgen)
    return module


def compileFile(path):
    """
    Lee un archivo CLite desde disco y genera su modulo LLVM IR.

    Parametros:
        path: Ruta al archivo fuente de entrada (`.c` o `.clite`).

    Retorno:
        Modulo LLVM IR correspondiente al archivo leido.
    """
    source = Path(path).read_text(encoding='utf-8')
    return generateIr(source)


def writeLlFileFromSource(path):
    """
    Compila un archivo fuente y escribe su salida LLVM IR en un `.ll`.

    Parametros:
        path: Ruta del archivo fuente de entrada.

    Retorno:
        Ruta del archivo `.ll` generado.
    """
    sourcePath = Path(path)
    outputPath = sourcePath.with_suffix('.ll')
    module = compileFile(str(sourcePath))
    outputPath.write_text(str(module), encoding='utf-8')
    return outputPath


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python analisis.py <archivo.c>")
        sys.exit(1)
    outputPath = writeLlFileFromSource(sys.argv[1])
    print(outputPath)
