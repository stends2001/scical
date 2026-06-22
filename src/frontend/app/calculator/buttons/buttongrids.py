from .buttons import Button, ButtonGrid

# ==================== #
###     GRID 1       ###
# ==================== #
buttons_grid1 = [
    [
        Button('1', 'input'),
        Button('2', 'input'),
        Button('3', 'input'),
        Button('/', 'input'),
    ],
    [
        Button('4', 'input'),
        Button('5', 'input'),
        Button('6', 'input'),
        Button('*', 'input'),
    ],
    [
        Button('7', 'input'),
        Button('8', 'input'),
        Button('9', 'input'),
        Button('-', 'input'),
    ],
    [  
        Button('ANS',   'system',   'ans'),           
        Button('0',     'input'),
        Button('.',     'input'),
        Button('+',     'input'),
    ],
    [             
        Button('(', 'input'),        
        Button(')', 'input'),    
        Button('<', 'system'),    
        Button('>', 'system'),                                 
    ],
    [
        Button('CLEAR', 'system',   'clear',    _span   =2),    
        Button('DEL',   'system',   'del',      col     =2),   
        Button('⌫',   'system',   'backspace', col     =3)           
    ],
]

# ==================== #
###     GRID 2       ###
# ==================== #
buttons_grid2 = [
    [
        Button('xⁿ',        'input', '**', "^"),
        Button('ⁿ√x',       'notimplemented'),
        Button('logₙ(x)',   'notimplemented'),
        Button('ln(x)',     'input',  'ln', 'ln'),
    ],

    [
        Button('sin(x)',    'input',   'sin',  'sin'),
        Button('cos(x)',    'input',  'cos',  'cos'),
        Button('tan(x)',    'input',  'tan',  'tan'),
        Button('π',          'input','pi'),        
    ],
    [
        Button('sin⁻¹(x)', 'notimplemented', 'math.asin', 'asin'),
        Button('cos⁻¹(x)', 'notimplemented', 'math.acos',  'acos'),
        Button('tan⁻¹(x)', 'notimplemented', 'math.atan',  'atan'),
        Button('e',        'input','e'),          
    ],
    [
        Button('...)',          'notimplemented',    '...',             '...'),
        Button('...',           'notimplemented',    '...',             '...'),
        Button('!',             'notimplemented',    '',             ''),
        Button('eˣ',            'input',            'exp'),        
    ],    
    [
        Button('abs(x)',        'notimplemented',    'abs',             'abs'),
        Button('round(x,n)',    'notimplemented',    'round x to n',    'notimplemented'),
        Button('nPr',           'notimplemented',    'npr',             'npr'),
        Button('nCr',           'notimplemented',    'nCr',             'nCr'),        
    ],
    [             
        Button('(', 'input'),        
        Button(')', 'input'),    
        Button('<', 'system'),    
        Button('>', 'system'),                                 
    ],
    [
        Button('CLEAR', 'system',   'clear',    _span   =2),    
        Button('DEL',   'system',   'del',      col     =2),   
        Button('⌫',   'system',   'backspace', col     =3)        
    ],
]

GRID1 = ButtonGrid(buttons_grid1, 6, 4)
GRID2 = ButtonGrid(buttons_grid2, 7, 4)