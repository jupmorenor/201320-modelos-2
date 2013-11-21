% Definicion general del arbol de desicion
% arbol(0, arbol(1, arbol(1)), arbol(2, arbol(2)), arbol(3, arbol(3)), arbol(4, arbol(4))).

% Las posibilidades para la destruccion de elementos son las siguientes:

% 5 elementos en linea
posibilidad(1001, arbol(A, arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)))).
posibilidad(1002, arbol(A, arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(A, arbol(A)))).

% 5 elementos en L
posibilidad(1003, arbol(A, arbol(A, arbol(A)), arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(_, arbol(_)))).
posibilidad(1004, arbol(A, arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(A, arbol(A)), arbol(_, arbol(_)))).
posibilidad(1005, arbol(A, arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(A, arbol(A)))).
posibilidad(1006, arbol(A, arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)))).

% 5 elementos en T
posibilidad(1007, arbol(A, arbol(A, arbol(A)), arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)))).
posibilidad(1008, arbol(A, arbol(A, arbol(_)), arbol(A, arbol(A)), arbol(A, arbol(_)), arbol(_, arbol(_)))).
posibilidad(1009, arbol(A, arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(A)), arbol(A, arbol(_)))).
posibilidad(1010, arbol(A, arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(A)))).

% 4 elementos en linea
posibilidad(1011, arbol(A, arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)))).
posibilidad(1012, arbol(A, arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)))).
posibilidad(1013, arbol(A, arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(A, arbol(_)))).
posibilidad(1014, arbol(A, arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)))).

% 3 elementos en linea:
posibilidad(1015, arbol(A, arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(_, arbol(_)))).
posibilidad(1016, arbol(A, arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(_, arbol(_)))).
posibilidad(1017, arbol(A, arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)))).
posibilidad(1018, arbol(A, arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)))).
posibilidad(1019, arbol(A, arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)))).
posibilidad(1020, arbol(A, arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)))).


% Las posibilidades para la generacion de sugerencias son las siguientes:

sugerencia(2001, arbol(_, arbol(A, arbol(A)), arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(_, arbol(_)))).
sugerencia(2002, arbol(_, arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)))).
sugerencia(2003, arbol(_, arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)))).
sugerencia(2004, arbol(_, arbol(A, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(_, arbol(_)))).
sugerencia(2005, arbol(_, arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(A, arbol(_)), arbol(_, arbol(_)))).
sugerencia(2006, arbol(_, arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)), arbol(A, arbol(_)))).
sugerencia(2007, arbol(_, arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)))).
sugerencia(2008, arbol(_, arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(A)), arbol(_, arbol(_)))).
sugerencia(2009, arbol(_, arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)), arbol(A, arbol(_)))).
sugerencia(2010, arbol(_, arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)))).
sugerencia(2011, arbol(_, arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(A)))).
sugerencia(2012, arbol(_, arbol(_, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(A)))).
sugerencia(2013, arbol(_, arbol(A, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)))).
sugerencia(2014, arbol(_, arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(_)))).
sugerencia(2015, arbol(_, arbol(_, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(_)), arbol(A, arbol(_)))).
sugerencia(2016, arbol(_, arbol(A, arbol(_)), arbol(A, arbol(_)), arbol(_, arbol(_)), arbol(A, arbol(_)))).

% Las sugerencias se ofrecen unicamente para formar lineas de 3 elementos


% Consulta en tiempo de ejecucion
buscarPosibilidad(X, arbol(A, arbol(B, arbol(C)), arbol(D, arbol(E)), arbol(F, arbol(G)), arbol(H, arbol(I)))) :- posibilidad(X, arbol(A, arbol(B, arbol(C)), arbol(D, arbol(E)), arbol(F, arbol(G)), arbol(H, arbol(I)))).

% Consulta en tiempo de accion
buscarSugerencia(X, arbol(A, arbol(B, arbol(C)), arbol(D, arbol(E)), arbol(F, arbol(G)), arbol(H, arbol(I)))) :- sugerencia(X, arbol(A, arbol(B, arbol(C)), arbol(D, arbol(E)), arbol(F, arbol(G)), arbol(H, arbol(I)))).
